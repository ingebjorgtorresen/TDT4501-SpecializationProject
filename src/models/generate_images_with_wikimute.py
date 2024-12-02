from src.models.model_loader_with_wikimute import load_stable_diffusion

def generate_image(prompt, output_path="output_image.png", steps=30, device=None):
    """
    Generate an image from a text prompt.

    Args:
        prompt (str): The text prompt to generate the image.
        output_path (str): The file path to save the image.
        steps (int): The number of inference steps (higher = better quality).
        device (str): Device to use ('cpu' or 'cuda').

    Returns:
        str: Path to the generated image.
    """
    try:
        # Load the Stable Diffusion pipeline
        pipeline = load_stable_diffusion(device=device)

        print(f"Generating image for prompt: '{prompt}'")
        image = pipeline(prompt, num_inference_steps=steps).images[0]

        # Save the generated image
        image.save(output_path)
        print(f"Image saved at: {output_path}")
        return output_path
    except Exception as e:
        print(f"Error generating image: {e}")
        return None
