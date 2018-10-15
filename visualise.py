"""Visualising stock history-data."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_line(data_frame, data_column, ax_handle=None):
    """Create a line plot from the pandas data_frame."""
    # Check the data_frame
    if not isinstance(data_frame, pd.DataFrame):
        raise TypeError("The data_frame has to be a pandas.DataFrame.")

    # Checking column
    if not isinstance(data_column, (str)):
        raise TypeError("The data_column must be a string.")
    elif data_column not in data_frame.columns:
        raise ValueError("The data_column does not exist in the data frame.")

    # Checking index
    if not isinstance(data_frame.index, pd.DatetimeIndex):
        raise TypeError(
            "The index of the data frame must be pandas.DatetimeIndex.")

    # Checking plot-handle
    if not ax_handle:
        ax_handle = plt.subplot(1, 1, 1)
    elif not isinstance(ax_handle, plt.Subplot):
        raise TypeError("The ax_handle must be a plt.Subplot (axes-handle).")

    ax_handle.plot(data_frame[data_column])

    return ax_handle


if __name__ == "__main__":
    pass
