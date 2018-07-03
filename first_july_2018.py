# enumerate function
# this function is for list. if we use a dictionary, it prints the numeric index and the key 

# study: kruskal's algoritm

l1 = [1,2,3,4]

for x, y in enumerate(l1):
    print(x,y)

l1 = [1,2,3]
l2 = ['a','b']

result = {}
# the zip function takes n number of iterables. it returns a tuple to access all i-th index of all the iterators
# it iterates over the shortest of the iterables and raises StopIteration

for x, y in zip(l1, l2):
    result[x] = y

print(result)

# HW: study the following containers: bytearray, deque, defaultdict, ordereddict
# in 2.7, range is not a generator function. use xrange instead
# in 3.x, range is finally a generator function.