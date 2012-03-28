colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]
measurements = ['green', 'green', 'green' ,'green', 'green']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
sensor_right = 0.7
p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

def sense(p, Z):
    q = []
    for i in range(nRows):
        r = []
        for j in range(nCols):
            hit = (colors[i][j] == Z)
            r.append(p[i][j] * (hit * pHit + (1-hit) * pMiss))
        q.append(r)
    # normalise
    s = 0
    for row in q:
        s += sum(row)
    for i in range(nRows):
        for j in range(nCols):
            q[i][j] /= s
    return q

def move(p, U): # i.e. U is [x,y], where x,y are in {-1, 0, 1}
    q = []
    for i in range (nRows):
        r = []
        for j in range(nCols):
            if U == [0,0]: # stationary
                s = p[i][j]            
            elif U == [0,1]: # right
                s = pMove * p[i][(j-1)%nCols]
                s += pStationary * p[i][j]            
            elif U == [0,-1]: # left
                s = pMove * p[i][(j+1)%nCols]
                s += pStationary * p[i][j]            
            elif U == [1,0]: # down
                s = pMove * p[(i-1)%nRows][j]
                s += pStationary * p[i][j]            
            elif U == [-1,0]: # up
                s = pMove * p[(i+1)%nRows][j]
                s += pStationary * p[i][j]            
            else:
                print 'Big problem...'
            r.append(s)
        q.append(r)
    return q

def getInitialP(nRows, nCols, val):
    q = []
    for i in range(nRows):
        r = []
        for j in range(nCols):
            r.append(val)
        q.append(r)
    return q

nMeasurements = len(measurements)
nRows = len(colors)
nCols = len(colors[0])
uniformP = 1./(nRows*nCols)
pHit = sensor_right
pMiss = 1-sensor_right
pMove = p_move
pStationary = (1 - pMove)

p = getInitialP(nRows, nCols, uniformP)
for k in range(nMeasurements):
    p = move(p, motions[k])
    p = sense(p, measurements[k])

show(p)