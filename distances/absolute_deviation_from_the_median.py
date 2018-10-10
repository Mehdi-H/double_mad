from typing import Iterable

import numpy as np


class AbsoluteDeviationFromTheMedian:
    def on(self, sample: np.array) -> Iterable:
        return np.abs(sample - np.median(sample))
