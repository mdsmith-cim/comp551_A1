import numpy as np

class linearReg:

    def __init__(self, X, y):

        self.X = np.insert(X, 0, 1,1)

        self.y = y.reshape((-1,1))

        self.w = np.zeros((self.X.shape[1], 1))


    def fit(self):

        self.w = np.linalg.inv(self.X.T * self.X) * self.X.T * self.y


    def predict(self, X):

        return X * self.w

    def score(self,X,y):

        pred = self.predict(X)
        # TODO: Implement
        return 0