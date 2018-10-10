import numpy as np


class MedianAbsoluteDeviationFromTheMedian:

    def __init__(self, absolute_deviation_from_the_median):
        self.absolute_deviation_from_the_median = absolute_deviation_from_the_median

    def on(self, x: np.array) -> float:
        return float(np.median(self.absolute_deviation_from_the_median.on(x)))
