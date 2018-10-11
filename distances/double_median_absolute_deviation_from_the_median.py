from typing import Iterable

import numpy as np


class DoubleMedianAbsoluteDeviationFromTheMedian:
    def __init__(self, median_pair_of_statistics_producer):
        self.median_pair_of_statistics_producer = median_pair_of_statistics_producer

    def on(self, sample: np.array) -> Iterable:
        return self.median_pair_of_statistics_producer.split_on(sample)
