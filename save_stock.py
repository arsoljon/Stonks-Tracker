import pandas as pd
import os

class Save_stock():
    __stock_info = {}
    def __set_stock_info(self):
        df = pd.read_csv("databases/clean_stock_db", sep=',', dtype=str).to_dict()
        self.__stock_info = {"Ticker": [df["Ticker"][0]], "Current_price": [df["Current_price"][0]]}
    def __get_stock_info(self): return self.__stock_info

    def __init__(self):
        self.__set_stock_info()
        df = pd.DataFrame(self.__get_stock_info(), columns=["Ticker", "Current_price"])
        path = "databases/all_stock_db"
        if os.path.isfile(path):
            df.to_csv(path, sep=',', mode='a', header=False)
        else:
            df.to_csv(path, sep=',')