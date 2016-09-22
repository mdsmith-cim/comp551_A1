import numpy as np
import scipy.stats as st

class naive_bayes:

    # Implements Gaussian naive bayes

    def __init__(self,X, y):

        self.X = X

        # Make sure y has correct shape
        self.y = y.reshape(-1).astype(np.int32)

        if self.X.shape[0] != self.y.shape[0]:
            raise Exception('Number of rows in X and y should be the same')

    # Fits the data
    def fit(self):

        # Separate into each class: ex. 1 or 0
        uniq = np.unique(self.y)

        # Calculate mean / std. dev of each feature per class (attend/not attend as an example
        self.param = {}
        for i in uniq:
            # Get all related features
            features = self.X[self.y == i]
            ft_data = []
            # Iterate over each feature (column)
            for j in range(0, features.shape[1]):
                one_feature = features[:,j]
                ft_data.append((np.mean(one_feature), np.std(one_feature)))

            self.param[i] = ft_data

    # Predicts results for given X
    def predict(self, X):

        y = []
        # Get each row
        for i in range(0,X.shape[0]):

            row = X[i,:]

            best_class = None
            best_prob = -99

            # Test each potential class (usually 2)
            for cl in self.param.keys():
                dt = self.param[cl]
                num_feat = len(dt)

                gaussian = 1
                for k in range(0, num_feat):
                    # Create gaussian
                    gaussian *= st.norm.pdf(row[k], dt[k][0], dt[k][1])

                if gaussian > best_prob:
                    best_prob = gaussian
                    best_class = cl

            y.insert(i, best_class)


        return np.asarray(y)

    # Returns classifcation accuracy for given X and y
    def score(self,X,y):
        pred = self.predict(X)

        return np.count_nonzero(pred.astype(np.int32) == y.astype(np.int32).reshape(-1))/y.size