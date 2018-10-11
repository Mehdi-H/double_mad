from unittest import TestCase

from distances.interactors.mad_repeater import MadRepeater
from distances.sample import Sample


class TestMadRepeater(TestCase):

    def test_repeat_from_should_return_a_sample_of_same_length(self):
        # Given
        sample_of_length_3 = Sample([1, 2, 3])

        # When
        mad_repeated_sample = MadRepeater().repeat_from(sample_of_length_3)

        # Then
        self.assertEqual(3, len(mad_repeated_sample))

    def test_repeat_from_should_return_a_sample_with_every_values_the_mad_of_the_array(self):
        # Given
        sample = Sample([1, 2, 3, 3, 4, 4, 4, 5, 5.5, 6, 6, 6.5, 7, 7, 7.5, 8, 9, 12, 52, 90])

        # When
        mad_repeated_sample = MadRepeater().repeat_from(sample)

        # Then
        expected_sample = Sample([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(expected_sample, mad_repeated_sample)
