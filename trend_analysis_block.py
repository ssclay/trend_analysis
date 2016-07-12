from nio.block.base import Block
from nio.signal.base import Signal
from nio.util.discovery import discoverable
from nio.properties import Property
from nio.properties.version import VersionProperty


@discoverable
class TrendAnalysis(Block):

    x = Property(title='Data Set', default='')
    version = VersionProperty('0.1.0')
    
    def process_signals(self, signals):
        for signal in signals:
            if isinstance(self.x(signal), list):
                x = self.x(signal)
                trend,trend_start = self.linreg(range(len(x)),x)
                trend_end = [trend * index + trend_start for index in range(len(x))][len(x)-1]
                signal.trend = trend
                signal.trend_start = trend_start
                signal.trend_end = trend_end
                self.notify_signals(signals)
            else:
                self.logger.exception("Data Set must be a list")
    """
    Perform least-squares-fit of linear regression to a list of numeric values
    """
    def linreg(self, X, Y):
        N = len(X)
        Sx = Sy = Sxx = Syy = Sxy = 0.0
        for x, y in zip(X, Y):
            Sx = Sx + x
            Sy = Sy + y
            Sxx = Sxx + x*x
            Syy = Syy + y*y
            Sxy = Sxy + x*y
        det = Sxx * N - Sx * Sx
        return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det
