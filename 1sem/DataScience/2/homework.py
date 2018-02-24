import numpy as np
from scipy.sparse import csc_matrix, csr_matrix
import scipy.spatial


print 1
chess = np.array([[1 - (i + j) % 2 for j in range(8)] for i in range(8)])
print chess
print ''

print 2
arr = np.random.randint(-500, 500, 10)
print arr
for i in range(3):
	arr[np.argmax(np.absolute(arr))] = 0
print arr
print ''

print 3
row = np.array([i for i in range(10)])
col = np.array([i for i in range(10)])
data = np.array([i * i for i in range(10)])
print csc_matrix((data, (row, col)), shape = (10, 10)).toarray()
print ''

print 4
print np.array([i for i in range(1, 26)]).reshape((5, 5)).T
print ''


vecpattern = [6, 7, 3, 5, 9]

matpattern = np.array(
			[[6, 3, 67, 5, 2],
			[-9, -4, -4, -5, -1],
			[2, 4, 1, 2, 6],
			[6, 7, 3, 5, 9]
			]
	)
print 5
help_ = np.linalg.norm(np.array([vecpattern for i in range(4)]) - matpattern, axis = 1)
print help_
print ''

print 6
f = lambda x: scipy.spatial.distance.cosine(x, np.array(vecpattern))
for i in matpattern:
	print f(i)

