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

points = []
points.append(Point(28,145))
points.append(Point(65,140))
points.append(Point(50,130))
points.append(Point(25,125))
points.append(Point(55,118))
points.append(Point(38,115))
points.append(Point(44,105))
points.append(Point(29,97))
points.append(Point(50,90))
points.append(Point(63,88))
points.append(Point(43,83))
points.append(Point(35,63))
points.append(Point(55,63))
points.append(Point(50,60))
points.append(Point(42,57))
points.append(Point(23,40))
points.append(Point(64,37))
points.append(Point(50,30))
points.append(Point(33,22))
points.append(Point(55,20))

centroids = [Point(25,125),Point(44,105),Point(29,97),Point(35,63),Point(55,63),Point(42,97),Point(23,40),Point(64,37),Point(33,22),Point(55,20)]

def dist(a,b):
	"""
	Return distance between two points
	"""
	return sqrt(((a.x - b.x) ** 2 + (a.y - b.y) ** 2))

# computer closest centroid and assign it to the point
for point in points:
	d = float('inf')
	for centroid in centroids:
		if dist(point, centroid) < d:
			point.clusterCentroid = centroid
			d = dist(point, centroid)
print [point.getCoordinates() for point in points]
print [point.clusterCentroid.getCoordinates() for point in points]
print
print [centroid.getCoordinates() for centroid in centroids]

# construct clusters and calculate new centroids
clusters = {}
for point in points:
	if point.clusterCentroid.getCoordinates() in clusters:
		clusters[point.clusterCentroid.getCoordinates()].append(point.getCoordinates())
	else:
		clusters[point.clusterCentroid.getCoordinates()] = [point.getCoordinates()]

centroidsNew = []
for cluster, members in clusters.items():
	x, y = float(sum([x[0] for x in members])) / len(members), float(sum([x[1] for x in members])) / len(members)
	centroidsNew.append(Point(x,y))

# computer closest centroid and assign it to the point again
for point in points:
	d = float('inf')
	for centroid in centroidsNew:
		if dist(point, centroid) < d:
			point.clusterCentroid = centroid
			d = dist(point, centroid)
print
print [point.getCoordinates() for point in points]
print [point.clusterCentroid.getCoordinates() for point in points]
print
print [centroid.getCoordinates() for centroid in centroidsNew]