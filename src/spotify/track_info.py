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
