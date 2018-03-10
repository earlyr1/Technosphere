from numba import jit
import numpy as np
from math import sqrt

@jit(nopython=True)
def matrix_multiply(X, Y):
    """ Matrix multiplication
    Inputs:
      - X: A numpy array of shape (N, M)
      - Y: A numpy array of shape (M, K)
    Output:
      - out: A numpy array of shape (N, K)
    """
    Z = np.zeros((X.shape[0], Y.shape[1]))
    for i in range(X.shape[0]):
      for j in range(Y.shape[0]):
        for k in range(Z.shape[1]):
          Z[i][k] += X[i, j] * Y[j, k]

    return Z


@jit(nopython=True)
def matrix_rowmean(X, weights=np.empty((0,))):
    """ Calculate mean of each row.
    In case of weights do weighted mean.
    For example, for matrix [[1, 2, 3]] and weights [0, 1, 2]
    weighted mean equals 2.6666 (while ordinary mean equals 2)
    Inputs:
      - X: A numpy array of shape (N, M)
      - weights: A numpy array of shape (M,)
    Output:
      - out: A numpy array of shape (N,)
    """
    if weights.shape == (0,):

      res = [0.] * X.shape[0]
      for i in range(X.shape[0]):
        for j in range(X.shape[1]):
          res[i] += X[i, j]
        res[i] /= X.shape[1]
    
      return np.array(res)

    else:
      res = [0.] * X.shape[0]
      for i in range(X.shape[0]):
        for j in range(X.shape[1]):
          res[i] += weights[i] * X[i, j]
        res[i] /= X.shape[1]
    
      return np.array(res)


#@jit(nopython=True)
def cosine_similarity(X, top_n=10, with_mean=True, with_std=True):
    """ Calculate cosine similarity between each pair of row.
    1. In case of with_mean: subtract mean of each row from row
    2. In case of with_std: divide each row on it's std
    3. Select top_n best elements in each row or set other to zero.
    4. Compute cosine similarity between each pair of rows.
    Inputs:
      - X: A numpy array of shape (N, M)
      - top_n: int, number of best elements in each row
      - with_mean: bool, in case of subtracting each row's mean
      - with_std: bool, in case of subtracting each row's std
    Output:
      - out: A numpy array of shape (N, N)

    Example (with top_n=1, with_mean=True, with_std=True):
        X = array([[1, 2], [4, 3]])
        after mean and std transform:
        X = array([[-1.,  1.], [ 1., -1.]])
        after top n choice
        X = array([[0.,  1.], [ 1., 0]])
        cosine similarity:
        X = array([[ 1.,  0.], [ 0.,  1.]])

    """
    n = X.shape[0]
    m = X.shape[1]
    if with_mean:
      for i in range(n):
        mn = 0
        for j in range(m):
          mn += X[i, j]
        mn /= m
        for j in range(m):
          X[i, j] -= mn
    if with_std:
      for i in range(n):
        mn = 0
        for j in range(m):
          mn += X[i, j]
        mn /= m
        std = 0
        for j in range(m):
          std += (X[i, j] - mn) ** 2
        std /= m
        for j in range(m):
          X[i, j] /= std
    for i in range(n):
      for j in range(m - top_n):
        minabs = 0
        for k in range(m):
          if np.abs(X[i, k]) < X[i, minabs]:
            minabs = k
        X[i, minabs] = 0

    norm = np.zeros((n,))
    for i in range(n):
      for j in range(m):
        norm[i]+= X[i, j] ** 2
      norm[i] = sqrt(norm[i])
    dist = matrix_multiply(X, X.T)
    for i in range(n):
      for j in range(n):
        dist[i, j] /= (norm[i] * norm[j])

    return dist


a = np.array([[1.,0,0,0], [0,1,0,0], [0,0,0,1]])
#print matrix_multiply(a, a.T)
print cosine_similarity(a)