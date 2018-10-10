from math import sqrt
from unittest import TestCase, skip
from unittest.mock import Mock

import numpy as np

from distances.absolute_deviation_from_the_median import AbsoluteDeviationFromTheMedian
from distances.median_absolute_deviation_from_the_median import MedianAbsoluteDeviationFromTheMedian as mad


class TestIntMedianAbsoluteDeviationFromTheMedian(TestCase):

    def test_on_should_calculate_the_median_of_absolute_deviations(self):
        # Given
        sample = [1, 2, 3, 3, 4, 4, 4, 5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 9, 12, 52, 90]
        mock_absolute_deviation_from_the_median = Mock(spec=AbsoluteDeviationFromTheMedian)
        distances_from_the_centre = [5.0, 4.0, 3.0, 3.0, 2.0, 2.0, 2.0, 1.0, 0.5, 0.0, 0.0, 0.5, 1.0, 1.0, 1.5, 2.0,
                                     3.0, 6.0, 46.0, 84.0]
        mock_absolute_deviation_from_the_median.on.return_value = distances_from_the_centre

        # When
        computed_mad = mad(mock_absolute_deviation_from_the_median).on(sample)

        # Then
        self.assertEqual(2, computed_mad)


class TestMedianAbsoluteDeviationFromTheMedian(TestCase):

    def test_on_should_calculate_the_median_of_absolute_deviations(self):
        # Given
        sample = [1, 2, 3, 3, 4, 4, 4, 5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 9, 12, 52, 90]

        # When
        computed_mad = mad().on(sample)

        # Then
        self.assertEqual(2, computed_mad)

    def test_on_should_allow_a_consistency_constant(self):
        # Given
        sample = [1, 2, 3, 3, 4, 4, 4, 5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 9, 12, 52, 90]

        # When
        consistency_constant_for_normal_distribution = 1.4826
        distance = mad().on(sample, consistency_constant_for_normal_distribution)

        # Then
        self.assertEqual(2.9652, distance)

    def test_on_should_return_0_when_more_than_50_percent_of_the_values_are_identical(self):
        # Given
        sample_with_more_than_fifty_percent_of_identical_values = [0, 1, 1, 1, 1, 1, 1, 1, 0]

        # When
        distance = mad().on(sample_with_more_than_fifty_percent_of_identical_values)

        # Then
        self.assertEqual(0, distance)

    @skip
    def test_the_consistency_constant_can_make_the_mad_an_estimator_of_the_standard_deviation(self):
        """
            This test is skippable as it contains a random component,
            but I thought it could be useful to document this property through a test
        """
        # Given
        uniform_distribution_sample = np.random.uniform(80, 90, 1000)

        # When
        consistency_constant = 2 / sqrt(3)
        distance = mad().on(uniform_distribution_sample, consistency_constant)

        # Then
        observed_delta_while_testing = 0.2
        self.assertAlmostEqual(np.std(uniform_distribution_sample), distance, delta=observed_delta_while_testing)
