"""from src.tidal.authentication import authenticate_tidal
from src.tidal.search import get_tidal_track_info
from src.musicbert.midi_processing import load_midi_file
from src.musicbert.analysis import analyze_music_with_musicbert
from src.utils.prompt_generator import generate_prompt
from src.openai.dall_e import generate_image"""

from spotify.authentication import authenticate_spotify
from spotify.track_info import get_track_info
from utils.feature_to_descriptor import convert_features_to_descriptors
from musicbert.analysis import analyze_music_with_musicbert
from musicbert.midi_processing import load_midi_file
from stable_diffusion.model_loader import load_stable_diffusion
from stable_diffusion.generate_image import generate_image
from wikiMuTe.train import train_wikimute

def main(title, artist, midi_path):
        # Step 1: Authenticate and retrieve Spotify features
    sp = authenticate_spotify()
    track_info = get_track_info(sp, title, artist)
    if not track_info:
        print("Track not found.")
        return
    
    # Convert audio features to descriptors
    descriptors = convert_features_to_descriptors(track_info["features"])
    print("Spotify Descriptors:", descriptors)

    # Step 2: Load MIDI file and get MusicBERT embeddings
    symbolic_data = load_midi_file(midi_path)
    musicbert_embeddings = analyze_music_with_musicbert(symbolic_data)
    print("MusicBERT Embeddings:", musicbert_embeddings)

    # Combine Spotify descriptors with MusicBERT embeddings or descriptors
    # Example: Generate a prompt based on both
    prompt = " ".join(descriptors) + " " + "a piece with abstract qualities"
    print("Generated Prompt:", prompt)

"""    # Authenticate with TIDAL
    session = authenticate_tidal()
    if not session:
        return

    # Retrieve track metadata from TIDAL
    track = get_tidal_track_info(session, title, artist)
    if not track:
        return

    print(f"Found track: {track.name} by {track.artist.name}")

    # Load symbolic data (MIDI file)
    music_data = load_midi_file(midi_path)

    # Analyze music data with MusicBERT
    labels = analyze_music_with_musicbert(music_data)
    print("Extracted labels:", labels)

    # Generate a prompt for DALL-E
    prompt = generate_prompt(labels)
    print("Generated prompt:", prompt)

    # Generate an image based on the prompt
    image_url = generate_image(prompt)
    print("Generated image URL:", image_url)"""

if __name__ == "__main__":
    main("Viva La Vida", "Coldplay", "/Users/ingtorre/Downloads/Coldplay - Viva La Vida.mid")
    train_wikimute()


"""from soundfile.audio_processing import extract_audio_features
from models.music_semantic_analysis import analyze_music_to_text
from openai.image_generation import generate_image

def main(music_file):
    # 1. Extract audio features
    features = extract_audio_features(music_file)
    
    # 2. Analyze the music and get a description
    description = analyze_music_to_text(features)
    
    # 3. Generate an image from the description
    image_url = generate_image(description)
    print(f"Generated Image URL: {image_url}")

if __name__ == "__main__":
    music_file = "path/to/music/file.mp3"
    main(music_file)
"""