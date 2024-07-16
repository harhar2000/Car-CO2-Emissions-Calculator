from dotenv import load_dotenv
import os
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

load_dotenv()
MY_API_KEY = os.getenv("MY_API_KEY")

url = "https://api.climatiq.io/data/v1/estimate"
authorization_headers = {"Authorization": f"Bearer {MY_API_KEY}"}

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

    response = requests.post(url, json=json_body, headers=authorization_headers)
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

st.set_page_config(page_title="CO2 Emissions Calculator", layout="centered")
st.title("CO2 Emissions Calculator")
st.markdown("""
    This app estimates the CO2 emissions for different types of vehicles based on the distance travelled.
    Enter the distance and click on "Estimate Emissions" to see the results.
""")

distance = st.number_input("Enter distance in miles", value=0, step=1)

if st.button("Estimate Emissions"):
    if MY_API_KEY:
        with st.spinner("Estimating emissions..."):
            results = []
            for vehicle_type, activity_id in activity_ids.items():
                result = estimate_emissions(vehicle_type, activity_id, distance, "mi")
                if "CO2 Emissions (kg)" in result:
                    results.append(result)
                else:
                    st.error(f"Error for {vehicle_type}: {result['Error']}")

        if results:
            df = pd.DataFrame(results)
            df['Vehicle Type'] = pd.Categorical(df['Vehicle Type'], categories=["light", "mid_range", "heavy_duty"], ordered=True)
            df = df.sort_values('Vehicle Type')
            st.write(df)

            st.markdown("### CO2 Emissions by Vehicle Type")
            fig, ax = plt.subplots()
            ax.bar(df['Vehicle Type'], df['CO2 Emissions (kg)'], color=['lightblue', 'orange', 'green'])
            ax.set_xlabel('Vehicle Type')
            ax.set_ylabel('CO2 Emissions (kg)')
            ax.set_title('CO2 Emissions by Vehicle Type')
            st.pyplot(fig)

            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='co2_emissions.csv',
                mime='text/csv',
            )
    else:
        st.error("API key is missing. Please set up your API key in the environment variables.")
