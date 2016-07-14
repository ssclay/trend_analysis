Trend Analysis
==============

This block performs linear regression analysis by least-squares-fitting a list of numeric data. The output is a line indicating trend for the data set.

Example
===========

Consider a list of numeric values such as `data = [10,9,8,7,6,5,4,3,2,1]` where each Y value is separated by equal space (time) along X the axis. This block outputs `{'trend_start': 10.0, 'trend_end': 1.0, 'trend': -1.0}`. A line can be plotted from `data[0], trend_start` to `data[-1], trend_end`, and at each point along the X axis the Y value of the line will vary from the previous point by `trend`.


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

If the input signal does not contain an acceptable list, and error is logged and no signals are notified.