import numpy as np

from distances.absolute_deviation_from_the_median import AbsoluteDeviationFromTheMedian


class MedianAbsoluteDeviationFromTheMedian:

    def __init__(self, absolute_deviation_from_the_median=AbsoluteDeviationFromTheMedian()):
        self.absolute_deviation_from_the_median = absolute_deviation_from_the_median

    def on(self, x: np.array, consistency_constant: float = 1) -> float:
        return consistency_constant * float(np.median(self.absolute_deviation_from_the_median.on(x)))
