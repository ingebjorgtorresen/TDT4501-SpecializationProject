import pretty_midi

"""def load_midi_file(file_path):
    # Load MIDI file and convert it into a symbolic representation
    # Example: Using pretty_midi to load MIDI and process
    midi_data = pretty_midi.PrettyMIDI(file_path)
    # Process midi_data as needed
    return midi_data"""

def load_midi_file(file_path):
    midi_data = pretty_midi.PrettyMIDI(file_path)
    # Convert MIDI to a symbolic representation suitable for MusicBERT
    notes = [note.pitch for instrument in midi_data.instruments for note in instrument.notes]
    return notes
