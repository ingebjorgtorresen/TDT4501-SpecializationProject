from midi_processing import load_midi_file
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from transformers import AutoModel

def analyze_music_with_musicbert(music_data):
    # Try using a generic BERT tokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")  # Or another BERT variant
    #model = AutoModelForSequenceClassification.from_pretrained("ruru2701/musicbert-v1.1")
    #tokenizer = AutoTokenizer.from_pretrained("ruru2701/musicbert-v1.1")
    model = AutoModel.from_pretrained("ruru2701/musicbert-v1.1")

    
    # Tokenize the input music data
    inputs = tokenizer(music_data, return_tensors="pt", truncation=True, padding=True)
    #inputs = tokenizer(music_data, return_tensors="pt", truncation=True, padding=True, clean_up_tokenization_spaces=True)

    
    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
    
    embeddings = outputs.last_hidden_state.mean(dim=1)

    return embeddings
    # Return logits
    #return outputs.logits

def normalize_embeddings(embeddings):
    """
    Normalize embeddings to ensure comparability across songs.
    """
    return (embeddings - embeddings.mean()) / embeddings.std()


"""def map_embeddings_to_semantics(embeddings):
    # Placeholder function: Replace with actual model or logic
    # Example: If embeddings indicate a high energy level
    #return ["energetic", "uplifting"]
    # Normalize embeddings for interpretability
    energy_level = embeddings.norm().item()
    
    if energy_level > 10:  # Example threshold
        return ["energetic", "uplifting"]
    else:
        return ["calm", "soothing"]"""

import torch

def map_embeddings_to_semantics(embeddings):
    """
    Map embeddings to semantic descriptors using advanced statistics.
    """
    normalized_embeddings = normalize_embeddings(embeddings)

    # Calculate additional statistics
    mean_value = normalized_embeddings.mean().item()
    std_value = normalized_embeddings.std().item()
    q25 = torch.quantile(normalized_embeddings, 0.25).item()
    q75 = torch.quantile(normalized_embeddings, 0.75).item()
    range_value = q75 - q25

    print(f"Embedding stats - Mean: {mean_value}, Std Dev: {std_value}, Q25: {q25}, Q75: {q75}, Range: {range_value}")

    semantics = []

    # Refine mood descriptors
    if mean_value > 0.2 or range_value > 1.5:
        semantics.append("uplifting")
    elif mean_value > -0.2:
        semantics.append("melancholic")
    else:
        semantics.append("dark")

    # Refine intensity descriptors
    if std_value > 0.6 or range_value > 2.0:
        semantics.append("energetic")
    elif std_value > 0.4:
        semantics.append("dynamic")
    else:
        semantics.append("calm")

    return semantics



def generate_image_prompt(song_title, artist, semantics):
    base_prompt = f"An artwork inspired by the song '{song_title}' by {artist}. "
    mood_description = "The mood is " + " and ".join(semantics) + "."
    return base_prompt + mood_description

def main():
    # Paths to MIDI files
    midi_file_path_1 = "/Users/ingtorre/Specialization_Project/TDT4501-SpecializationProject/src/musicbert/music/Coldplay - Viva La Vida.mid"
    midi_file_path_2 = "/Users/ingtorre/Specialization_Project/TDT4501-SpecializationProject/src/musicbert/music/Dancing_Queen.1.mid"

    # Song details
    song_1 = {"title": "Viva La Vida", "artist": "Coldplay", "file": midi_file_path_1}
    song_2 = {"title": "Dancing Queen", "artist": "ABBA", "file": midi_file_path_2}

    # List of songs to process
    songs = [song_1, song_2]

    for song in songs:
        try:
            print(f"\nProcessing {song['title']} by {song['artist']}...")

            # Step 1: Load MIDI file
            music_data = load_midi_file(song["file"])
            #print(f"Loading MIDI file: {file_path}")
            print(f"Music data length for {song['title']}: {len(music_data)}")

            # Step 2: Analyze music with MusicBERT
            embeddings = analyze_music_with_musicbert(music_data)
            print(f"Generated embeddings for {song['title']}: {embeddings.shape}")

            # Step 3: Map embeddings to semantic descriptors
            semantics = map_embeddings_to_semantics(embeddings)
            print(f"Semantic descriptors for {song['title']}: {semantics}")

            # Step 4: Generate image prompt
            prompt = generate_image_prompt(song["title"], song["artist"], semantics)
            print(f"Generated Prompt: {prompt}")

        except Exception as e:
            print(f"Error processing {song['title']} by {song['artist']}: {e}")



"""import os

def main():
    midi_folder = "/path/to/midi/files"
    song_details = [
        {"title": "Viva La Vida", "artist": "Coldplay", "file": "Coldplay - Viva La Vida.mid"},
        {"title": "Imagine", "artist": "John Lennon", "file": "John Lennon - Imagine.mid"},
    ]

    for song in song_details:
        try:
            midi_file_path = os.path.join(midi_folder, song["file"])
            music_data = load_midi_file(midi_file_path)
            embeddings = analyze_music_with_musicbert(music_data)
            semantics = map_embeddings_to_semantics(embeddings)
            prompt = generate_image_prompt(song["title"], song["artist"], semantics)
            print(f"Generated Prompt for '{song['title']}': {prompt}")
        except Exception as e:
            print(f"Error processing '{song['title']}': {e}")"""


if __name__ == "__main__":
    main()