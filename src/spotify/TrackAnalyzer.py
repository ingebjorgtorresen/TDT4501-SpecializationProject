class SpotifyTrackAnalyzer:
    def __init__(self, spotify_client):
        self.spotify_client = spotify_client

    def get_track_info(self, title, artist):
        query = f"track:{title} artist:{artist}"
        results = self.spotify_client.search(q=query, type="track", limit=1)
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            track_id = track['id']
            audio_features = self.spotify_client.audio_features(track_id)[0]
            return {
                "name": track["name"],
                "artist": track["artists"][0]["name"],
                "album": track["album"]["name"],
                "duration": track["duration_ms"],
                "features": audio_features
            }
        else:
            raise ValueError("Track not found on Spotify.")

    def map_audio_features_to_semantics(self, features):
        descriptors = []

        # Danceability
        if features["danceability"] > 0.7:
            descriptors.append("a highly danceable rhythm")
        elif features["danceability"] > 0.4:
            descriptors.append("a moderately danceable beat")
        else:
            descriptors.append("a low-key groove")

        # Energy
        if features["energy"] > 0.7:
            descriptors.append("high energy and intense dynamics")
        elif features["energy"] > 0.4:
            descriptors.append("a moderate energy level")
        else:
            descriptors.append("a calm and mellow tone")

        # Valence
        if features["valence"] > 0.7:
            descriptors.append("a joyful and positive mood")
        elif features["valence"] > 0.4:
            descriptors.append("a neutral and reflective atmosphere")
        else:
            descriptors.append("a somber and melancholic vibe")

        # Tempo
        descriptors.append(f"a tempo of around {features['tempo']} BPM")
        return descriptors
