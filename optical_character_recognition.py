import pytesseract
from PIL import Image
import argparse


def ocr_image(image_path):
    """
    Perform OCR on an image using Tesseract.

    Parameters:
    - image_path (str): The path to the image file.

    Returns:
    - str: The recognized text from the image.
    """
    try:
        # Open an image file
        with Image.open(image_path) as img:
            # Perform OCR on the image
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        print(f"Error performing OCR: {e}")
        return None

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Perform OCR on an image using Tesseract.")
    
    # Add the arguments
    parser.add_argument("image_path", type=str, help="The path to the image file.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Perform OCR on the image
    result = ocr_image(args.image_path)
    
    # Print the recognized text
    if result:
        print(result)
    else:
        print("OCR failed. Please check the image path and ensure Tesseract is correctly installed.")

if __name__ == "__main__":
    main()
