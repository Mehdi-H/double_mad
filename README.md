Double Mad
==========

A Python implementation of the double mad (median absolute deviation from the median), this eurekastatistics post: https://eurekastatistics.com/using-the-median-absolute-deviation-to-find-outliers/, originally coded in R.

The structure of the code is meant to be "use case"-oriented, with a tolerated adherence to numpy.

This implementation is the result of a "data-science" kata, in this state it's really packaged to be used in an application.

## Getting started

Setup a virutalenv and download dependencies.

```bash
$virtualenv double_mad_env
$source ./double_mad_env/bin/activate
$pip install -r requirements.txt
```

You can now launch the tests

```bash
$python -m unittest
```