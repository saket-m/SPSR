import sys
import os
import numpy as np
import cv2

def save_crops(image_path, crop_dir):
    '''
    Crops(16 times sequentialy) the image present in image_path and saves them
    in crop_dir.
    '''
    n_crop = 9

    image = cv2.imread(image_path)
    h, w, _ = image.shape

    crop_h = h // n_crop
    crop_w = w // n_crop

    for i in range(n_crop):
        for j in range(n_crop):
            image_crop = image[i*crop_h : (i+1)*crop_h, j*crop_w : (j+1)*crop_w, :]
            print(os.path.join(crop_dir, image_path.replace('.png', f'_{i}{j}.png')))
            cv2.imwrite(os.path.join(crop_dir, image_path.split('/')[-1].replace('.png', f'_{i}{j}.png')), image_crop)

if __name__ == '__main__':
    image_path = sys.argv[1]
    crop_dir = sys.argv[2]

    if not os.path.exists(crop_dir):
        os.makedirs(crop_dir)
    else:
        os.system(f'rm {crop_dir} -rf')
        os.makedirs(crop_dir)

    save_crops(image_path, crop_dir)
