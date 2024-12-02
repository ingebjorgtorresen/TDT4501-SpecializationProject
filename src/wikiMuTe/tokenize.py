from transformers import AutoTokenizer

def tokenize_sentences(sentences, model_name="bert-base-uncased"):
    """Tokenize sentences using a specified tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return sentences.apply(lambda x: tokenizer(x, padding=True, truncation=True, return_tensors="pt"))
