from chart_utilities import regression


def check_crossover(data1, data2, trading_sessions):
    """
    Checks whether there is a crossover between two data within the specified duration.
    returns:
                -1 if data1 intersects the data2 from upside i.e. data1 decreasing and data2 increasing
                0 if data 1 does not intersect data2
                1 if data1 intersects the data2 from downside i.e. data1 increasing and data2 decreasing
    """

    trading_sessions = min(len(data1), len(data2), trading_sessions)  # To process minimum available trading sessions

    # Trimming data to equal dimensions
    data1 = data1[:trading_sessions][::-1]
    data2 = data2[:trading_sessions][::-1]

    data1_reg = regression.linear_regression(data1)
    data2_reg = regression.linear_regression(data2)

    slope1 = regression.regression_slope(data1_reg)
    slope2 = regression.regression_slope(data2_reg)
    intercept1 = regression.regression_intercept(data1_reg)
    intercept2 = regression.regression_intercept(data2_reg)

    """
        # Intersection check

        1. When two different lines are parallel:
            Slope is equal and intercept should be different 

        2. When two different lines intersect:
            say the two lines are y1 = m1x1+c1
                                  y2 = m2x2+c2
            at intersection y and x will be equal for both lines. At that point we can re-write the equation as:
                m1x+c1 = m2x+c2
                So x = (c2-c1)/(m1-m2)
    """

    if slope1 == slope2 and intercept1 != intercept2:  # When lines are parallel
        return 0

    else:  # When lines are intersecting
        x_intersection = (intercept2 - intercept1) / (slope1 - slope2)

        sample_x = x_intersection - 1e-5                # sample value of x
        sample_y1 = slope1 * sample_x + intercept1      # Corresponding y value for sample x on line 1
        sample_y2 = slope2 * sample_x + intercept2      # Corresponding y value for sample x on line 2

        if 0 <= x_intersection <= trading_sessions-1:
            if sample_y1 > sample_y2:       # Regression Line of data1 intersects the line 2 from upside
                return -1
            else:
                return 1

    return 0
