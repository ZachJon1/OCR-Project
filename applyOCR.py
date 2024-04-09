import pytesseract
import cv2

def applyOCR(image):
    """_summary_
    Apply OCR to the image to extract the text from the image.

    Args:
        image_path (_type_): _description_

    Returns:
        _type_: _description_
        The extracted text from the image.
    """
    text = pytesseract.image_to_string(image)
    return text


# save the extracted text to a file
def saveText(text, file_path):
    """_summary_
    Save the extracted text to a file.

    Args:
        text (_type_): _description_
        file_path (_type_): _description_
    """
    with open(file_path, 'w') as file:
        file.write(text)