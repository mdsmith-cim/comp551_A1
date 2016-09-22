import numpy as np
import sklearn.datasets as dataset
import linear_reg
import split_data as sp
from sklearn.linear_model import LinearRegression as SKLinear

bos = dataset.load_boston()

X = bos.data
y = bos.target

X_train, X_test, y_train, y_test = sp.split(np.concatenate((X,y.reshape((-1,1))),axis=1))

lin = linear_reg.linearReg(X_train,y_train)

lin.fit()

print("Linear regression R^2 error: {0}".format(lin.score(X_test, y_test)))

### SK Learn test

sk = SKLinear()

sk.fit(X_train, y_train)

print("SKLearn lin. regression R^2 error: {0}".format(sk.score(X_test, y_test)))



