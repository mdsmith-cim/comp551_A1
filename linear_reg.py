import numpy as np

class linearReg:

    def __init__(self, X, y):

        self.X = np.insert(X, 0, 1,1)

        self.y = y.reshape((-1,1))

        self.w = np.zeros((self.X.shape[1], 1))

    # Fits linear model to data
    def fit(self):

        self.w = np.linalg.inv(self.X.T.dot(self.X)).dot(self.X.T).dot(self.y)

    # Predicts new values
    def predict(self, X):

        X2 = np.insert(X, 0, 1,1)
        return X2.dot(self.w)

    # Returns the coefficient of determination R^2 of the prediction.
    # Emulates scikit-learn choice of scoring method for ease of comparison
    # As defined in sk-learn:
    # The coefficient R^2 is defined as (1 - u/v), where u is the regression sum of squares
    # ((y_true - y_pred) ** 2).sum() and v is the residual sum of squares ((y_true - y_true.mean()) ** 2).sum().
    # Best possible score is 1.0 and it can be negative (because the model can be arbitrarily worse).
    # A constant model that always predicts the expected value of y, disregarding the input features,
    # would get a R^2 score of 0.0.
    def score(self, X, y):

        pred = self.predict(X).reshape(-1)
        y2 = y.reshape(-1)

        u = ((y2 - pred) ** 2).sum()
        v = ((y2 - y2.mean()) ** 2).sum()
        return 1 - u/v
