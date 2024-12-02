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

def test_audio_features():
    """
    Test fetching audio features for a specific track.
    """
    track_id = "0VjIjW4GlUZAMYd2vXMi3b"  # Replace with a valid Spotify track ID
    try:
        features = fetch_audio_features(track_id)
        print("Audio Features:")
        for key, value in features.items():
            print(f"- {key}: {value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_audio_features()
