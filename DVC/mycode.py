import pandas as pd
import os


data = {"Name":["Aditya", "Kashish", "Didii"],
      "Age":[23, 18, 18],
      "Mobile":["RealME", "Xiomi", "Oppo"]}

df = pd.DataFrame(data)

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

filepath = os.path.join(data_dir, "sample_data.csv")

df.to_csv(filepath, index=False)