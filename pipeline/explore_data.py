import pandas as pd
import os


def explore_data(input_path):
    df = pd.read_csv(input_path, header=None)
    print(df.head())
    print(df.describe())
    print(df.info())
    print(df.shape)
    print(df[60].value_counts())