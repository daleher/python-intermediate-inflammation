"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2]),
    ])
def test_daily_min(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [5, 6]),
    ])
def test_daily_max(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]])
    ])
def test_patient_normalise(test, expected):
    """Test normalisation works for arrays of one and positive integers.
       Assumption that test accuracy of two decimal places is sufficient."""
    from inflammation.models import patient_normalise
    npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[3, 5], [5, 3], [0.15, 0.05], [0.05, 0.01]], [[3, 5], [5, 3], [0.15, 0.05], [0.05, 0.01]])
    ])
def test_random_numpy(test, expected):
    """Test normalisation works for arrays of one and positive integers.
       Assumption that test accuracy of two decimal places is sufficient."""
    from inflammation.models import patient_normalise
    npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)


def test_random_numpy():
    mean = 5
    sdev = 3
    sample_size = 1000000

    sample = np.random.normal(mean, sdev, sample_size)

    np.testing.assert_almost_equal(mean, np.mean(sample), decimal=2)
    np.testing.assert_almost_equal(sdev, np.std(sample), decimal=2)


