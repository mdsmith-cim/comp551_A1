import numpy as np

def split(data, train_test_ratio = 0.7):

    train_ratio = train_test_ratio
    test_ratio = 1 - train_test_ratio

    np.random.shuffle(data)

    num_values = data.shape[0]

    train_amt = int(num_values * train_ratio)
    test_amt = int(num_values * test_ratio)

    X_train = data[:train_amt,:-1]
    X_test = data[train_amt:train_amt + test_amt, :-1]
    # Make sure y data has proper dimension
    y_train = data[:train_amt,-1].reshape((-1,1))
    y_test = data[train_amt:train_amt + test_amt, -1].reshape((-1,1))

    return X_train, X_test, y_train, y_test

