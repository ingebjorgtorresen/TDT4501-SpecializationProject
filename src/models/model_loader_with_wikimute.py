from diffusers import StableDiffusionPipeline
import torch

def load_stable_diffusion(model_name="CompVis/stable-diffusion-v1-4", device=None):
    """
    Load the Stable Diffusion pipeline.

    Args:
        model_name (str): The Hugging Face model repository name.
        device (str): Device to use ('cpu' or 'cuda'). If None, auto-detects.

    Returns:
        StableDiffusionPipeline: The loaded pipeline.
    """
    if device is None:
        device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Loading Stable Diffusion model on {device}...")

    # Load the pipeline
    pipeline = StableDiffusionPipeline.from_pretrained(
        model_name,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    pipeline.to(device)
    print("Model loaded successfully!")
    return pipeline
