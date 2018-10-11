from typing import Iterable

import numpy as np

from distances.sample import Sample


class DoubleMedianAbsoluteDeviationFromTheMedian:
    def __init__(self, median_pair_of_statistics_producer, mad_repeater):
        self.median_pair_of_statistics_producer = median_pair_of_statistics_producer
        self.mad_repeater = mad_repeater

    def on(self, sample: Sample) -> Iterable:
        left_part, right_part = self.median_pair_of_statistics_producer.split_on(sample)
        mad_repeated_on_left_pair = self.mad_repeater.repeat_from(left_part)
        mad_repeated_on_right_pair = self.mad_repeater.repeat_from(right_part)
        return self.median_pair_of_statistics_producer.reassemble(mad_repeated_on_left_pair, mad_repeated_on_right_pair)
