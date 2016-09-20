import numpy as np
# Expit = efficient implementation of sigmoid function
from scipy.special import expit

class lg:

    def __init__(self):
        self.alpha = 0.1
        self.epsilon = 1e-5
        self.w = 0
        self.num_iter = 100

    ## TODO: Add cross validation
    def fit(self, X,y):

        # Add row of 1's
        X2 = np.insert(X, 0, 1, 1)

        y2 = y.reshape((y.shape[0],-1))

        w = np.zeros((X2.shape[1], 1))

        error = self.epsilon + 1

        iterations = 0

        previous_error = self._err_w_(X2,y2,w)

        while error > self.epsilon and iterations < self.num_iter:
            update = self.alpha * np.sum(X2 * (y2 - expit(np.multiply(w.transpose(),  X2))), 0)
            w = w + update.reshape(w.shape)
            error_w = self._err_w_(X2, y2, w)
            error = np.sum(np.abs(error_w - previous_error))
            previous_error = error_w
            iterations += 1

        self.w = w

    # Note: for internal use
    def _err_w_(self, X, y, w):

        sig = expit(np.multiply(w.transpose(), X))
        return -np.sum(y * np.log(sig) + (1-y) * np.log(1-sig), axis=0)

    def predict(self, X):
        #TODO: write
        pass


    def getW(self):
        return self.w

    def setAlpha(self, alpha):
        self.alpha = alpha

    def setEpsilon(self, epsilon):
        self.epsilon = epsilon

    def setIter(self, iter):
        self.num_iter = iter