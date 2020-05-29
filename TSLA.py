# Import Dependencies
import pandas as pd

# Find the csv and import it into a dataframe
f = "TSLA.csv"
data = pd.read_csv(f)

# Create a new dataframe with the columns we want
stocks_df = data[["Date", "Open", "Close"]]

# Add a column to show the change for the day, round it to match the other values
stocks_df["Change"]= round(((stocks_df["Close"]/stocks_df["Open"])-1),6)

# Check to see if it worked
stocks_df.head()

# Export it into a new csv
stocks_df.to_csv("TSLA_Cleaned.csv")