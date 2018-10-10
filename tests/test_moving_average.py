"""Unit tests."""
import unittest
import moving_average


class TestMovingAverage(unittest.TestCase):
    """Testing the moving_average-module."""

    def test_sliding_moving_average(self):
        """Testing the sliding_moving_average-method."""
        self.assertEqual(
            moving_average.sliding_moving_average(), NotImplementedError)


if __name__ == '__main__':
    unittest.main()
