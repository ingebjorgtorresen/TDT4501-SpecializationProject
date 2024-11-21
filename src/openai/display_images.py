from PIL import Image
import requests
from io import BytesIO

def display_image_from_url(image_url):
    response = requests.get(image_url)
    img = Image.open(BytesIO(response.content))
    img.show()
