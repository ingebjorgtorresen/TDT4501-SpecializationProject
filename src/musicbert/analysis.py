from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

def analyze_music_with_musicbert(music_data):
    # Try using a generic BERT tokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")  # Or another BERT variant
    model = AutoModelForSequenceClassification.from_pretrained("ruru2701/musicbert-v1.1")
    
    # Tokenize the input music data
    inputs = tokenizer(music_data, return_tensors="pt", truncation=True, padding=True)
    
    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Return logits
    return outputs.logits
