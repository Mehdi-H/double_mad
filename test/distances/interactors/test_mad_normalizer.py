from unittest import TestCase

from distances.absolute_deviation_from_the_median import AbsoluteDeviationFromTheMedian
from distances.interactors.mad_normalizer import MadNormalizer
from distances.sample import Sample


class TestMadNormalizer(TestCase):

    def test_normalize_should_divide_each_sample_element_with_provided_weights(self):
        # Given
        sample = Sample([2, 4, 6, 8])
        weights = Sample([2, 2, 2, 2])
        object_that_implements_on_method = type('identity', (object,), {'on': (lambda x: x)})

        # When
        normalized_sample = MadNormalizer(object_that_implements_on_method).normalize_with(sample, weights)

        # Then
        self.assertEqual(Sample([1, 2, 3, 4]), normalized_sample)

    def test_mad_normalization_should_divide_each_sample_element_with_absolute_deviation_from_the_median(self):
        # Given
        sample = Sample([2, 4, 6, 8])
        weights = Sample([2, 2, 2, 2])
        absolute_deviation_from_the_median_implementation = AbsoluteDeviationFromTheMedian()

        # When
        normalized_sample = MadNormalizer(absolute_deviation_from_the_median_implementation).normalize_with(sample,
                                                                                                            weights)
        # Then
        self.assertEqual([1.5, 0.5, 0.5, 1.5], normalized_sample)
