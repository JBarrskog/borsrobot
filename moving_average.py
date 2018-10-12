"""A collection of different types of moving averages."""


def simple_moving_average(data, window):
    """Take the Sliding Moving Average of the pandas dataframe."""

    if data.index.is_monotonic_increasing:
        short_rolling = data.rolling(window=window).mean()
    else:
        short_rolling = data.rolling(window=window).mean().shift(-(window-1))

    #data['SMA_{}'.format(window)] = short_rolling

    # return data
    return short_rolling


def exponential_moving_average():
    """Take the Exponential Moving Average of the pandas dataframe."""
    pass


if __name__ == '__main__':
    pass
