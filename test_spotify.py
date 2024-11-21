import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables
load_dotenv()

# Authenticate with Spotify
def authenticate_spotify():
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(auth_manager=auth_manager)

# Retrieve track metadata and audio features
def test_spotify_track_info(title, artist):
    sp = authenticate_spotify()
    query = f"track:{title} artist:{artist}"
    results = sp.search(q=query, type="track", limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_id = track['id']
        audio_features = sp.audio_features(track_id)[0]
        
        # Print track details and audio features
        print(f"Track Name: {track['name']}")
        print(f"Artist: {track['artists'][0]['name']}")
        print(f"Album: {track['album']['name']}")
        print(f"Duration: {track['duration_ms']} ms")
        print("Audio Features:", audio_features)
    else:
        print("Track not found on Spotify.")

# Run test with a sample song
if __name__ == "__main__":
    # Replace these with a song and artist you want to test
    test_spotify_track_info("Blinding Lights", "The Weeknd")
