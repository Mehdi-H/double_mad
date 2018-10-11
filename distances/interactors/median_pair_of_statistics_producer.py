import _operator
from typing import Iterable, Union

import numpy as np

from distances.sample import Sample


class MedianPairOfStatisticsProducer():

    def __init__(self):
        pass

    def split_on(self, sample: Sample) -> Iterable[Union[Sample, Sample]]:
        median_of_skewed_sample = float(np.median(sample))

        left_pair = self._subtract_part_of(sample, median_of_skewed_sample, _operator.le)
        right_pair = self._subtract_part_of(sample, median_of_skewed_sample, _operator.gt)

        return left_pair, right_pair

    def _subtract_part_of(self, sample: Sample, threshold: float, comparison_operator: callable) -> Sample:
        elements_are_on_this_side_of_the_threshold = comparison_operator(np.array(sample), threshold)
        return Sample(np.array(sample)[np.where(elements_are_on_this_side_of_the_threshold)])
