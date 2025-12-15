import requests
import shutil
import os
import json

API_KEY = "pk_UtbYMlJeTXu4Wch1triTuA"   # replace with your API key from logo.dev
FOLDER_NAME = "logos"   # specify folder to save logos
DEFAULT_FILE_TYPE = "jpg"   # default file type, specify jpg or png
os.makedirs(FOLDER_NAME, exist_ok=True)

# Function to download logo for a given ticker
# Parameters:
#   ticker: stock ticker symbol
#   file_type: "jpg" or "png"
#   force: if True, re-download even if file exists
# Returns: None
# Example usage:
#   ticker_to_logo("AAPL", "png", False)
def ticker_to_logo(ticker, file_type, force):
    ticker = ticker.lower() # ensure lowercase
    print("Downloading logo for:", ticker)
    file_name = f"{ticker}.{file_type}"
    file_path = os.path.join(FOLDER_NAME, file_name)

    if (not force and os.path.exists(file_path)):
        print("Logo already exists, skipping download.")
        return

    # API call to get logo
    match file_type:
        case "jpg":
            IMAGE_URL = "https://img.logo.dev/ticker/" + ticker + "?token=" + API_KEY
        case "png":
            IMAGE_URL = "https://img.logo.dev/ticker/" + ticker + "?format=png&token=" + API_KEY
        case _:
            raise ValueError("Unsupported file type. Use 'jpg' or 'png'.")

    response = requests.get(IMAGE_URL, stream=True)
    if response.status_code == 200:
        with open(file_path, "wb") as out_file:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, out_file)
        print("Image successfully downloaded to: {file_path}")
    else:
        print("Failed to download.")


def getAllLogos(file_type = DEFAULT_FILE_TYPE, force = False):
    # Load ticker list from file
    with open("list_ticker.json", "r") as f:
        list_ticker = json.load(f)

    for ticker in list_ticker:
        ticker_to_logo(ticker, file_type, force)   # specify jpg or png (default jpg)

def getLogo(ticker, file_type = DEFAULT_FILE_TYPE, force = False):
    ticker_to_logo(ticker, file_type, force)   # specify jpg or png (default jpg)

def main():
    getAllLogos("jpg", False)
    # getLogo("AAPL", "jpg")  # Example for single ticker

if __name__ == "__main__":
    main()