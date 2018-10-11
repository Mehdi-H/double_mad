from unittest import TestCase
from unittest.mock import Mock

from distances.double_median_absolute_deviation_from_the_median import DoubleMedianAbsoluteDeviationFromTheMedian
from distances.sample import Sample


class TestDoubleMedianAbsoluteDeviationFromTheMedian(TestCase):

    def setUp(self):
        self.median_pair_of_statistics_producer = Mock()

    def test_on_should_split_the_sample_into_two_pairs_of_statistics_on_the_median(self):
        # Given
        left_part, right_part = [1, 4, 4, 4, 5, 5, 5, 5], [7, 7, 8, 10, 16, 30]
        skewed_sample = Sample([1, 4, 4, 4, 5, 5, 5, 5, 7, 7, 8, 10, 16, 30])
        self.median_pair_of_statistics_producer.split_on.return_value = (left_part, right_part)

        # When
        DoubleMedianAbsoluteDeviationFromTheMedian(self.median_pair_of_statistics_producer).on(skewed_sample)

        # Then
        self.median_pair_of_statistics_producer.split_on.assert_called_with(skewed_sample)
