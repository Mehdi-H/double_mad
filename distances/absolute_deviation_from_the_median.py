from typing import Iterable

import numpy as np

from distances.sample import Sample


class AbsoluteDeviationFromTheMedian:
    def on(self, sample: Sample) -> Iterable:
        return np.abs(sample - np.median(sample))
