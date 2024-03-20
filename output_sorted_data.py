from log import MY_API_KEY   # COMMENT THIS LINE ONCE YOU HAVE YOUR API KEY
import requests
import pandas as pd
import matplotlib.pyplot as plt
import json

#MY_API_KEY = "<ENTER HERE WITHIN QUOTES>"   UNCOMMENT THIS LINE AND ADD API KEY WITHIN QUOTES
url = "https://api.climatiq.io/data/v1/estimate"

authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}    # USE AMERICAN SPELLING w/Z

activity_ids = {
    "light": "passenger_vehicle-vehicle_type_car-fuel_source_petrol-engine_size_na-vehicle_age_na-vehicle_weight_na",
    "mid_range": "passenger_vehicle-vehicle_type_upper_medium_car-fuel_source_petrol-engine_size_na-vehicle_age_na-vehicle_weight_na",
    "heavy_duty": "commercial_vehicle-vehicle_type_truck_medium_or_heavy-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
}

def estimate_emissions(vehicle_type, activity_id, distance, distance_unit="mi"):
    distance_miles = distance  

    json_body = {
        "emission_factor": {
            "activity_id": activity_id,
            "data_version": "^10",
        },
        "parameters": {
            "distance": distance_miles,
            "distance_unit": distance_unit,
        }
    }

    response = requests.post(url, json=json_body, headers=authorization_headers)       # AMERICAN SPELLING
    if response.status_code == 200:
        result = response.json()
        return {
            "Vehicle Type": vehicle_type,
            "Distance (miles)": distance_miles,
            "CO2 Emissions (kg)": result['co2e']
        }
    else:
        return {
            "Vehicle Type": vehicle_type,
            "Error": response.text
        }

results = []
for vehicle_type, activity_id in activity_ids.items():
    result = estimate_emissions(vehicle_type, activity_id, 16, "mi")
    if "CO2 Emissions (kg)" in result:  
        results.append(result)

df = pd.DataFrame(results)

print(df)

plt.figure(figsize=(10, 6))
plt.bar(df['Vehicle Type'], df['CO2 Emissions (kg)'], color='blue')      # AMERICAN SPELLING colour, color
plt.xlabel('Vehicle Type')
plt.ylabel('CO2 Emissions (kg)')
plt.title('CO2 Emissions by Vehicle Type over 16 Miles')
plt.show()