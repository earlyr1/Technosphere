import numpy as np
from scipy.sparse import csc_matrix, csr_matrix
import scipy.spatial



chess = np.array([[1 - (i + j) % 2 for j in range(8)] for i in range(8)])
print chess
print ''

arr = np.random.randint(-500, 500, 10)
print arr
for i in range(3):
	tpl = np.argmax(np.absolute(arr))
	arr[tpl] = 0
print arr
print ''


row = np.array([i for i in range(10)])
col = np.array([i for i in range(10)])
data = np.array([i * i for i in range(10)])
print csc_matrix((data, (row, col)), shape = (10, 10)).toarray()
print ''


print np.array([i for i in range(1, 26)]).reshape((5, 5)).T
print ''

vecpattern = [6, 7, 3, 5, 9]
matpattern = np.array(
			[[6, 3, 67, 5, 2],
			[9, 4, 4, 5, 1],
			[2, 4, 1, 2, 6],
			[6, 7, 3, 5, 9]
			]
	)
help_ = np.linalg.norm(np.array([vecpattern for i in range(4)]) - matpattern, axis = 1)
print help_
print ''

f = lambda x: scipy.spatial.distance.cosine(x, vecpattern)
fv = np.vectorize(f)

print fv(matpattern)