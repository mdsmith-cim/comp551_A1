import numpy as np
import log_reg

# Tests against a toy dataset

# TODO: Add cross validation

data = np.genfromtxt('toy.csv', delimiter=',')

X_train = data[:70, :2]
X_test = data[-30:, :2]
y_train = data[:70, 2]
y_test = data[-30:, 2]

log_reg = log_reg.lg(X_train, y_train)

log_reg.fit()

y_as_int = y_test.reshape((y_test.shape[0], -1)).astype(np.int32)

result_as_int = log_reg.predict(X_test).astype(np.int32)

accuracy = (np.count_nonzero(result_as_int == y_as_int) / y_as_int.size)*100

print("Classification (test) accuracy: %f percent" % accuracy)



