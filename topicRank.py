import numpy as np

m = np.array([[0, 1, 0, 0], [0.5, 0, 0, 0], [0.5, 0, 0, 1],[0, 0, 1, 0]]) 

beta = 0.7

m = m.dot(beta)

w1, w2 = 2./3 * (1-beta), 1./3 * (1-beta)


m[0] += w1
m[1] += w2

r = np.array([0.25, 0.25, 0.25, 0.25])
n = len(r)

for _ in xrange(10000):
 	r = m.dot(r)
 	r += (1-sum(r))/n

print r
