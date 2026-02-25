import pandas as pd
import os


def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path, header=None)

    # simple cleaning
    df = df.dropna()

    df.to_csv(output_path, index=False)
    return df