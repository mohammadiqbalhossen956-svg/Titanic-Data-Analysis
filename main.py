import pandas as pd
import matplotlib.pyplot as plt

# 1. Loading the Data
# Fetching the famous Titanic dataset from a remote CSV source
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# 2. Extracting Top 5 Values (Highest Fares)
# Using nlargest to filter the passengers who paid the highest ticket prices
top_5_fares = df.nlargest(5, 'Fare')

# 3. Data Visualization (Creating the Graph)
plt.bar(top_5_fares['Name'], top_5_fares['Fare'], color='skyblue')
plt.xlabel('Passenger Name')
plt.ylabel('Ticket Fare')
plt.title('Top 5 Highest Fares in Titanic')
plt.xticks(rotation=45, ha='right') # Rotating names for better readability

# 4. Saving the Graph as an Image
plt.tight_layout()
plt.savefig('top_5_fares.png')
print("Graph saved as top_5_fares.png")
plt.show()
