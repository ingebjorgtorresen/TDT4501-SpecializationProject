import pretty_midi

"""def load_midi_file(file_path):
    # Load MIDI file and convert it into a symbolic representation
    # Example: Using pretty_midi to load MIDI and process
    midi_data = pretty_midi.PrettyMIDI(file_path)
    # Process midi_data as needed
    return midi_data"""

"""def load_midi_file(file_path):
    midi_data = pretty_midi.PrettyMIDI(file_path)
    # Convert MIDI to a symbolic representation suitable for MusicBERT
    notes = [note.pitch for instrument in midi_data.instruments for note in instrument.notes]
    return notes
"""

"""def load_midi_file(file_path):
    
    #Load MIDI file and convert it to a space-separated string of note pitches.
    
    midi_data = pretty_midi.PrettyMIDI(file_path)
    # Extract note pitches from all instruments
    notes = [note.pitch for instrument in midi_data.instruments for note in instrument.notes]
    # Convert notes to a space-separated string
    music_data = " ".join(map(str, notes))
    return music_data"""

"""def load_midi_file(file_path):
    try:
        midi_data = pretty_midi.PrettyMIDI(file_path)
    except Exception as e:
        raise ValueError(f"Invalid MIDI file: {e}")
    notes = [note.pitch for instrument in midi_data.instruments for note in instrument.notes]
    return " ".join(map(str, notes))
"""

def load_midi_file(file_path, max_length=512):
    """
    Load MIDI file and convert it to a space-separated string of note pitches.
    Truncate the output to `max_length` tokens.
    """
    try:
        midi_data = pretty_midi.PrettyMIDI(file_path)
        notes = [note.pitch for instrument in midi_data.instruments for note in instrument.notes]
        music_data = " ".join(map(str, notes))
        return music_data[:max_length]
    except Exception as e:
        raise ValueError(f"Invalid MIDI file: {e}")
