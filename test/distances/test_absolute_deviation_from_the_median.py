from unittest import TestCase

from numpy.testing import assert_array_equal

from distances.absolute_deviation_from_the_median import AbsoluteDeviationFromTheMedian
from distances.sample import Sample


class TestAbsoluteDeviationFromTheMedian(TestCase):

    def test_on_should_calculate_the_absolute_distance_from_center_in_terms_of_the_mad(self):
        # Given
        absolute_deviation_from_the_median = AbsoluteDeviationFromTheMedian()
        sample_with_a_median_of_6 = Sample([1, 2, 3, 3, 4, 4, 4, 5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 9, 12, 52, 90])

        # When
        distances_from_the_centre = absolute_deviation_from_the_median.on(sample_with_a_median_of_6)

        # Then
        expected_distances = Sample(
            [5.0, 4.0, 3.0, 3.0, 2.0, 2.0, 2.0, 1.0, 0.5, 0.0, 0.0, 0.5, 1.0, 1.0, 1.5, 2.0, 3.0, 6.0,
             46.0, 84.0])
        assert_array_equal(expected_distances, distances_from_the_centre)
