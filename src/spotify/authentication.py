"""import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def authenticate_spotify():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)
"""

import os
import requests
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

"""def get_access_token():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}
    
    response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))
    response_data = response.json()
    
    if response.status_code == 200:
        return response_data['access_token']
    else:
        raise Exception(f"Failed to get access token: {response_data}")
"""

# Globals to store token and its expiration time
ACCESS_TOKEN = None
TOKEN_EXPIRATION = None

def get_access_token():
    global ACCESS_TOKEN, TOKEN_EXPIRATION

    # Check if the token is still valid
    if ACCESS_TOKEN and TOKEN_EXPIRATION and time.time() < TOKEN_EXPIRATION:
        return ACCESS_TOKEN

    # Generate a new token
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))
    if response.status_code == 200:
        response_data = response.json()
        ACCESS_TOKEN = response_data["access_token"]
        TOKEN_EXPIRATION = time.time() + response_data["expires_in"]
        return ACCESS_TOKEN
    else:
        raise Exception(f"Failed to get access token: {response.status_code}, {response.json()}")