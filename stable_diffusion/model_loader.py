from diffusers import StableDiffusionPipeline
import torch

def load_stable_diffusion(model_name="CompVis/stable-diffusion-v1-4", use_cpu=True):
    """
    Load the Stable Diffusion pipeline.

    Args:
        model_name (str): The Hugging Face model repository name.
        use_cpu (bool): If True, forces the model to run on CPU.

    Returns:
        StableDiffusionPipeline: The loaded pipeline.
    """
    device = "cpu" if use_cpu else "cuda"
    print(f"Loading Stable Diffusion model on {device}...")
    
    # Load the pipeline
    pipeline = StableDiffusionPipeline.from_pretrained(
        model_name,
        torch_dtype=torch.float32  # Use float32 for CPU compatibility
    )
    pipeline.to(device)
    print("Model loaded successfully!")
    return pipeline