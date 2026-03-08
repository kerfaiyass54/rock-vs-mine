from pipeline.config import CONFIG_PATH
from pipeline.explore_data import explore_data
from pipeline.features_pipeline import create_features
from pipeline.load_data import load_dataset
from pipeline.preprocessing_pipeline import preprocess_data
from pipeline.training_pipeline import train_model
import yaml

with open(CONFIG_PATH, "r") as file:
    config = yaml.safe_load(file)

raw_path = config["data"]["row_path"]   # <- use row_path (your yaml key)
preprocessed_path = config["data"]["preprocessed_path"]
features_path = config["data"]["features_path"]

df = preprocess_data(raw_path, preprocessed_path)
df = create_features(preprocessed_path, features_path)

explore_data(features_path)

X, Y = load_dataset(features_path)

train_model(X, Y)