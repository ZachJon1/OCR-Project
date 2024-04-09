import cv2


class ImagePreprocessor:
    """_summary_
    Preprocess the image to make it easier to detect the edges of the image.
    methods: grayScale, removeNoise, thresholding, canny

    Returns:
        _type_: _description_
        Each method returns the image after applying the corresponding operation.
    """
    @staticmethod
    def grayScale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def removeNoise(image):
        return cv2.GaussianBlur(image, (5, 5), 0)

    @staticmethod
    def thresholding(image):
        return cv2.adaptiveThreshold(image, 255,
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 13, 2)

    @staticmethod
    def canny(image):
        return cv2.Canny(image, 100, 200)
    
   
