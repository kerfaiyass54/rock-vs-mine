import joblib
import numpy as np
import yaml
from pipeline.config import CONFIG_PATH

def run_inference():
    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)
    model_path = config["models"]["path"]
    model = joblib.load(model_path)
    input_data = (0.0260,0.0363,0.0136,0.0272,0.0214,0.0338,0.0655,0.1400,0.1843,0.2354,0.2720,0.2442,0.1665,0.0336,0.1302,0.1708,0.2177,0.3175,0.3714,0.4552,0.5700,0.7397,0.8062,0.8837,0.9432,1.0000,0.9375,0.7603,0.7123,0.8358,0.7622,0.4567,0.1715,0.1549,0.1641,0.1869,0.2655,0.1713,0.0959,0.0768,0.0847,0.2076,0.2505,0.1862,0.1439,0.1470,0.0991,0.0041,0.0154,0.0116,0.0181,0.0146,0.0129,0.0047,0.0039,0.0061,0.0040,0.0036,0.0061,0.0115)
    data_array = np.asarray(input_data)
    data_reshaped = data_array.reshape(1,-1)
    prediction = model.predict(data_reshaped)
    print(prediction)