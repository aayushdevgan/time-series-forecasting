import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf


def collect_bankex_data(banks, start_date, end_date):
    """
    Collects closing price data for the provided banks and dates using Yahoo Finance.
    """
    yf.pdr_override()

    collected_data = []

    for bank_symbol in banks:
        df = pdr.get_data_yahoo(bank_symbol, start=start_date, end=end_date)
        closing_prices = df["Close"].values

        if closing_prices.shape[0] > 3033:
            collected_data.append(closing_prices[3:3035])
        else:
            collected_data.append(closing_prices[0:3032])

    return np.array(collected_data)


def main():
    banks = [
        "AXISBANK.BO", "BANKBARODA.BO", "FEDERALBNK.BO", "HDFCBANK.BO",
        "ICICIBANK.BO", "INDUSINDBK.BO", "KOTAKBANK.BO", "PNB.BO",
        "SBIN.BO", "YESBANK.BO"
    ]

    start_date = '2005-07-12'
    end_date = '2017-11-03'

    bankex_data = collect_bankex_data(banks, start_date, end_date)

    # Save to CSV
    np.savetxt('bank.csv', bankex_data, delimiter=',')

    # Load the saved data
    loaded_data = np.genfromtxt('BANKEX.csv', delimiter=',')

    print(loaded_data.shape)


if __name__ == "__main__":
    main()