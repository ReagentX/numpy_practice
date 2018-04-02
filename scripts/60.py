import numpy as np
from io import BytesIO
from PIL import Image
import requests


URL = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
response = requests.get(URL)

# Get the response as an image object
im = Image.open(BytesIO(response.content))
print(f'Image: {im.height}x{im.width}')

# Convert to a NumPy array
a = np.array(im)
print(a[:1])
