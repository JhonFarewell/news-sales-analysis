import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("news_data.csv") 

# 2. Create a bar chart of news sold per month
plt.figure(figsize=(10, 6))
plt.bar(df["month"], df["news_sold"], color='skyblue')
plt.title("News Sold per Month")
plt.xlabel("Month")
plt.ylabel("Number of News Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. Add a column for month-to-month percentage change
df["percentage_change"] = df["news_sold"].pct_change() * 100

# 4. Filter and display months where news_sold < 2000
filtered_df = df[df["news_sold"] < 2000]
print("Months with sales < 2000:")
print(filtered_df)

# 5. Group months into quarters and calculate total sales
# Convert month names to datetime to get quarters
df["quarter"] = pd.to_datetime(df["month"], format="%B").dt.to_period("Q")
quarterly_sales = df.groupby("quarter")["news_sold"].sum()
print("\nQuarterly Sales:")
print(quarterly_sales)

# 6. Save months with above-average news sold into a new CSV file
average_sales = df["news_sold"].mean()
above_avg_df = df[df["news_sold"] > average_sales]
above_avg_df.to_csv("above_average_news.csv", index=False)

print("\nAbove-average sales months saved to 'above_average_news.csv'")
