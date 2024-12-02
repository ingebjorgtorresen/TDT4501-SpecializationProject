def preprocess_wikimute(data):
    """
    Preprocess the WikiMuTe dataset to extract prompts.
    Args:
        data (pd.DataFrame): The WikiMuTe dataset.
    Returns:
        list: A list of prompts.
    """
    prompts = []
    for _, row in data.iterrows():
        aspects = row.get("aspects", "")
        sentence = row.get("sentences", "")
        # Create a meaningful prompt
        prompt = f"A visual depiction of '{aspects}' inspired by the sentence: '{sentence}'."
        prompts.append(prompt)
    return prompts


"""from .load_data import load_wikimute_dataset

def preprocess_aspects(aspect_column):
    #Clean and parse the 'aspects' column.
    return aspect_column.str.strip("[]").str.replace("'", "").str.split(", ")

def preprocess_sentences(sentences_column):
    #Process the 'sentences' column.
    return sentences_column.apply(lambda x: x.split(". "))

def preprocess_dataset(file_path="data/all.csv"):
    #Load and preprocess the dataset.
    dataset = load_wikimute_dataset(file_path)
    dataset["aspects"] = preprocess_aspects(dataset["aspects"])
    dataset["sentences"] = preprocess_sentences(dataset["sentences"])
    return dataset
"""