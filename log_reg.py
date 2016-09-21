import numpy as np
import progressbar

class lg:
    def __init__(self, X, y, error_threshold = 1e-4, alpha=0.1, max_iterations = 10000):

        # Define X : add ones column
        self.X = np.insert(X, 0, 1, 1)

        # Make sure y has correct shape
        self.y = y.reshape((y.shape[0], -1))

        self.w = np.zeros((self.X.shape[1], 1))

        self.error_threshold = error_threshold

        self.alpha = alpha

        self.max_iterations = max_iterations


    def fit(self):

        diff = self.error_threshold + 1

        old_likelihood = self.log_likelihood()
        iteration = 0

        print("Fitting with alpha = {}, error threshold = {} and {} maximum # of iterations".format(self.alpha, self.error_threshold, self.max_iterations))

        bar = progressbar.ProgressBar(max_value=self.max_iterations)

        while diff > self.error_threshold and iteration < self.max_iterations:
            # Sum takes care of the fact that we are doing all X_i at once; reshape ensures correct output shape
            self.w = self.w + self.alpha * ((self.y - self.sigmoid(self.X.dot(self.w))) * self.X).sum(0).reshape(self.w.shape)

            cur_likelihood = self.log_likelihood()
            diff = np.abs(cur_likelihood - old_likelihood)
            old_likelihood = cur_likelihood
            iteration += 1
            bar.update(iteration)

        bar.finish()

        # Clean up terminal from progress bar
        print("")

        print("Took %i iterations, difference = " % iteration, diff)


    def sigmoid(self, x):
        return 1/(1 + np.exp(-x))

    def log_likelihood(self):

        sig = self.sigmoid(self.X.dot(self.w))
        # Define epsilon
        epsilon = np.spacing(1)
        return -(self.y * np.log(sig+epsilon) + (1-self.y) * np.log(1-sig+epsilon)).sum()


    def predict(self, X):

        X2 = np.insert(X, 0, 1, 1)
        prod = self.sigmoid(X2.dot(self.w))
        prod[prod < 0.5] = 0
        prod[prod >= 0.5] = 1
        return prod
