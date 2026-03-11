import pandas as pd
import os


data = {"Name":["Aditya", "Kashish", "Didii"],
      "Age":[23, 18, 18],
      "Mobile":["RealME", "Xiomi", "Oppo"]}

#v1


df = pd.DataFrame(data)


new_row = {"Name":"ABC", "Age":"20", "Mobile":"HTC"}
df.loc[len(df.index)]=new_row

new_row2 = {"Name":"AAA", "Age":"21", "Mobile":"Nokia"}
df.loc[len(df.index)]=new_row2


data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

filepath = os.path.join(data_dir, "sample_data.csv")

df.to_csv(filepath, index=False)