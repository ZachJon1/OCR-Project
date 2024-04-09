import argparse
import sys
import os
import logging
import preProcess
import plot
import applyOCR
import cv2


def main():
    parser = argparse.ArgumentParser(description='Extract text from images.')   
    parser.add_argument('image_path', default="./imgs/", type=str, help='path to the image')
    parser.add_argument('output_path', default="./runs/", type=str, help='path to save the extracted text')
    parser.add_argument('--preprocess', action='store_true', help='preprocess the image')
    parser.add_argument('--plot', action='store_true', help='plot the image')
    args = parser.parse_args()

    if not os.path.exists(args.image_path):
        logging.error('Image path does not exist.')
        sys.exit(1)

    if args.preprocess:
        preProcess.ImagePreprocessor()
        # multiple preprocess methods can be applied here
        # for example, apply thresholding to the image
        image = cv2.imread(args.image_path)
        image = preProcess.ImagePreprocessor.grayScale(image)
        image = preProcess.ImagePreprocessor.removeNoise(image)
        image = preProcess.ImagePreprocessor.thresholding(image)
        image = preProcess.ImagePreprocessor.canny(image)
        # save the preprocessed image to different path
        cv2.imwrite('./preProcessed/preprocessed_image.jpg', image)
        
    if args.plot:
        # plot the image after preprocessing
        image = cv2.imread(args.image_path)
        image = preProcess.ImagePreprocessor.grayScale(image)
        image = preProcess.ImagePreprocessor.removeNoise(image)
        image = preProcess.ImagePreprocessor.thresholding(image)
        image = preProcess.ImagePreprocessor.canny(image)
        plot.plotImage(image, 'Preprocessed Image')
        
    # apply OCR to preprocessed image
    text = applyOCR.applyOCR(image)
    applyOCR.saveText(text, args.output_path)
    logging.info('Text extracted successfully.')
    logging.info(f'Text saved to {args.output_path}')
    
    
if __name__ == '__main__':
    main()
    
   
    
    
        
