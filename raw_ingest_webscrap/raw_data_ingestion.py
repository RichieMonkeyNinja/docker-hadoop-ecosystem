import requests
from bs4 import BeautifulSoup
import os 
import pandas as pd
import re

from pathlib import Path

def download_airbnb_dataset(cities, target_url):
    # Target link
    target_url = target_url
    headers = {'User-Agent': 'Mozilla/5.0'}

    print("Searching for latest data links")
    response = requests.get(target_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all table rows which contain city data
    rows = soup.find_all('tr')

    for city_name in cities:
        found = False
        for row in rows:
            # Inside Airbnb tables use city names in their headers or text
            if city_name.lower() in row.get_text().lower():
                # Look for the 'visualisations/listings.csv' link specifically
                link_tag = row.find('a', href=lambda href: href and 'listings.csv.gz' in href)

                if link_tag:
                    download_url = link_tag['href']

                    filename = f"{city_name.lower()}_listings.csv"

                    print(f"Found {city_name}! Downloading from: {download_url}")

                    # Perform the download
                    df = pd.read_csv(download_url)
                    df['city'] = city_name.lower()
                    df['extraction_date'] = re.search(r"\d{4}-\d{2}-\d{2}", download_url).group()
                    # print(df.dtypes)

                    
                    important_dtypes = {
                        'host_listings_count': 'float64',
                        'host_total_listings_count': 'float64',
                        'license':'str',
                        'minimum_minimum_nights':'float64',
                        'maximum_minimum_nights':'float64',
                        'minimum_maximum_nights':'float64',
                        'maximum_maximum_nights':'float64'
                    }

                    df = df.astype({k:v for k,v in important_dtypes.items() if k in df.columns})
                    base_dir = Path("/bronze_layer") / "listings"

                    city_dir = base_dir / f"city={city_name.lower()}"
                    date_dir = city_dir / f"extraction_date={re.search(r'\d{4}-\d{2}-\d{2}', download_url).group()}"

                    # ✅ CREATE DIRECTORIES
                    date_dir.mkdir(parents=True, exist_ok=True)

                    # parquet file path
                    output_path = date_dir / "listings.parquet"

                    df.to_parquet(
                        output_path,
                        index=False,
                        engine="pyarrow"
                    )

                    print(f"Saved: {output_path}")

                    found = True
                    break # Move to next city after finding the first (latest) match

        if not found:
            print(f"Could not find recent data for: {city_name}")

# City name
target_url = "http://insideairbnb.com/get-the-data.html"
target_cities = ["London", "Bristol", "Edinburgh"]
download_airbnb_dataset(target_cities, target_url)            