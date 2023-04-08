import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the Puma Store India webpage
url = "https://in.puma.com/store-locator"
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the store elements
store_elements = soup.find_all("div", class_="store-locator-store")

# Initialize lists to store the extracted data
store_names = []
store_addresses = []
store_timings = []
store_phone_numbers = []


# Loop through each store element and extract the required data
for store_element in store_elements:
    store_name = store_element.find("h2", class_="store-locator-store-title").text.strip()
    store_address = store_element.find("div", class_="store-locator-store-address").text.strip()
    store_timing = store_element.find("div", class_="store-locator-store-timings").text.strip()
    store_phone_number = store_element.find("div", class_="store-locator-store-phone").text.strip()
    # store_latitude = store_element.find("span", class_="store-locator-store-lat").text.strip()
    # store_longitude = store_element.find("span", class_="store-locator-store-lon").text.strip()
    
    # Append the extracted data to the respective lists
    store_names.append(store_name)
    store_addresses.append(store_address)
    store_timings.append(store_timing)
    store_phone_numbers.append(store_phone_number)
# Create a DataFrame to store the extracted data
data = {
    "Store Name": store_names,
    "Address": store_addresses,
    "Timing": store_timings,
    "Phone Number": store_phone_numbers,
    # "Latitude": store_latitudes,
    # "Longitude": store_longitudes
}
df = pd.DataFrame(data)

# Check the DataFrame for any missing data or errors
print(df.info())

# Save the data to a CSV file
try:
    df.to_csv("puma_store_data.csv", index=False)
    print("Data saved to CSV file")
except Exception as e:
    print("Error saving data to CSV file:", e)
