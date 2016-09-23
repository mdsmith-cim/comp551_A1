import numpy as np

# Implements k-fold cross validation
class cross_valdiate:

    # X,y : input data, numpy matrix or array format
    # algorithm: reference to algorithm to run
    # parameters: dictionary of lists of parameters to vary e.g. {'alpha': [0.1,1,10], 'beta':[20,30]} will vary alpha
    # with value 0.1,1,10 and beta with 20 and 30.  Note that each parameter is tested separately; if you wish to test
    # all possible combinations, you will need to do it manually and call this function several times
    # fixed_parameters: dictionary of parameters that remain unchanged e.g. {'a': 1} means a = 1
    # num_folds : number (k) of folds to use.  Note this should evenly divide the number of rows in X and y, but if it
    # does not cross validation will still run except some rows at the end of X and y will not be used anywhere
    def __init__(self, X, y, algorithm, parameters, fixed_parameters, num_folds):

        # Sanity check
        if X.shape[0] != y.shape[0]:
            raise Exception("X and y should have the same number of rows")

        self.algo = algorithm
        self.param = parameters
        self.num_folds = num_folds
        self.fixed_parameters = fixed_parameters

        # Check to make sure user did not specify variable in both variable and fixed dictionaries
        for key in parameters.keys():
            if key in fixed_parameters:
                raise Exception('Key {0} found in both fixed and variable parameters'.format(key))

        fold_size = X.shape[0]/num_folds

        if not(fold_size.is_integer()):
            print("Warning: the data cannot be evenly split into {0} folds.".format(num_folds))
            print("Some data will be discarded.")

        fold_size = int(fold_size)

        self.all_folds = np.arange(self.num_folds)

        # Split X/y into lists based on folds
        self.X_list = []
        self.y_list = []

        for i in range(0, self.num_folds):
            self.X_list.append(X[i * fold_size : i * fold_size + fold_size,:])
            self.y_list.append(y[i * fold_size : i * fold_size + fold_size])


    # Run cross validation and check out different parameters
    # Returns a tuple
    # First entry: dictionary showing parameter name and best value
    # Second entry: dictionary showing parameter name and all calculated training/test errors for each tested value
    def run(self):

        best_parameters = {}
        all_scores = {}

        # Go over parameters and their potential values
        for param_name, param_values in self.param.items():

            best_score = -9999

            # Keep track of all train/test results
            all_scores[param_name] = {'train' : {}, 'test': {}}

            # Try out all potential values
            for v in param_values:

                test_scores = []
                train_scores = []

                # Run on all folds
                for fld in range(0,self.num_folds):

                    # Define folds
                    test_fold = self.all_folds[fld]
                    train_folds = self.all_folds[self.all_folds != fld]

                    # Define test, train sets based on folds
                    X_test = self.X_list[test_fold]
                    y_test = self.y_list[test_fold]

                    X_train = np.concatenate(np.array(self.X_list)[train_folds],axis=0)
                    y_train = np.concatenate(np.array(self.y_list)[train_folds],axis=0)

                    # Create dictionary to give appropriate parameters to algorithm
                    pass_param = self.fixed_parameters
                    pass_param.update({param_name:v})

                    algorithm = self.algo(X_train, y_train, **pass_param)

                    # Fit training data
                    algorithm.fit()

                    # Get train and test results
                    test_scores.append(algorithm.score(X_test,y_test))
                    train_scores.append(algorithm.score(X_train, y_train))

                mean_test_score = np.mean(test_scores)
                mean_train_score = np.mean(train_scores)

                # Store all scores
                all_scores[param_name]['train'][v] = mean_train_score
                all_scores[param_name]['test'][v] = mean_test_score

                # Check for best score
                if mean_test_score > best_score:
                    best_score = mean_test_score
                    best_parameters[param_name] = v


        return best_parameters, all_scores

