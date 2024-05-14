# Vehicle CO2 Emissions Calculator

This project includes a Python script that uses the Climatiq API to calculate CO2 emissions for three types of vehicles over a distance of 16 miles. The vehicles considered are light, mid-range, and heavy-duty vehicles. This project was commissioned by [marllm.io](https://www.marllm.io/)

<img src="images/co2_emissions_chart.png" alt="CO2 Emissions Chart" width="400"/>

## Files Included

- `output_all_data.py`: This script will return the unfiltered emission data.
- `output_sorted_data.py`: This script will return a neat table and bar graph.
- `app.py`: This script creates an interactive Streamlit web app for estimating CO2 emissions.

## Getting Started

To run these scripts, you will need Python and the `requests` library installed. You'll also need an API key from Climatiq. [Climatiq API](https://www.climatiq.io/)

### Prerequisites

- Python
- `requests` library (`pip install requests`)
- Climatiq API Key
- Streamlit (`pip install streamlit`)

### How to Use

1. Clone this repository.
2. Install `requests` and `Streamlit` using pip: 
3. Insert your Climatiq API key into the script
4. Comment Line 1 in `output_all_data.py`, `output_sorted_data.py` and `app.py` once you've inserted your Climatiq API key.
5. To run the streamlit app, run `streamlit run app.py` in the terminal for app.py. This will start a local server. Open the URL provided in the terminal to interact with your app.