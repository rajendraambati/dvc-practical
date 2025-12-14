import pandas as pd
import os


data={
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["New York", "Los Angeles", "Chicago"]
}

data=pd.DataFrame(data)
file_path = os.path.join("data", "people.csv")
os.makedirs("data", exist_ok=True)
data.to_csv(file_path, index=False)
print(f"Data saved to {file_path}")