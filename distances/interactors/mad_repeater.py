from distances.median_absolute_deviation_from_the_median import MedianAbsoluteDeviationFromTheMedian
from distances.sample import Sample


class MadRepeater():
    def __init__(self, median_absolute_deviation_from_the_median=MedianAbsoluteDeviationFromTheMedian()):
        self.median_absolute_deviation_from_the_median = median_absolute_deviation_from_the_median

    def repeat_from(self, sample: Sample) -> Sample:
        mad_of_the_sample = self.median_absolute_deviation_from_the_median.on(sample)
        return Sample([mad_of_the_sample] * len(sample))
