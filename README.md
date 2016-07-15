Trend Analysis
==============

This block performs linear regression analysis by least-squares-fitting a list of numeric data. The output is two points on a line indicating trend for the data set, and the rate of change for the trend.

Example
===========

Consider plotting a list of numeric values such as `[10,9,8,7,6,5,4,3,2,1]` where each Y value is separated by equal space (time) along X the axis. So at X0, Y = 10; at X1, Y = 9; and at X9, Y = 1. This block will output `{'trend_start': 10.0, 'trend_end': 1.0, 'trend': -1.0}`. The trend line can be plotted from `X0, trend_start` to `X9, trend_end` and the Y coordinate of the line will vary from adjacent points on the X axis by `trend`.

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
* **trend_start:** The first Y value of the trend line, coincides with first point in `Data Set`
* **trend_end:** The last Y value of the trend line, coincides with the last point in `Data Set`
* **trend:** The rate of change for trend line, per X axis unit
* All attributes of input signal

If the input signal does not contain an acceptable list, and error is logged and no signals are notified.
