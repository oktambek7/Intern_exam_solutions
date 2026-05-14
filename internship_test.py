import random
import pandas as pd
import numpy as np
from itertools import count

# WeatherRecord class
class WeatherRecord:
    def __init__(self, city_name, temperatures, humidity_values, conditions):
        self.city_name = city_name
        self.temperatures = temperatures  # List of 7 temperatures
        self.humidity_values = humidity_values  # List of 7 humidity values
        self.conditions = conditions  # List of 7 conditions

    # Adding methods
    def average_temperature(self):
        return sum(self.temperatures) / len(self.temperatures)

    def highest_temperature(self):
        return max(self.temperatures)

    def lowest_temperature(self):
        return min(self.temperatures)

    def average_humidity(self):
        return sum(self.humidity_values) / len(self.humidity_values)

    # Corrected method to count occurrences of a specific condition
    def count_condition(self, condition_name):
        return self.conditions.count(condition_name)

    def to_dictionary(self):
        return {
            "city_name": self.city_name,
            "avg_temp": round(self.average_temperature(), 2),
            "highest_temp": self.highest_temperature(),
            "lowest_temp": self.lowest_temperature(),
            "avg_humidity": round(self.average_humidity(), 2),
            "conditions": self.conditions
        }

    def display(self):
        print(self.to_dictionary())

# Helper function to generate dummy data for 7 days
def generate_random_data():
    temps = [random.randint(15, 35) for _ in range(7)]
    humidity = [random.randint(40, 90) for _ in range(7)]
    conditions = [random.choice(["Sunny", "Rain", "Cloudy", "Snow"]) for _ in range(7)]
    return temps, humidity, conditions

# Create at least 5 city objects
cities = ["New York", "London", "Tokyo", "Sydney", "Cairo"]
weather_objects = []

for city in cities:
    temps, humidity, conditions = generate_random_data()
    city_record = WeatherRecord(city, temps, humidity, conditions)
    weather_objects.append(city_record)

# Display weekly summary for each city
print("--- Weekly Weather Summary ---")
for record in weather_objects:
    # Option 1: Using the display method
    record.display()

# Optional: View as a pandas DataFrame
print("\n--- Summary DataFrame ---")
data = [r.to_dictionary() for r in weather_objects]
df = pd.DataFrame(data)
print(df[['city_name', 'avg_temp', 'highest_temp', 'lowest_temp', 'avg_humidity']])

max_avg_temp = df.groupby('city_name')['avg_temp'].max().sort_values(ascending=False).index[0]
print('City with max avg temp: ', max_avg_temp)

lowest_avg_temp = df.groupby('city_name')['avg_temp'].min().sort_values(ascending=True).index[0]
print('City with min avg temp: ', lowest_avg_temp)

high_humidity_df = df[df['avg_humidity'] > 70]

print("\n--- High Humidity Cities (> 70) ---")
print(high_humidity_df[['city_name', 'avg_humidity' ]])

for record in weather_objects:
    print(f"\n--- {record.city_name} Weather Report ---")
    print(f"Rainy days: {record.count_condition('Rain')}")
    print(f"Sunny days: {record.count_condition('Sunny')}")
    print(f"Cloudy days: {record.count_condition('Cloudy')}")
    print(f"Windy days: {record.count_condition('Windy')}")

avg_temp = city_record.average_temperature()

if avg_temp >= 30:
    classification = "Hot Week"
elif avg_temp >= 20:
    classification = "Warm Week"
else:
    classification = "Cool Week"

print(f"{city_record.city_name}: {classification} (Avg Temp: {avg_temp:.1f}°C)")