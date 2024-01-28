import numpy as np


def mean(values):
    return sum(values) / len(values)


def covariance(x, y, mean_x, mean_y):
    covar = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(len(x)))
    return covar


def variance(values, mean_value):
    return sum((x - mean_value) ** 2 for x in values)


def pearson_correlation(x, y):
    mean_x, mean_y = mean(x), mean(y)
    covar = covariance(x, y, mean_x, mean_y)
    var_x, var_y = variance(x, mean_x), variance(y, mean_y)
    corr = covar / (np.sqrt(var_x) * np.sqrt(var_y))
    return corr


# Пример использования
array1 = np.random.rand(100)
array2 = np.random.rand(100)

correlation = pearson_correlation(array1, array2)
print("Корреляция Пирсона:", correlation)

