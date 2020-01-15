"""
Define a class named slope-intercept which can be constructed by the slope (m) and the intercept (b) in y = m(x) + b. 
"""

class Slope_Intercept:
    def __init__ (self, m, b):
        self.slope = m
        self.intercept = b
    def a straight line (self):
        """
        be a able to plot a line with the slope-intercept equation.
        """
        return self.slope * (x) + self.intercept

ySlope_Intercept = Slope_Intercept(1,-5)
print(ySlope_Intercept.line())
