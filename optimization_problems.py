import numpy as np


class OptimizationProblem:
    def __init__(self, dimensions, lower_bound, upper_bound):
        self.dimensions = dimensions
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def evaluate(self, position):
        raise NotImplementedError("Subclasses must override evaluate() method")


class AckleyFunction(OptimizationProblem):
    def __init__(self, dimensions, lower_bound=-30, upper_bound=30, a=20, b=0.2, c=2*np.pi):
        super().__init__(dimensions, lower_bound, upper_bound)
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self, position):
        d = len(position)
        sum1 = -self.a * np.exp(-self.b * np.sqrt(np.sum(position**2) / d))
        sum2 = -np.exp(np.sum(np.cos(self.c * position)) / d)
        return sum1 + sum2 + self.a + np.exp(1)
