import numpy as np
from log_reg import lg
from sklearn.linear_model import LogisticRegression as LogisticRegressionSKL
import pandas as pd
import split_data as sp
import bayes as by

# TODO: Add cross validation

# TODO: provide test against sk-learn


wine = pd.read_csv("wine.csv")
y = (wine.Type=='Red').values.astype(np.int32).reshape((-1,1))
X = wine.loc[:,wine.columns[0:11]].values


X_train, X_test, y_train, y_test = sp.split(np.concatenate((X,y),axis=1))


log_reg = lg(X_train, y_train, alpha=1e-6,error_threshold=1e-6,max_iterations=50000)

log_reg.fit()

y_as_int = y_test.reshape((y_test.shape[0], -1)).astype(np.int32)

result_as_int = log_reg.predict(X_test).astype(np.int32)

accuracy = (np.count_nonzero(result_as_int == y_as_int) / y_as_int.size)*100

print("Classification (test) accuracy: {} %".format(accuracy))

# SK Learn comparison
logSKL = LogisticRegressionSKL(tol=5.4e-4,C=1e15)
logSKL.fit(X_train, y_train.ravel())

print("SK Learn results")
print("Test classification accuracy: {} %".format(logSKL.score(X_test, y_test)*100))

### Bayes

bayes = by.naive_bayes(X_train, y_train)

bayes.fit()

pred = bayes.predict(X_test)



