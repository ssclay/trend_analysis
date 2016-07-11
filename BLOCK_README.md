Example
===========

Consider a list of numeric values such as `[ 90, 85, 88, 87, 84 ]` where each Y value is separated by equal space along X axis.

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
* **trend_from:** The first Y value of the trend line, coincides with first point in `Data Set`
* **trend:** The rate of change for trend line, per X axis unit
Using the example list above, this block outputs `{'trend_from': xx, 'trend':, yy}` indicating that the overall trend is `yy` per point
