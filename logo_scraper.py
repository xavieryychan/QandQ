import requests
import shutil
import os
import json

API_KEY = "pk_UtbYMlJeTXu4Wch1triTuA"
FOLDER_NAME = "logos"

# Load ticker list from file
with open("list_ticker.json", "r") as f:
    list_ticker = json.load(f)

# count = 0

# Download logos
for ticker in list_ticker:
    ticker = ticker.lower() # ensure lowercase
    # count += 1
    # if (count >= 20):
    #     break  # limit to first 20 for testing
    file_name = f"{ticker}.jpg"
    print("Downloading logo for:", ticker)
    os.makedirs(FOLDER_NAME, exist_ok=True)
    file_path = os.path.join(FOLDER_NAME, file_name)

    # API call to get logo
    IMAGE_URL = "https://img.logo.dev/ticker/" + ticker + "?token=" + API_KEY

    response = requests.get(IMAGE_URL, stream=True)
    if response.status_code == 200:
        with open(file_path, "wb") as out_file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, out_file)
        print("Image successfully downloaded to: {file_path}")
    else:
        print("Failed to download.")