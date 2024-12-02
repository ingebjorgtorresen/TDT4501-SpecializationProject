import requests
from src.spotify.authentication import get_access_token  # Ensure this is imported

def fetch_audio_features(track_id):
    """
    Fetches audio features for a track using the Spotify API.
    """
    access_token = get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch audio features: {response.status_code}, {response.json()}")


def get_track_info(sp, title, artist):
    query = f"track:{title} artist:{artist}"
    results = sp.search(q=query, type="track", limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_id = track['id']
        audio_features = sp.audio_features(track_id)[0]
        return {
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "album": track["album"]["name"],
            "duration": track["duration_ms"],
            "features": audio_features
        }
    else:
        print("Track not found on Spotify.")
        return None