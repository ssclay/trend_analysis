from .trend_analysis_base import TrendAnalysisBase
from nio.util.discovery import discoverable
from nio.properties import Property
from nio.properties.version import VersionProperty


@discoverable
class TrendAnalysis(TrendAnalysisBase):

    version = VersionProperty('0.1.0')
    x = Property(title='Data Set', default='')

    def process_signals(self, signals):
        for signal in signals:
            x = self.x(signal)
            trend,trend_from = self.linreg(range(len(x)),x)
            signal.trend=trend
            signal.trend_from=trend_from
        self.notify_signals(signals)
