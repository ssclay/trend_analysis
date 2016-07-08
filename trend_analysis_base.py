from nio.block.base import Block
from nio.signal.base import Signal
from nio.properties.version import VersionProperty

class TrendAnalysisBase(Block):

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
