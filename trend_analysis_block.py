from nio.block.base import Block
from nio.signal.base import Signal
from nio.util.discovery import discoverable
from nio.properties import Property
from nio.properties.version import VersionProperty


@discoverable
class TrendAnalysis(Block):


    data = Property(title='Data Set', default='')
    version = VersionProperty('0.1.0')
    
    def process_signals(self, signals):
        # Create empty list of signals to notify
        signals_to_notify = []
        for signal in signals:
            if (isinstance(self.data(signal), list) and
                    len(self.data(signal)) > 1):
                # Make sure input is a list with at least two values
                d = self.data(signal)
                trend,trend_start = self.linreg(range(len(d)),d)
                trend_end = [
                        trend * index + trend_start for index in range(len(d))
                        ][len(d)-1]
                # Create new signal attributes
                signal.trend = trend
                signal.trend_start = trend_start
                signal.trend_end = trend_end
                # Append signal to list signals_to_notify
                signals_to_notify.append(signal)
            else:
                # Raise exception, do not append signals_to_notify
                self.logger.exception(
                        "Data Set must be a list with length > 1"
                        )
        self.notify_signals(signals_to_notify)

    def linreg(self, X, Y):
        # Perform least-squares-fit of linear regression to a list of numeric
        # values
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
