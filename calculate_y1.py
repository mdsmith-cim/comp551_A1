import numpy as np
import logistic_regression

data = np.loadtxt('logistic_test.txt')

X = data[:, 0:2]

y = data[:,2].reshape(-1,1)

log_reg = logistic_regression.lg()

log_reg.fit(X,y)

