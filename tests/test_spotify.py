"""from src.spotify.authentication import authenticate_spotify
from src.spotify.track_info import get_track_info

# Test Spotify Track Info
def test_spotify_track_info(title, artist):
    sp = authenticate_spotify()
    track_info = get_track_info(sp, title, artist)
    if track_info:
        print("Track Details:")
        print(f"- Name: {track_info['name']}")
        print(f"- Artist: {track_info['artist']}")
        print(f"- Album: {track_info['album']}")
        print(f"- Duration: {track_info['duration']} ms")
        print("\nAudio Features:")
        for feature, value in track_info["features"].items():
            print(f"- {feature}: {value}")

# Run test with a sample song
if __name__ == "__main__":
    # Replace these with a song and artist you want to test
    test_spotify_track_info("Blinding Lights", "The Weeknd")
"""

from src.spotify.track_info import fetch_audio_features
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

"""def test_audio_features():
    
    #Test fetching audio features for a specific track.
    
    track_id = "0VjIjW4GlUZAMYd2vXMi3b"  # Replace with a valid Spotify track ID
    try:
        features = fetch_audio_features(track_id)
        print("Audio Features:")
        for key, value in features.items():
            print(f"- {key}: {value}")
    except Exception as e:
        print(f"Error: {e}")"""

def test_track_id(track_id):
    access_token = os.getenv("SPOTIFY_ACCESS_TOKEN")
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://api.spotify.com/v1/tracks/{track_id}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Track ID is valid. Track details:")
        print(response.json())
    elif response.status_code == 403:
        print("403 Forbidden: Ensure the track is publicly accessible.")
    else:
        print(f"Failed to fetch track details: {response.status_code}, {response.json()}")

def test_audio_features_direct(track_id):
    token = "YOUR_NEW_ACCESS_TOKEN"  # Replace with a valid token
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(url, headers=headers)
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())

def test_audio_features():
    track_id = "0GjEhVFGZW8afUYGChu3Rr"  # Replace with a valid Spotify track ID
    try:
        features = fetch_audio_features(track_id)
        if features:
            print("Audio Features:")
            for key, value in features.items():
                print(f"- {key}: {value}")
        else:
            print("No audio features available for this track.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_track_id("0GjEhVFGZW8afUYGChu3Rr")  # Test Dancing Queen Spotify track ID
    test_audio_features_direct("0GjEhVFGZW8afUYGChu3Rr")  # Test Dancing Queen Spotify track ID
    test_audio_features()
