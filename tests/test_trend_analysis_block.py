from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from unittest.mock import MagicMock
from ..trend_analysis_block import TrendAnalysis


class TestExample(NIOBlockTestCase):

    def test_process_signals(self):
        blk = TrendAnalysis()
        self.configure_block(blk, {
            "data": "{{ $data }}"
        })
        blk.start()
        blk.process_signals([
            Signal({"data": [5,4,3,2,1]}),
            Signal({"data": [1,2,3,4,5]}),
            Signal({"data": [3,3,3,3,3]})
            ])
        blk.stop()
        self.assert_num_signals_notified(3)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][2].to_dict(), {
                "trend": 0.0,
                "trend_start": 3.0,
                "trend_end": 3.0,
                "data": [3,3,3,3,3]
            })
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][1].to_dict(), {
                "trend": 1.0,
                "trend_start": 1.0,
                "trend_end": 5.0,
                "data": [1,2,3,4,5]
            })
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(), {
                "trend": -1.0,
                "trend_start": 5.0,
                "trend_end": 1.0,
                "data": [5,4,3,2,1]
            })
    """invalid input data, expected behavior is to log an error"""
    def test_invalid_input(self):
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
        self.assert_num_signals_notified(1)
        blk.logger.exception.assert_called_once_with("Data Set must be a list")