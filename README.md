Trend Analysis
==============

This block performs linear trend analysis on a set of numeric data. The method used is a least-square line fit, which will plot a line so that the sum of the squares of all points' error (vertical offsets, or residuals) is minimized. In such methods of linear regression, the solution contains the Y-Intercept and Slope values, and in this block some additional data and statistics are computed.

Example
===========

Consider a list of data such as `[6, 6, 7, 6, 7, 7, 8, 6, 8, 7]` where each value is a parameter's value (Y axis) at a time interval (X axis). This block first calculates the Y-intercept and Slope values, and then iterates through the data to calculate the error of that trend for each data point, and finally the Y value of the trend at the end of the data set. In this example we get the following results (rounded here for readability):

`{'trend_start': 6.145, 'trend_end': 7.455, 'trend': 0.145, 'std_error': 0.346}`

From this output we understand that the trend line for the data set is drawn from `6.145` at `X0`, and changes by `0.145` at each point on the X axis, ending at `7.455`. The standard error of `0.346` indicates how closely the line fits the data, returning 0.0 when the data set is perfectly linear. The value for the most recent data point in this example can be assumed to be `7.455±0.346 = 7.109~7.801` with a probability of 68% in a normal distribution (one standard deviation)


Properties
--------------
* **Data Set:** A list of numeric values with length of at least 2.

Dependencies
----------------
None

Commands
----------------
None

Input
-------
Any list of signals.

Output
---------
* **trend_start:** The first Y value of the trend line, this is the Y-Intercept value
* **trend_end:** The last Y value of the trend line, coincides with the last point in data
* **trend:** The rate of change for trend line, Slope, per X axis unit
* **std_error:** Standard deviation (sample) of absolute trend error (residual) for each point in data
* All attributes of input signal

If the input signal does not contain an acceptable list, and error is logged and no signals are notified.
