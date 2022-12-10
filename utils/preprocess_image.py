# Import the required modules
from PIL import Image, ImageFilter, ImageEnhance
from skimage.morphology import dilation
import numpy as np

def preprocess_image(image_file, output_file):
    # Load the image
    image = Image.open(image_file)

    # Convert the image to grayscale
    image = image.convert("L")

    # Enhance the contrast of the image
    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(2)

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Apply dilation to the image
    kernel = np.ones((3, 3))
    image_array = dilation(image_array, kernel)

    # Save the preprocessed image
    image.save(output_file)
