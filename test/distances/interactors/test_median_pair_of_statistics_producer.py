from unittest import TestCase

from distances.interactors.median_pair_of_statistics_producer import MedianPairOfStatisticsProducer
from distances.sample import Sample

from numpy.testing import assert_array_equal


class TestMedianPairOfStatisticsProducer(TestCase):

    def test_split_on_should_return_two_parts_of_an_array(self):
        # Given
        skewed_sample = Sample([1, 4, 4, 4, 5, 5, 5, 5, 7, 7, 8, 10, 16, 30])

        # When
        left_part, right_part = MedianPairOfStatisticsProducer().split_on(skewed_sample)

        # Then
        assert_array_equal(Sample([1, 4, 4, 4, 5, 5, 5, 5]), left_part)
        assert_array_equal(Sample([7, 7, 8, 10, 16, 30]), right_part)
