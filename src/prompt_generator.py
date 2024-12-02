from src.models.generate_images_with_wikimute import generate_image
from src.models.utils import ensure_directory_exists
import os
from src.wikiMuTe.load_data import load_wikimute_data
from src.wikiMuTe.preprocess import preprocess_wikimute

import pandas as pd

def generate_prompts(data_path):
    """
    Generate prompts for specific songs based on the dataset.

    Args:
        data_path (str): Path to the data directory containing `all.csv`.

    Returns:
        list: A list of prompts for the specified songs.
    """
    csv_file_path = os.path.join(data_path, "all.csv")
    print("CSV file path:", csv_file_path)

    try:
        # Load the CSV file
        df = pd.read_csv(csv_file_path, header=None)
        df.columns = [
            "filename",
            "id",
            "categories",
            "details",
            "file_url",
            "wiki_url"
        ]  # Adjust column names to match the structure of your CSV
        
        # Specify the songs of interest
        target_songs = ["Silent Night", "Viva la Vida", "Michael Jackson Thriller"]
        
        # Filter for the target songs based on their filenames
        filtered_df = df[df["filename"].str.contains("|".join(target_songs), case=False)]

        # Generate custom prompts based on the song details
        prompts = []
        for _, row in filtered_df.iterrows():
            song_name = row["filename"].split(".")[0]  # Extract the song name
            categories = row["categories"]
            details = row["details"]

            prompt = f"Create an image inspired by the song '{song_name}' using themes such as {categories}. "
            if isinstance(details, str) and len(details) > 0:
                prompt += f"Include visual elements suggested by: {details}."
            prompts.append(prompt)

        return prompts

    except FileNotFoundError as e:
        print(f"Error loading data: {e}")
        return []



"""def generate_prompts(file_path):
    """"""
    Generate prompts from the WikiMuTe dataset.
    Args:
        file_path (str): Path to the WikiMuTe CSV file.
    Returns:
        list: List of generated prompts.
    """"""
    data = load_wikimute_data(file_path)
    if data is not None:
        prompts = preprocess_wikimute(data)
        return prompts
    return []"""

def generate_images_from_prompts(prompts, output_dir="generated_images", steps=30, device=None):
    """
    Generate images from a list of prompts using Stable Diffusion.

    Args:
        prompts (list): List of prompts to generate images for.
        output_dir (str): Directory to save the generated images.
        steps (int): Number of inference steps (higher = better quality).
        device (str): Device to use ('cpu' or 'cuda').

    Returns:
        None
    """
    ensure_directory_exists(output_dir)
    for i, prompt in enumerate(prompts):
        output_path = os.path.join(output_dir, f"image_{i}.png")
        generate_image(prompt, output_path, steps, device)



