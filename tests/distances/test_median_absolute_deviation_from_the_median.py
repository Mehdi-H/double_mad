from unittest import TestCase
from unittest.mock import Mock

from distances.absolute_deviation_from_the_median import AbsoluteDeviationFromTheMedian
from distances.median_absolute_deviation_from_the_median import MedianAbsoluteDeviationFromTheMedian as mad


class TestIntMedianAbsoluteDeviationFromTheMedian(TestCase):

    def test_on_should_calculate_the_median_of_absolute_deviations(self):
        # Given
        sample = [1, 2, 3, 3, 4, 4, 4, 5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 9, 12, 52, 90]
        mock_absolute_deviation_from_the_median = Mock()
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
        absolute_deviation_from_the_median = AbsoluteDeviationFromTheMedian()
        sample = [1, 2, 3, 3, 4, 4, 4, 5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 9, 12, 52, 90]

        # When
        computed_mad = mad(absolute_deviation_from_the_median).on(sample)

        # Then
        self.assertEqual(2, computed_mad)
