"""
Define a class named slope-intercept which can be constructed by the slope (m) and the intercept (b) in y = m(x) + b. 
"""

class Slope_Intercept:
    def __init__ (self, m, x, b):
        self.slope = m
        self.intercept = b
        self.x_intercept = x
    def a straight line (self):
        """
        be a able to plot a line with the slope-intercept equation.
        """
        return self.slope * self.x_intercept + self.intercept

ySlope_Intercept = Slope_Intercept(1, 2, -5)
print(ySlope_Intercept.line())
