import pandas as pd

# Load the DataFrame from the pickle file
df = pd.read_pickle('df.pkl')

pipe = pd.read_pickle('pipe.pkl')

predicted_prices = pipe.predict(df)