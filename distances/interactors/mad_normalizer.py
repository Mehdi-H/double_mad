from typing import List

from distances.absolute_deviation_from_the_median import AbsoluteDeviationFromTheMedian
from distances.sample import Sample


class MadNormalizer:

    def __init__(self, absolute_deviation_from_the_median=AbsoluteDeviationFromTheMedian()):
        self.absolute_deviation_from_the_median = absolute_deviation_from_the_median

    def normalize_with(self, sample_to_normalize: Sample, weights: List) -> Sample:
        return Sample([s / w for s, w in zip(self.absolute_deviation_from_the_median.on(sample_to_normalize), weights)])
