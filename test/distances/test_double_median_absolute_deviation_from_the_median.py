from unittest import TestCase
from unittest.mock import Mock, call

from distances.double_median_absolute_deviation_from_the_median import DoubleMedianAbsoluteDeviationFromTheMedian
from distances.sample import Sample


class TestDoubleMedianAbsoluteDeviationFromTheMedian(TestCase):

    def setUp(self):
        self.median_pair_of_statistics_producer = Mock()
        self.mad_repeater = Mock()

    def test_on_should_split_the_sample_into_two_pairs_of_statistics_on_the_median(self):
        # Given
        left_part, right_part = [1, 4, 4, 4, 5, 5, 5, 5], [7, 7, 8, 10, 16, 30]
        skewed_sample = Sample([1, 4, 4, 4, 5, 5, 5, 5, 7, 7, 8, 10, 16, 30])
        self.median_pair_of_statistics_producer.split_on.return_value = (left_part, right_part)

        # When
        DoubleMedianAbsoluteDeviationFromTheMedian(self.median_pair_of_statistics_producer, self.mad_repeater).on(skewed_sample)

        # Then
        self.median_pair_of_statistics_producer.split_on.assert_called_with(skewed_sample)

    def test_on_should_repeat_the_mad_on_each_compound_of_the_pair_of_statistics(self):
        # Given
        left_part, right_part = [1, 4, 4, 4, 5, 5, 5, 5], [7, 7, 8, 10, 16, 30]
        skewed_sample = Sample([1, 4, 4, 4, 5, 5, 5, 5, 7, 7, 8, 10, 16, 30])
        self.median_pair_of_statistics_producer.split_on.return_value = [left_part, right_part]

        # When
        DoubleMedianAbsoluteDeviationFromTheMedian(
            self.median_pair_of_statistics_producer,
            self.mad_repeater
        ).on(skewed_sample)

        # Then
        expected_calls_in_this_order = [call(left_part), call(right_part)]
        self.mad_repeater.repeat_from.assert_has_calls(expected_calls_in_this_order)
