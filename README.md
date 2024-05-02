# Vehicle CO2 Emissions Calculator

This project includes a Python script that uses the Climatiq API to calculate CO2 emissions for three types of vehicles over a distance of 16 miles. The vehicles considered are light, mid-range and heavy-duty vehicles. This project was commissioned by marllm.io

- `output_all_data.py` will return the unfiltered emission data.
- `output_sorted_data.py` will return a neat table and bar graph. 

## Getting Started

To run this script, you will need Python and the `requests` library installed. You'll also need an API key from Climatiq. https://www.climatiq.io/

### Prerequisites

- Python
- `requests` library (`pip install requests`)
- Climatiq API Key

### How to Use

1. Clone this repository.
2. Install the `requests` library using pip.
3. Insert your Climatiq API Key into the script.
4. Comment out Line 1 for output_all_data.py and output_sorted_data.py once you have inserted your CLimatiq API key
4. Run the script with Python to see the CO2 emissions calculations.
