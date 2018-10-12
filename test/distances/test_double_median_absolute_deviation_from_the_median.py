from unittest import TestCase
from unittest.mock import Mock, call

from distances.double_median_absolute_deviation_from_the_median import DoubleMedianAbsoluteDeviationFromTheMedian
from distances.interactors.mad_normalizer import MadNormalizer
from distances.interactors.mad_repeater import MadRepeater
from distances.interactors.median_pair_of_statistics_producer import MedianPairOfStatisticsProducer
from distances.sample import Sample


class TestDoubleMedianAbsoluteDeviationFromTheMedian(TestCase):

    def setUp(self):
        self.median_pair_of_statistics_producer = Mock()
        self.mad_repeater = Mock()
        self.mad_normalizer = Mock()

    def test_on_should_split_the_sample_into_two_pairs_of_statistics_on_the_median(self):
        # Given
        left_part, right_part = [1, 4, 4, 4, 5, 5, 5, 5], [7, 7, 8, 10, 16, 30]
        skewed_sample = Sample([1, 4, 4, 4, 5, 5, 5, 5, 7, 7, 8, 10, 16, 30])
        self.median_pair_of_statistics_producer.split_on.return_value = (left_part, right_part)

        # When
        DoubleMedianAbsoluteDeviationFromTheMedian(self.median_pair_of_statistics_producer, Mock(),
                                                   Mock()).on(skewed_sample)

        # Then
        self.median_pair_of_statistics_producer.split_on.assert_called_with(skewed_sample)

    def test_on_should_repeat_the_mad_on_each_compound_of_the_pair_of_statistics(self):
        # Given
        left_part, right_part = [1, 4, 4, 4, 5, 5, 5, 5], [7, 7, 8, 10, 16, 30]
        skewed_sample = Sample([1, 4, 4, 4, 5, 5, 5, 5, 7, 7, 8, 10, 16, 30])
        self.median_pair_of_statistics_producer.split_on.return_value = [left_part, right_part]

        # When
        DoubleMedianAbsoluteDeviationFromTheMedian(self.median_pair_of_statistics_producer, self.mad_repeater,
                                                   Mock()).on(skewed_sample)

        # Then
        expected_calls_in_this_order = [call(left_part), call(right_part)]
        self.mad_repeater.repeat_from.assert_has_calls(expected_calls_in_this_order)

    def test_mad_repeated_samples_should_be_concatenated_in_exact_order(self):
        # Given
        left_part, right_part = [1, 4, 4, 4, 5, 5, 5, 5], [7, 7, 8, 10, 16, 30]
        left_side_mad, right_side_mad = [1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2]
        skewed_sample = Sample([1, 4, 4, 4, 5, 5, 5, 5, 7, 7, 8, 10, 16, 30])
        self.median_pair_of_statistics_producer.split_on.return_value = [left_part, right_part]
        self.mad_repeater.repeat_from.side_effect = [left_side_mad, right_side_mad]

        # When
        DoubleMedianAbsoluteDeviationFromTheMedian(self.median_pair_of_statistics_producer, self.mad_repeater,
                                                   Mock()).on(skewed_sample)

        # Then
        self.median_pair_of_statistics_producer.reassemble.assert_called_with(
            [1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2]
        )

    def test_absolute_deviation_from_the_median_should_be_normalized_by_two_sided_mad_weights(self):
        # Given
        left_part, right_part = [1, 4, 4, 4, 5, 5, 5, 5], [7, 7, 8, 10, 16, 30]
        left_side_mad, right_side_mad = [1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2]
        skewed_sample = Sample([1, 4, 4, 4, 5, 5, 5, 5, 7, 7, 8, 10, 16, 30])
        self.median_pair_of_statistics_producer.split_on.return_value = [left_part, right_part]
        self.mad_repeater.repeat_from.side_effect = [left_side_mad, right_side_mad]
        self.median_pair_of_statistics_producer.reassemble.return_value = [
            1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

        # When
        DoubleMedianAbsoluteDeviationFromTheMedian(
            self.median_pair_of_statistics_producer,
            self.mad_repeater,
            self.mad_normalizer
        ).on(skewed_sample)

        # Then
        self.mad_normalizer.normalize_with.assert_called_with(
            skewed_sample, [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        )

    def test_double_mad_should_return_the_expected_distances(self):
        # Given
        skewed_sample = Sample([1, 4, 4, 4, 5, 5, 5, 5, 7, 7, 8, 10, 16, 30])

        # When
        processed_distances = DoubleMedianAbsoluteDeviationFromTheMedian(
            MedianPairOfStatisticsProducer(),
            MadRepeater(),
            MadNormalizer()
        ).on(skewed_sample)

        # Then
        expected_distances = Sample([8, 2, 2, 2, 0, 0, 0, 0, 1, 1, 1.5, 2.5, 5.5, 12.5])
        self.assertEqual(expected_distances, processed_distances)
