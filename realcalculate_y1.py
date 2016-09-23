import numpy as np
from log_reg import lg
from sklearn.linear_model import LogisticRegression as LogisticRegressionSKL
import pandas as pd
import split_data as sp
import bayes as by
from sklearn.naive_bayes import GaussianNB

## Get formatted data
pastruns = pd.read_csv("FinalDataSets/Y1TrainSet.csv")
y = (pastruns.didTheyAttend==1).values.reshape((-1,1))
X = pastruns.loc[:,pastruns.columns[0:6]].values

## Cross validate
## Split train/test
X_train, X_test, y_train, y_test = sp.split(np.concatenate((X,y),axis=1))

## Run logistic regression
log_reg = lg(X_train, y_train, alpha=1e-6,error_threshold=1e-6,max_iterations=50000)
log_reg.fit()
accuracy = log_reg.score(X_test, y_test) * 100
print("Classification (test) accuracy: {0}%".format(accuracy))

## SK Learn comparison
logSKL = LogisticRegressionSKL(tol=5.4e-4,C=1e15)
logSKL.fit(X_train, y_train.ravel())
print("SK Learn results")
print("Test classification accuracy: {0}%".format(logSKL.score(X_test, y_test)*100))

## Bayes
bayes = by.naive_bayes(X_train, y_train)
bayes.fit()
accu = bayes.score(X_test, y_test)
print("Bayes class. accuracy: {0}%".format(accu * 100))

## SK learn test
gnb = GaussianNB()
gnb.fit(X_train, y_train.reshape(-1))
print("SK Learn Naive Bayes: {0}%".format(gnb.score(X_test, y_test.reshape(-1)) * 100))



