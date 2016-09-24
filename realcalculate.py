from sklearn.linear_model import LogisticRegression as LogisticRegressionSKL
import split_data as sp
import bayes as by
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from log_reg import lg
import pprint
import numpy as np
import linear_reg
import split_data as sp
import pandas as pd
from pandas import DataFrame
from sklearn.linear_model import LinearRegression as SKLinear

### Calculate Y1

## Get formatted data
pastruns = pd.read_csv("FinalDataSets/DataSetOn23rd/Y1TrainSet.csv")
y = pastruns.loc[:,pastruns.columns[-1]].values.reshape((-1,1))
#X = pastruns.loc[:,pastruns.columns[1:5]].values
X = pastruns.loc[:,pastruns.columns[1:4]].values

## Run logistic regression

## Split train/test
X_train, X_test, y_train, y_test = sp.split(np.concatenate((X,y),axis=1))

log_reg = lg(X_train, y_train, alpha=1e-6,error_threshold=1e-6,max_iterations=50000)
diff_list = log_reg.fit()


## Show plot for logistic regression showing difference < as iterations go on
# ax = plt.plot(diff_list)
# plt.ylabel("Log Likelihood Difference")
# plt.xlabel("Number of Iterations")
#
# plt.yscale('log')
#
# plt.show()

print("---- Logistic Regression -----")
accu, precision, recall, false_positive = log_reg.score(X_test, y_test)
print("TEST")
print("Precision: {0}\nRecall: {1}\nFalse Positives: {2}\nClass. Accuracy:{3}\n".format(precision, recall, false_positive, accu * 100))
accu, precision, recall, false_positive = log_reg.score(X_train, y_train)
print("TRAIN")
print("Precision: {0}\nRecall: {1}\nFalse Positives: {2}\nClass. Accuracy:{3}\n".format(precision, recall, false_positive, accu * 100))

## SK Learn comparison
# logSKL = LogisticRegressionSKL(tol=5.4e-4,C=1e15)
# logSKL.fit(X_train, y_train.ravel())
# print("SK Learn results")
# print("Test classification accuracy: {0}%".format(logSKL.score(X_test, y_test)*100))

## Bayes
print("---- Naive Bayes ----")
bayes = by.naive_bayes(X_train, y_train)
bayes.fit()
accu, precision, recall, false_positive = bayes.score(X_test, y_test)
print("TEST")
print("Precision: {0}\nRecall: {1}\nFalse Positives: {2}\nClass. Accuracy:{3}\n".format(precision, recall, false_positive, accu * 100))
accu, precision, recall, false_positive = bayes.score(X_train, y_train)
print("TRAIN")
print("Precision: {0}\nRecall: {1}\nFalse Positives: {2}\nClass. Accuracy:{3}\n".format(precision, recall, false_positive, accu * 100))

## SK learn test
# gnb = GaussianNB()
# gnb.fit(X_train, y_train.reshape(-1))
# print("SK Learn Naive Bayes: {0}%".format(gnb.score(X_test, y_test.reshape(-1)) * 100))
#


### Calculate Y2

# Get formatted data
pastruns = pd.read_csv("FinalDataSets/DataSetOn23rd/Y2TrainingSet.csv")
y = pastruns.loc[:,pastruns.columns[-1]].values.reshape((-1,1))
X = pastruns.loc[:,pastruns.columns[1:4]].values

# Split
X_train, X_test, y_train, y_test = sp.split(np.concatenate((X,y.reshape((-1,1))),axis=1))

# Implemented Linear Reg Training
lin = linear_reg.linearReg(X_train, y_train)
lin.fit()
print("Linear regression Test R^2 error: {0}".format(lin.score(X_test, y_test)))
print("Linear regression Train R^2 error: {0}".format(lin.score(X_train, y_train)))

### SK Learn Training test
# sk = SKLinear()
# sk.fit(X_train, y_train)
# print("SKLearn lin. regression R^2 error: {0}".format(sk.score(X_test, y_test)))
#


##### ---- FINAL PREDICTIONS ----
####  Calculate final predictions for submission


## Y1
pastruns = pd.read_csv("FinalDataSets/DataSetOn23rd/Y1TestSet_Extended.csv")
X = pastruns.loc[:,pastruns.columns[1:4]].values
ids = pastruns.loc[:,pastruns.columns[0]].values


pred_logistic_reg = log_reg.predict(X).astype(np.int32).reshape(-1)
pred_bayes = bayes.predict(X).astype(np.int32).reshape(-1)


## Y2
pastruns = pd.read_csv("FinalDataSets/DataSetOn23rd/Y2TestSet_Extended.csv")
X = pastruns.loc[:,pastruns.columns[1:4]].values
ids = pastruns.loc[:,pastruns.columns[0]].values

pred_linear_reg = lin.predict(X)

pred_linear_reg2 = []
for i in range(0, pred_linear_reg.shape[0]):
    m, s = divmod(np.asscalar(pred_linear_reg[i]), 60)
    h, m = divmod(m, 60)
    pred_linear_reg2.append("{:0>2d}:{:1>2d}:{:2>2d}".format(int(h), int(m), int(s)))


## Prepare data for writing

listToWrite = [ids,pred_logistic_reg, pred_bayes, pred_linear_reg2]

df = DataFrame(listToWrite).transpose()

df.to_csv('FinalResults.csv',header=False, index=False)