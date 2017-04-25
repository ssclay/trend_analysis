from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from unittest.mock import MagicMock
from ..trend_analysis_block import TrendAnalysis


class TestExample(NIOBlockTestCase):

    def test_process_signals(self):
    # Pass a list of three signals
        blk = TrendAnalysis()
        self.configure_block(blk, {
            "data": "{{ $data }}"
            })
        blk.start()
        blk.process_signals([
            Signal({"data": [5,4,3,2,1]}),
            Signal({"data": [3,3,4,3,5]}),
            Signal({"data": [3,3,3,3,3], "group": "null"})
            ])
        blk.stop()
        self.assert_num_signals_notified(3)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(), {
                "trend": -1.0,
                "trend_start": 5.0,
                "trend_end": 1.0,
                "data": [5,4,3,2,1],
                "std_error": 0.0
                })
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][1].to_dict(), {
                "trend": 0.4,
                "trend_start": 2.8,
                "trend_end": 4.4,
                "data": [3,3,4,3,5],
                "std_error":  0.33466401061363016
                })
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][2].to_dict(), {
                "trend": 0.0,
                "trend_start": 3.0,
                "trend_end": 3.0,
                "data": [3,3,3,3,3],
                "std_error": 0.0,
                "group": "null"
                })

    def test_string_input(self):
    # input is string, log error and notify no signals
        blk = TrendAnalysis()
        self.configure_block(blk, {
            "data": "{{ $data }}"
            })
        blk.logger = MagicMock()
        blk.start()
        blk.process_signals([
            Signal({"data": "not a list"})
            ])
        blk.stop()
        self.assert_num_signals_notified(0)
        blk.logger.error.assert_called_once_with(
            "Data Set must be a list with length > 1")
            
    def test_short_input(self):
    # input is list with length 1, log error and notify no signals
        blk = TrendAnalysis()
        self.configure_block(blk, {
            "data": "{{ $data }}"
            })
        blk.logger = MagicMock()
        blk.start()
        blk.process_signals([
            Signal({"data": [1]})
            ])
        blk.stop()
        self.assert_num_signals_notified(0)
        blk.logger.error.assert_called_once_with(
            "Data Set must be a list with length > 1")