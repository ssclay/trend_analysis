from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase
from ..trend_analysis_block import TrendAnalysis


class TestExample(NIOBlockTestCase):

    def test_process_signals(self):
        """Signals pass through block unmodified."""
        blk = TrendAnalysis()
        self.configure_block(blk, {
            "x": [10,9,8,7,6,5,4,3,2,1]
        })
        blk.start()
        blk.process_signals([Signal({"hello": "n.io"})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(), {
                "trend": -1.0,
                "trend_start": 10.0,
                "trend_end": 1.0,
                "hello": "n.io"
            })
