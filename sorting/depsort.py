
"""
Kaleb R. Horvath
November 11th, 2017 (START)
November 11th, 2017 (END)
9:39 AM (START)
9:48 AM (END)
---------------------------
A simple sorting algorithm
meant for creating dependency
expressions.
"""

# Algorithm:
"""
(NOTE: in code, the below would be a dictionary like:
	tree = {'a':['x','y'], 'x':['c','k'], 'b':['a']}	
)

a depends on x, y
x depends on c, k
b depends on a

so... the proper expression...

[c, k, x, y, a, b]

"""

# Let us try a python implementation of the depsort algorithm

# import basic libaries
import sys
import itertools

def retDeps(visited, start):
    queue = []
    out = []
    queue.append(start)
    while queue:
        newNode = queue.pop(0)
        if newNode not in visited:
            visited.add(newNode)
        for child in depGraph[newNode]:
            queue.append(child)
            out.append(child)
    out.append(start)
    return out


def retDepGraph():
    visited = set()
    out = []
    # visited.add(given[0])
    for pac in given:
        if pac in visited:
            continue
        visited.add(pac)
        #out.append(pac)
        if pac in depGraph:
            # find all children
            for child in depGraph[pac]:
                if child in visited:
                    continue
                out.extend(retDeps(visited, child))
        out.append(pac)
    print(out)
retDepGraph()
