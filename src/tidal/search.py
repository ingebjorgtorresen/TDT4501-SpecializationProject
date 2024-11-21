def get_tidal_track_info(session, title, artist):
    search_results = session.search('track', title)
    for track in search_results.tracks:
        if track.artist.name.lower() == artist.lower():
            return track
    print("Track not found on TIDAL.")
    return None
