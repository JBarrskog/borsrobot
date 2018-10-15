"""Unit tests of the visualise-module."""
import unittest

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import visualise


# @patch('visualise.plt')
class TestPlotLine(unittest.TestCase):
    """Testing the plot_line method."""

    def setUp(self):
        """Set up general settings for the unit tests."""
        # Set a seed for the random-algorithm
        np.random.seed(seed=1337)

        days = pd.date_range('2018-01-01', '2018-12-31', freq='D')
        data = np.random.randint(1, high=100, size=len(days))
        data2 = np.random.randint(2, high=100, size=len(days))
        data_frame = pd.DataFrame({'days': days, 'col2': data, 'col3': data2})
        self.data_frame = data_frame.set_index('days')

    def test_data_frame(self):
        """Test different types in data_frame."""
        self.assertRaises(TypeError, visualise.plot_line,
                          1, data_column='col2')
        self.assertRaises(TypeError, visualise.plot_line,
                          np.arange(10), data_column='col2')

    def test_data_column(self):
        """Test different types in data_column."""
        # Testing non-existing data_column
        self.assertRaises(ValueError, visualise.plot_line,
                          self.data_frame, data_column='some string')

        # Testing other data types
        self.assertRaises(TypeError, visualise.plot_line,
                          self.data_frame, data_column=1)
        self.assertRaises(TypeError, visualise.plot_line,
                          self.data_frame, data_column=2.0)
        self.assertRaises(TypeError, visualise.plot_line,
                          self.data_frame, data_column=3+2j)
        self.assertRaises(TypeError, visualise.plot_line,
                          self.data_frame, data_column=True)
        self.assertRaises(TypeError, visualise.plot_line,
                          self.data_frame, data_column=None)

    def test_handles(self):
        """Testing handling of plot (axes) handles."""
        self.assertTrue(isinstance(visualise.plot_line(
            self.data_frame, data_column='col2'), (plt.Subplot)))

        # Testing other ax_handle
        self.assertRaises(TypeError,
                          visualise.plot_line, self.data_frame,
                          data_column='col2', ax_handle="some string")
        self.assertRaises(TypeError,
                          visualise.plot_line, self.data_frame,
                          data_column='col2', ax_handle="some string")
