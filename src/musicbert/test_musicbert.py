from midi_processing import load_midi_file
from analysis import analyze_music_with_musicbert

def main():
    # Path to your MIDI file
    midi_file_path = "/Users/ingtorre/Specialization_Project/TDT4501-SpecializationProject/src/musicbert/music/Coldplay - Viva La Vida.mid"
    
    # Step 1: Process MIDI file
    try:
        print("Loading and processing MIDI file...")
        midi_data = load_midi_file(midi_file_path)
        print(f"Processed MIDI data: {midi_data[:10]}...")  # Show first 10 notes for sanity check
        
        # Step 2: Analyze with MusicBERT
        print("Analyzing music with MusicBERT...")
        embeddings = analyze_music_with_musicbert(midi_data)
        print(f"Generated embeddings: {embeddings.shape}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
