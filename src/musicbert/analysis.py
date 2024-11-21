from transformers import AutoTokenizer, AutoModel
import torch

def analyze_music_with_musicbert(music_data):
    tokenizer = AutoTokenizer.from_pretrained("facebook/musicbert")
    model = AutoModel.from_pretrained("facebook/musicbert")
    inputs = tokenizer(music_data, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1)
    return embeddings
