Example
===========

Consider a list of numeric values such as `[10,9,8,7,6,5,4,3,2,1]` where each Y value is separated by equal space along X axis.

Properties
--------------
* **Data Set:** A list of numeric values

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

Using the example list of data above, this block outputs `{'trend_start': 10.0, 'trend_end': 1.0, 'trend': -1.0}`. A line can be plotted from `trend_start` to `trend_end`, and each point along the X axis will vary from the previous point by the value of `trend`.
