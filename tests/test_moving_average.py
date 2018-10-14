"""Unit tests."""
import unittest

import pandas as pd
import numpy as np

import moving_average


class TestMovingAverage(unittest.TestCase):
    """Testing the moving_average-module."""

    def setUp(self):
        """Set up general settings for the unit tests."""
        # Set a seed for the random-algorithm
        np.random.seed(seed=1337)

    def test_algorithm(self):
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
            {'days': days, 'SMA_3': answer})
        data_frame_ans = data_frame_ans.set_index('days')

        np.testing.assert_array_equal(
            moving_average.simple_moving_average(data_frame, 'col2', 3)[
                'SMA_3'].values, answer)

    def test_algorithm_reversed_date(self):
        """Testing the sliding_moving_average-method with reversed dates."""
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

        np.testing.assert_array_equal(
            moving_average.simple_moving_average(data_frame, 'col2', 3)[
                'SMA_3'].values, answer)

    def test_name_of_new_column(self):
        """Testing that the returned data has the correct header."""
        days = pd.date_range('2018-01-10', '2018-01-19', freq='D')[::-1]
        data = np.random.randint(1, high=100, size=len(days))
        data_frame = pd.DataFrame({'days': days, 'col2': data})
        data_frame = data_frame.set_index('days')

        answer = ['col2']
        for window in range(1, 9):
            data_frame = moving_average.simple_moving_average(
                data_frame, 'col2', window)

            answer.append('SMA_{}'.format(window))

        self.assertEqual(list(data_frame), answer)

        # Testing exceptions
        for tst in [True, [1, 2, 3], 2, 2.0]:
            self.assertRaises(TypeError, moving_average.simple_moving_average,
                              data_frame, tst, 3)
        self.assertRaises(ValueError, moving_average.simple_moving_average,
                          data_frame, "some sting", 3)

    def test_window(self):
        """Testing different kinds of windows."""
        days = pd.date_range('2018-01-10', '2018-01-19', freq='D')[::-1]
        data = np.random.randint(1, high=100, size=len(days))
        data_frame = pd.DataFrame({'days': days, 'col2': data})
        data_frame = data_frame.set_index('days')

        # Different integers
        self.assertRaises(ValueError, moving_average.simple_moving_average,
                          data_frame, 'col2', len(data_frame)+1)
        self.assertRaises(ValueError, moving_average.simple_moving_average,
                          data_frame, 'col2', len(data_frame)+10000)
        self.assertRaises(ValueError, moving_average.simple_moving_average,
                          data_frame, 'col2', 0)
        self.assertRaises(ValueError, moving_average.simple_moving_average,
                          data_frame, 'col2', -1)
        self.assertRaises(ValueError, moving_average.simple_moving_average,
                          data_frame, 'col2', -10000)

        # Float, string, bool, complex, list
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          data_frame, 'col2', 3.)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          data_frame, 'col2', "three")
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          data_frame, 'col2', True)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          data_frame, 'col2', 3+5j)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          data_frame, 'col2', [1, 2, 3])

    def test_data_column(self):
        """Testing different kinds of data_column."""
        days = pd.date_range('2018-01-10', '2018-01-19', freq='D')[::-1]
        data = np.random.randint(1, high=100, size=len(days))
        data_frame = pd.DataFrame({'days': days, 'col2': data})
        data_frame = data_frame.set_index('days')

        # Float, string, bool, complex, list
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          data_frame, 3.)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          data_frame, 'col2', "three")
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          data_frame, 'col2', True)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          data_frame, 'col2', 3+5j)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          data_frame, 'col2', [1, 2, 3])

    def test_data_frame(self):
        """Testing different kinds of data_frame."""
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          np.arange(10), 'col2', 3)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          1, 'col2', 3)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          1.0, 'col2', 3)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          True, 'col2', 3)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          "some string", 'col2', 3)
        self.assertRaises(TypeError, moving_average.simple_moving_average,
                          3+5j, 'col2', 3)


if __name__ == '__main__':
    unittest.main()
