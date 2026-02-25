from sklearn.preprocessing import LabelEncoder
import pandas as pd

def create_features(input_path, output_path):
    df = pd.read_csv(input_path)
    label_encode = LabelEncoder()
    labels = label_encode.fit_transform(df[60])
    df.to_csv(output_path, index=False)
    return df