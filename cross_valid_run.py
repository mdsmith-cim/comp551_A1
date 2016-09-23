import numpy as np
import cross_valid as cv
import pandas as pd
from log_reg import lg
import pprint

## Get example data
wine = pd.read_csv("wine.csv")
y = (wine.Type == 'Red').values.reshape((-1, 1))
X = wine.loc[:, wine.columns[0:11]].values

# Set up cross validation for alpha
cross = cv.cross_valdiate(X, y, lg, {'alpha': [1e-7, 1e-6, 1e-5]}, {'max_iterations': 50000, 'error_threshold': 1e-6}, 4)

# Get result, print
best_result, all_results = cross.run()

pprint.pprint("Best results: {0}".format(best_result))


pprint.pprint("All results: {0}".format(best_result))
