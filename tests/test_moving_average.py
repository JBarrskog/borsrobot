"""Unit tests."""
import unittest

import pandas as pd
import numpy as np

import moving_average


class TestMovingAverage(unittest.TestCase):
    """Testing the moving_average-module."""

    def setUp(self):
        """Setting up general settings for the unit tests."""
        # Set a seed for the random-algorithm
        np.random.seed(seed=1337)

    def test_simple_moving_average_3_units(self):
        """Testing the sliding_moving_average-method."""
        days = pd.date_range('2018-01-10', '2018-01-19', freq='D')

        data = np.random.randint(1, high=100, size=len(days))
        data_frame = pd.DataFrame({'days': days, 'col2': data})
        data_frame = data_frame.set_index('days')

        answer = np.array([np.nan,
                           np.nan,
                           59+2/3,
                           65,
                           74+1/3,
                           56+2/3,
                           73+2/3,
                           71+1/3,
                           86+1/3,
                           80+1/3])

        data_frame_ans = pd.DataFrame(
            {'days': days, 'col2': answer})
        data_frame_ans = data_frame_ans.set_index('days')

        pd.testing.assert_frame_equal(
            moving_average.simple_moving_average(data_frame, 3), data_frame_ans)

    def test_simple_moving_average_3_units_reversed_date(self):
        """Testing the sliding_moving_average-method."""
        days = pd.date_range('2018-01-10', '2018-01-19', freq='D')[::-1]
        data = np.random.randint(1, high=100, size=len(days))
        data_frame = pd.DataFrame({'days': days, 'col2': data})
        data_frame = data_frame.set_index('days')

        answer = np.array([59+2/3,
                           65,
                           74+1/3,
                           56+2/3,
                           73+2/3,
                           71+1/3,
                           86+1/3,
                           80+1/3,
                           np.nan,
                           np.nan])

        data_frame_ans = pd.DataFrame(
            {'days': days, 'col2': answer})
        data_frame_ans = data_frame_ans.set_index('days')
        print(moving_average.simple_moving_average(data_frame, 3))
        pd.testing.assert_frame_equal(
            moving_average.simple_moving_average(data_frame, 3), data_frame_ans)


if __name__ == '__main__':
    unittest.main()
