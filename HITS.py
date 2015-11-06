import numpy as np
from math import sqrt
# construct link matrix M
# number of nodes is 4
n = 4

M = np.array([[0,1,1,0], [1,0,0,0],[0,0,0,1],[0,0,1,0]])
MT = M.transpose()

# initiailze hubs vector and authrotities vector
h = a = [1/sqrt(n)] * n

# epsilon to check convergence
eps = 1e-9

# compute hub and authority scores
diff = 1
while diff > eps:
	aOld, hOld = a, h
	a = MT.dot(h)
	a = np.divide(a, max(a), dtype=float) # normalize so that the max is 1
	h = M.dot(a)
	h = np.divide(h, max(h), dtype=float)
	diff = sum(abs(h - hOld) + abs(a - aOld))

print h, a