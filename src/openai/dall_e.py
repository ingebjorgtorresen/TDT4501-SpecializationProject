import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_image(prompt):
    response = openai.Image.create(model="dall-e-3", prompt=prompt, n=1, size="1024x1024")
    return response['data'][0]['url']


"""import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key from the .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
openai.api_key = openai_api_key

# Generate an image using DALL-E 3
response = openai.Image.create(
  model="dall-e-3",
  prompt="a white siamese cat",  # Example prompt
  n=1,                           # Number of images to generate
  size="1024x1024"                # Size of the generated image
)

# Get the URL of the generated image
image_url = response['data'][0]['url']

# Print the image URL
print(f"Generated image URL: {image_url}")
"""