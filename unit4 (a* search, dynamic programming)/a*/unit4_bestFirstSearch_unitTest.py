from unit4_bestFirstSearch import *
import unittest
import pdb

class SimpleSearchTests(unittest.TestCase):
    def testIsGoal(self):
        for g in range(-10, 10):
            for i in range(-10, len(grid) + 10):
                for j in range(-10, len(grid[0]) + 10):
                    if [i, j] == goal:
                        self.assertTrue(isGoal([g, i, j]))
                    else:
                        self.assertFalse(isGoal([g, i, j]))                    
        
    def testIsVisited(self):
        visited = []
        self.checkIsVisited([0,0,0], visited, False)
        self.checkIsVisited([-2,3,7], visited, False)
        self.checkIsVisited([4,4,4], visited, False)
        visited = [[1,2,3],[4,5,6],[7,8,9]]
        self.checkIsVisited([0, 0, 0], visited, False)
        self.checkIsVisited([1,2,4], visited, False)
        self.checkIsVisited([7,6,9], visited, False)
        self.checkIsVisited([1,2,3], visited, True)
        self.checkIsVisited([2,2,3], visited, True)
        self.checkIsVisited([100,2,3], visited, True)
        self.checkIsVisited([1,5,6], visited, True)
        self.checkIsVisited([4,5,6], visited, True)
        self.checkIsVisited([100,5,6], visited, True)
        self.checkIsVisited([5,8,9], visited, True)
        self.checkIsVisited([7,8,9], visited, True)
        self.checkIsVisited([100,8,9], visited, True)
            
    def testApply(self):
        # delta = [[-1, 0 ], # go up
        #         [ 0, -1], # go left
        #         [ 1, 0 ], # go down
        #         [ 0, 1 ]] # go right
                
        up = delta[0]
        left = delta[1]
        down = delta[2]
        right = delta[3]
        
        # test move
        s = [0,2,1]
        self.checkApply(s, up, [1, 1, 1])
        self.checkApply(s, left, [1, 2, 0])
        self.checkApply(s, down, [1, 3, 1])
        self.checkApply(s, right, [1, 2, 2])
        
        # test off grid
        s = [0,0,0] # off grid up and left
        self.checkApply(s, up, None)
        self.checkApply(s, left, None)
        s = [0, len(grid)-1, len(grid[0])-1] # off grid down and right
        self.checkApply(s, down, None)
        self.checkApply(s, right, None)
        
        # test blocked
        s = [0,2,2] # blocked up
        self.checkApply(s, up, None)
        s = [0,0,3] # blocked left
        self.checkApply(s, left, None)
        s = [0,0,2] # blocked down
        self.checkApply(s, down, None)
        s = [0,0,1] # blocked right
        self.checkApply(s, right, None)
        
    def testExand(self):
        # 0, 0 - right, down
        self.checkExpand([0, 0, 0], [[1, 0, 1], [1, 1, 0]])
        # 2, 1 - all
        self.checkExpand([0, 2, 1], [[1, 1, 1], [1, 2, 0], [1, 3, 1], [1, 2, 2]])
        # 2, 3 - up, left
        self.checkExpand([0, 2, 3], [[1, 1, 3], [1, 2, 2]])
        # 4, 5 - up
        self.checkExpand([0, 4, 5], [[1, 3, 5]])

    def checkApply(self, s, d, expected):
        n = apply(s, d)
        self.assertEqual(expected, n)
        
    def checkIsVisited(self, s, visited, expected):
        b = isVisited(s, visited)
        self.assertEqual(expected, b)
    
    def checkExpand(self, s, expected):
        c = expand(s)
        for i in c:
            self.assertTrue(i in expected)
        for i in expected:
            self.assertTrue(i in c)
        
if __name__ == '__main__':
    unittest.main()