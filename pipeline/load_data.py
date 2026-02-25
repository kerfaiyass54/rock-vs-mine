import pandas as pd


def load_dataset(path):
    df = df = pd.read_csv(path)
    X = df.drop(columns=60, axis=1)
    Y = df[60]
    return X, Y