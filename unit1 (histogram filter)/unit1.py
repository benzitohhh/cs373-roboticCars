import pdb

#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.


p  =  [0.2,     0.2,   0.2,   0.2,     0.2    ]
# p    =[0,       1,      0,    0,       0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'red', 'green', 'green']
motions=[1, 1, 1, 1]

pHit = 0.6
pMiss = 0.2

pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (world[i] == Z)
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    # normalise
    s = sum(q)
    for i in range(len(p)):
        q[i] /= s
    return q

def move(p, U):
    q = []
    for i in range (len(p)):
        s = pExact * p[(i-U) % len(p)]
        s += pOvershoot * p[(i-U-1) % len(p)]
        s += pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q

for k in range(len(measurements)):
    print k
    p = sense(p, measurements[k])
    p = move(p, motions[k])

print p