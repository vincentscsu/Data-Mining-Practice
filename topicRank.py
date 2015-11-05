import numpy as np

# initialize adjacency matrix
m = np.array([[0, 1, 0, 0], [0.5, 0, 0, 0], [0.5, 0, 0, 1],[0, 0, 1, 0]]) 

# teleportation parameter
beta = 0.7

# transform matrix
m = m.dot(beta)

w1, w2 = 2./3 * (1-beta), 1./3 * (1-beta) # weight assigned to first and second node
m[0] += w1
m[1] += w2

# initilize rank vector
r = np.array([0.25, 0.25, 0.25, 0.25])
n = len(r)

# compute rank (for simplicity just run 10000 times and assume convergence)
for _ in xrange(10000):
 	r = m.dot(r)
 	r += (1-sum(r))/n

print r
