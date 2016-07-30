from nio.block.base import Block
from nio.signal.base import Signal
from nio.util.discovery import discoverable
from nio.properties import Property
from nio.properties.version import VersionProperty
import statistics


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
                dd = self.data(signal)
				# Plot trend line
                trend,trend_start = self.linreg(range(len(dd)),dd)
				trend_d = [
                        trend * index + trend_start for index in range(len(dd))
                        ]
                trend_end = trend_d[len(dd)-1]
				# Calculate standard error
				error = [trend_d - dd for trend_d, dd in zip(trend_d, dd)]
				std_error = statistics.stdev(error)
                # Create new signal attributes
                signal.trend = trend
                signal.trend_start = trend_start
                signal.trend_end = trend_end
				signal.std_error = std_error
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
