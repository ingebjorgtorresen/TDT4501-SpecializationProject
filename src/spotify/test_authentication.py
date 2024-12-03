import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def validate_spotify_credentials():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))

    if response.status_code == 200:
        print("Spotify credentials are valid.")
        print("Access Token:", response.json()["access_token"])
    else:
        print("Failed to validate credentials:", response.status_code, response.json())

validate_spotify_credentials()

def get_new_access_token():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))
    if response.status_code == 200:
        access_token = response.json().get("access_token")
        print("New Access Token:", access_token)
        return access_token
    else:
        print("Failed to get new access token:", response.status_code, response.json())
        return None

#get_new_access_token()