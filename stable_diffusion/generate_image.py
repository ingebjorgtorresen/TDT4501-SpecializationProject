from model_loader import load_stable_diffusion

def generate_image(prompt, output_path="output_image.png", steps=30, use_cpu=True):
    """
    Generate an image from a text prompt.

    Args:
        prompt (str): The text prompt to generate the image.
        output_path (str): The file path to save the image.
        steps (int): The number of inference steps (higher = better quality).
        use_cpu (bool): If True, forces generation on CPU.

    Returns:
        None
    """
    # Load the Stable Diffusion pipeline
    pipeline = load_stable_diffusion(use_cpu=use_cpu)
    
    print(f"Generating image for prompt: '{prompt}'")
    image = pipeline(prompt, num_inference_steps=steps).images[0]
    
    # Save the generated image
    image.save(output_path)
    print(f"Image saved at: {output_path}")

if __name__ == "__main__":
    # Example prompt
    prompt = "A futuristic cityscape with flying cars under a sunset sky"
    
    # Generate the image
    generate_image(prompt, "futuristic_city.png", steps=50)
