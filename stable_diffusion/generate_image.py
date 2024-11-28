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
    """prompt = "A futuristic cityscape with flying cars under a sunset sky"
    
    # Generate the image
    generate_image(prompt, "futuristic_city.png", steps=50)
    """
    prompt = "Illustrate the essence of the song 'Dancing Queen' by ABBA, focusing on the emotions of joy, freedom, and youthful exuberance. Depict a luminous dance floor bathed in soft, golden light, symbolizing nostalgia and happiness. At the center, portray a radiant young woman lost in the moment, spinning gracefully as if time stands still. Her expression conveys pure bliss and self-expression. Surround her with an abstract flow of vibrant colors—swirls of gold, pink, and blue—that reflect the rhythm and energy of the music. The scene should evoke a sense of timeless celebration and the joy of being alive and carefree."
    prompt2 = "Create an image inspired by the song 'Viva La Vida' by Coldplay, focusing on its themes of power, loss, and redemption. Depict a fallen king standing atop the ruins of a once-mighty throne, gazing over a vast, desolate kingdom. The atmosphere is ethereal, with stormy skies breaking into rays of golden light, symbolizing hope amidst despair. Surround the figure with subtle motifs of broken chains, crumbled statues, and fading crowns, representing the transient nature of power and glory. The scene should feel poignant and reflective, blending a sense of grandeur with the fragility of human ambition and the inevitability of change."
    prompt3 = "Create a serene and peaceful scene inspired by the song 'Silent Night.' Depict a snow-covered village illuminated by the soft glow of warm, golden lights from small, cozy homes. A beautiful starry sky dominates the backdrop, with a radiant star shining brightly above. In the foreground, show a quiet church surrounded by gently falling snow, evoking feelings of calm and wonder. Add subtle details like evergreen trees dusted with snow, children building a snowman, and a sense of stillness and tranquility that embodies the sacred and magical atmosphere of a silent, holy night."
    prompt4 = "Illustrate an electrifying and spooky scene inspired by Michael Jackson's 'Thriller.' Set the stage in a misty, eerie graveyard under a full moon, with gnarled trees silhouetted against the night sky. Show a group of undead figures—zombies—dancing in perfect synchronization, their expressions a mix of haunting and playful. Include Michael Jackson as the central figure, wearing his iconic red jacket, performing his signature dance moves. The atmosphere should be dark and suspenseful, with glowing eyes, creeping fog, and dramatic lighting, capturing the song's blend of horror, excitement, and iconic style."
    # Generate the image
    generate_image(prompt, "dancingQueen.png", steps=50)
    generate_image(prompt2, "vivaLaVida.png", steps=50)
    generate_image(prompt3, "silentNight.png", steps=50)
    generate_image(prompt4, "thriller.png", steps=50)