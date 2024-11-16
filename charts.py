import pandas as pd
import matplotlib.pyplot as plt

# Loading the CSV file
file_path = 'data/final.csv'  # replace with the path to your file
data = pd.read_csv(file_path)

# Counting the number of people by countries and cities
country_counts = data['code'].value_counts()
city_counts = data['city'].value_counts()

# Plotting a bar chart for the number of people by countries
plt.figure(figsize=(10, 6))
country_counts.plot(kind='bar')
plt.title('Number of People by Countries')
plt.xlabel('Country Code')
plt.ylabel('Number of People')
plt.xticks(rotation=45)
plt.show()

# Plotting a bar chart for the number of people by cities (top 20)
plt.figure(figsize=(12, 6))
city_counts.head(20).plot(kind='bar')  # Displaying top 20 cities
plt.title('Number of People by Cities (Top 20)')
plt.xlabel('City')
plt.ylabel('Number of People')
plt.xticks(rotation=75)
plt.show()
