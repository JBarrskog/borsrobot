"""A collection of different types of moving averages."""
import pandas as pd


def simple_moving_average(data_frame, data_column, window):
    """Take the Simple Moving Average of the pandas dataframe."""
    # Checking data_frame
    if not isinstance(data_frame, pd.DataFrame):
        raise TypeError("The data_frame has to be a pandas.DataFrame.")

    # Checking column
    if not isinstance(data_column, (str)):
        raise TypeError("The data_column must be a string.")
    elif data_column not in data_frame.columns:
        raise ValueError("The data_column does not exist in the data frame.")

    # Checking window
    if isinstance(window, (bool)) or not isinstance(window, (int)):
        raise TypeError("The window must be an integer greater than zero.")
    elif window < 1 or window > len(data_frame):
        raise ValueError('The window={} has to be between 1 and len(df).'
                         .format(window))

    if data_frame.index.is_monotonic_increasing:
        simple_rolling = data_frame[data_column].rolling(window=window).mean()
    else:
        simple_rolling = data_frame[data_column].rolling(
            window=window).mean().shift(-(window-1))

    data_frame['SMA_{}'.format(window)] = simple_rolling

    return data_frame


def exponential_moving_average():
    """Take the Exponential Moving Average of the pandas dataframe."""
    raise NotImplementedError


if __name__ == '__main__':
    pass
