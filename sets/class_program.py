# Understanding hashing. We index data to find things. Like how a book contains an index.

# Sets are unordered and unique collections of data.

# Two types of copy: shallow and deep. Related to copy() function in built in functions of set.

"""
a = [1,2,3,[1,2]]
b = a.copy()

Here both a and b ids are different

but the ids of a[3] and b[3] is same. Thus, if we change a[3], b[3] will also change.

So a.copy() is a shallow copy

Use the copy module

import copy
b = copy.deepcopy(a)
"""

# HW: Implement all the built in functions of sets on lists

