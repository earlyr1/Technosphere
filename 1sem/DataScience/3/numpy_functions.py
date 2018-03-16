import numpy as np


def matrix_multiply(X, Y):
    return np.dot(X, Y)


def matrix_rowmean(X, weights=1):
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
    return np.mean(X * weights, axis = 1)


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
    if with_mean: X = X - np.mean(X.reshape(1, -1), axis = 1)
    if with_std: X = X / np.std(X.reshape(1, -1), axis = 1)
    print X
    for i in range(X.shape[0]):
      for j in range(X.shape[1] - top_n):
        X[i][np.argmin(X[i])] = 0
    print X
    norms = np.linalg.norm(X, axis = 1)
    norms = np.dot(norms, norms.T)
    return np.dot(X, X.T) / norms
