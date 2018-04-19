
"""
Kaleb R. Horvath
November 11th, 2017 (START)
November 11th, 2017 (END)
7:09 AM (START)
7:26 AM (END)
---------------------
A sorting algorithm
written in Python 3.

"""

# Algorithm:

"""
[3, 6, 0, -2, -9]

append -9, remove -9
append -2, remove -2
...

[-9, -2, 0, 3, 6]
--------------------
Summary
--------------------
Append smallest
value to new array
and then remove that
value from orginal
and continue on with
iteration.
"""

# import basic libraries
import sys
import itertools

# create a sort function

def sort(listx):
	length = len(listx)
	nl = []
	for x in range(length):
		value = min(listx)
		nl.append(value)
		listx.remove(value)
	return nl












