from src.utils.config import DATA_PATH
from src.prompt_generator import generate_prompts, generate_images_from_prompts

if __name__ == "__main__":
    # Step 1: Load and preprocess prompts for the specific songs
    prompts = generate_prompts(DATA_PATH)
    
    # Step 2: Print the selected prompts (for debugging)
    print("Generated prompts:")
    for prompt in prompts:
        print(prompt)
    
    # Step 3: Generate images using Stable Diffusion
    generate_images_from_prompts(prompts, output_dir="output_images", steps=50)
