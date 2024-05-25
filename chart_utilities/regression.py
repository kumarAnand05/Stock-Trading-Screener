import numpy as np
from sklearn.linear_model import LinearRegression


def linear_regression(data):
    """
    Performs linear regression of passed data and returns the regression model object
    """

    regressor = LinearRegression()
    data = data.to_numpy()      # Converting data to numpy array

    x = np.arange(len(data)).reshape((-1, 1))       # Independent variable
    y = data.reshape((-1, 1))       # Dependant variable

    # Model fitting
    regressor.fit(x, y)
    return regressor


def regression_slope(regressor_obj):
    """
    returns the slope of the regression line to analyze the trend of the price data points
    """

    slope = regressor_obj.coef_[0][0]
    return round(slope, 2)


def regression_intercept(regressor_obj):
    """
    returns the intercept of the regression line to analyze the trend of the price data points
    """

    intercept = regressor_obj.intercept_[0]
    return round(intercept, 2)
