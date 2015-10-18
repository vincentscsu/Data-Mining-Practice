"""
Algorithm to count click-throughs of 5 advertisers based on their bids
and click-through-rate of three ad positions.
"""

ctr = [[0.1*0.15,0.1*0.01, 0.1*0.005, 1, 0], [0.09*0.016, 0.09*0.012, 0.09 * 0.006,2, 0], [0.08 * 0.017, 0.08 *0.014, 0.08*0.007,3, 0],[0.07*0.018, 0.07*0.015, 0.07*0.008, 4, 0], [0.06*0.019,0.06*0.016,0.06*0.01,5, 0]]

def findMax(l, i):
	_max = max([x[i] for x in l if x[3] - x[i] >= 0])
	return _max
	
def update(l, _max):
	for each in l:
		if each[i] == _max:
			each[3] -= _max
			each[4] += 1
			break
j = 101
while j > 0:
	for i in range(3):
		if j <= 0:
			break
		_max = findMax(ctr, i)
		update(ctr, _max)
		j -= 1

print ctr
