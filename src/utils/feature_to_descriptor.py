def convert_features_to_descriptors(features):
    descriptors = []

    # Valence
    valence = features.get("valence")
    if valence is not None:
        if valence < 0.3:
            descriptors.append("melancholic")
        elif valence < 0.7:
            descriptors.append("neutral")
        else:
            descriptors.append("happy")

    # Energy
    energy = features.get("energy")
    if energy is not None:
        if energy < 0.3:
            descriptors.append("calm")
        elif energy < 0.7:
            descriptors.append("moderate")
        else:
            descriptors.append("energetic")

    # Danceability
    danceability = features.get("danceability")
    if danceability is not None:
        if danceability < 0.3:
            descriptors.append("gentle")
        elif danceability < 0.7:
            descriptors.append("groovy")
        else:
            descriptors.append("danceable")

    # Tempo
    tempo = features.get("tempo")
    if tempo is not None:
        if tempo < 80:
            descriptors.append("slow-paced")
        elif tempo < 120:
            descriptors.append("moderate pace")
        else:
            descriptors.append("fast-paced")

    # Mode
    mode = features.get("mode")
    if mode is not None:
        if mode == 1:
            descriptors.append("bright")
        else:
            descriptors.append("dark")

    # Loudness
    loudness = features.get("loudness")
    if loudness is not None:
        if loudness < -15:
            descriptors.append("soft")
        elif loudness < -5:
            descriptors.append("balanced")
        else:
            descriptors.append("loud")

    return descriptors
