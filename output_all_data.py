from log import MY_API_KEY      # COMMENT THIS LINE ONCE YOU HAVE YOUR API KEY
import requests
import json

#MY_API_KEY = "<ENTER HERE WITHIN QUOTES>"   UNCOMMENT THIS LINE AND ADD API KEY WITHIN QUOTES
url = "https://api.climatiq.io/data/v1/estimate"

authorization_headers = {"Authorization": f"Bearer: {MY_API_KEY}"}

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

    response = requests.post(url, json=json_body, headers=authorization_headers)
    if response.status_code == 200:
        result = response.json()
        print(f"Vehicle Type: {vehicle_type}, Distance: {distance_miles} miles, CO2 Emissions: {result['co2e']} kg", json.dumps(result, indent=5))
    else:
        print(f"Failed to calculate CO2 emissions for {vehicle_type}. Error: {response.text}")

# https://www.climatiq.io/data/explorer?sector=Transport&unit_type=Distance&data_version=10.10
activity_ids = {
    "light": "passenger_vehicle-vehicle_type_car-fuel_source_petrol-engine_size_na-vehicle_age_na-vehicle_weight_na",
    "mid_range": "passenger_vehicle-vehicle_type_upper_medium_car-fuel_source_petrol-engine_size_na-vehicle_age_na-vehicle_weight_na",
    "heavy_duty": "commercial_vehicle-vehicle_type_truck_medium_or_heavy-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
}

for vehicle_type, activity_id in activity_ids.items():
    print(f"Estimating emissions for {vehicle_type} vehicle over 16 miles:")
    estimate_emissions(vehicle_type, activity_id, 16, "mi")
