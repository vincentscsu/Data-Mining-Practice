"""
Part of CURE clustering algorithm, getting representative points.
"""

from math import sqrt
class Point(object):
	"""
	A point in a 2-D dimension with it's assigned cluster
	"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.clusterCentroid = None

	def getCoordinates(self):
		return (self.x,self.y)

def dist(a,b):
	"""
	Return distance between two points
	"""
	return sqrt(((a.x - b.x) ** 2 + (a.y - b.y) ** 2))		

def maxIndex(l):
	m = float('-inf')
	for i in range(len(l)):
		if l[i] > m:
			m = l[i]
			j = i
	return j

points = []
points.append(Point(1,6))
points.append(Point(3,7))
points.append(Point(4,3))
points.append(Point(7,7))
points.append(Point(8,2))
points.append(Point(9,5))

repres = [Point(0,0), Point(10,10)]

for _ in range(5):
	minDs = []
	for point in points:
		minDs.append(min([dist(point, repre) for repre in repres]))
	idx = maxIndex(minDs)
	repres.append(points[idx])
	points.pop(idx)

for each in repres:
	print each.getCoordinates()