"""Reading data from different sources."""
import pandas as pd
import matplotlib.pyplot as plt

import visualise


def read_xls(path):
    """Create a pandas data_frame of the xls at path."""
    data_frame = pd.read_excel(path, index_col=0)

    return data_frame


if __name__ == "__main__":
    PATH = r'./test_data.xls'
    data_frame = read_xls(PATH)

    h1 = visualise.plot_line(data_frame, data_column='Closeprice')
    plt.show()
