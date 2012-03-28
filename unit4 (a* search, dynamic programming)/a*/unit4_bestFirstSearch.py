# import pdb

# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

# remember: s = [g, y, x]

def isGoal(s):
    if s[1:] == goal:
        return True
    return False

def isVisited(s, visited):
    for i in visited:
        if s[1:] == i[1:]:
            return True
    return False

def apply(s, d):
    # apply
    pos = [s[0]+1, s[1]+d[0], s[2]+d[1]]

    # check and return
    if (pos[1] > (len(grid)-1)) \
    or (pos[1] < 0) \
    or (pos[2] > len(grid[0])-1) \
    or (pos[2] < 0) \
    or grid[pos[1]][pos[2]] != 0 :
        return None
    return pos

def expand(s):
    children = []
    # for each direction, try to expand
    for d in delta:
        t = apply(s, d)
        if t is not None:
            children.append(t)
    return children

def search():
    visited = []
    frontier = [ [0] + init ]
    while len(frontier) > 0:
        s = frontier.pop()

        if isGoal(s):
            visited.append(s)
            return s

        # if already visited, ignore
        if isVisited(s, visited):
            continue
        
        # else, expand s...
        children = expand(s)
        frontier.extend(children)
        visited.append(s)
    return "fail"

print search()