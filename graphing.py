import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def graph(csv_file):

    dataframe = pd.read_csv(csv_file)

    x = dataframe.Date_HPSC
    y = dataframe.Test24
    z = dataframe.pool_test

    plt.ylabel('Number Of Cases Tested')
    plt.xlabel('Dates of Tests')
    plt.plot(x,y,z)
    plt.show()





graph('pool_test.csv')
