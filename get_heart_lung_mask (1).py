import cv2
import os
from PIL import Image
import glob

def separate_heart_and_lung(img_):
    hsv = cv2.cvtColor(img_, cv2.COLOR_BGR2HSV)

    heart_low_lim = (0, 0, 85)
    heart_up_lim = (85, 85, 85)
    lung_low_lim = (0, 0, 240)
    lung_up_lim = (255, 15, 255)

    heart_mask = cv2.inRange(hsv, heart_low_lim, heart_up_lim)
    lung_mask = cv2.inRange(hsv, lung_low_lim, lung_up_lim)
    return heart_mask, lung_mask


if __name__ == "__main__":
    
    file_path = './images/'
    
    
    for image_path in glob.glob(file_path + '*.png'):
        img = cv2.imread(image_path)
        mask_heart, mask_lung = separate_heart_and_lung(img)
        # save the masks as png files with same name as the original image
        image_name = image_path.split('\\')[-1]
        cv2.imwrite('./heart/' + image_name, mask_heart)
        cv2.imwrite('./lungs/' + image_name, mask_lung)


