import sys
import os

import numpy as np
import cv2

def get_abs_listdir(DIR):
    '''
    Returns the absolute or relative addresses.
    '''
    return sorted([os.path.join(DIR, frame) for frame in os.listdir(DIR)])

def stitch_image(crop_dir, image_w, image_h, image_name):
    '''
    Takes all the images present in crop_dir(of same dim) and
    stitches them together to get the o/p image
    '''
    op_image = np.zeros((image_h * 2, image_w * 2, 3))

    crop_list = get_abs_listdir(crop_dir)
    n_crop = int(np.sqrt(len(crop_list)))

    crop_w = (image_w // n_crop) * 2
    crop_h = (image_h // n_crop) * 2

    k = 0
    for i in range(n_crop):
        for j in range(n_crop):
            image = cv2.imread(crop_list[k])
            print(image.shape)
            image = cv2.resize(image, (crop_w, crop_h))
            print(image.shape)
            op_image[i*crop_h : (i+1)*crop_h , j*crop_w : (j+1)*crop_w, :] = image
            print()
            k += 1

    cv2.imwrite(f'SPSR_{image_name}', op_image)

if __name__ == '__main__':
    crop_dir = sys.argv[1]
    in_image = sys.argv[2]
    image_h, image_w, _ = cv2.imread(in_image).shape

    stitch_image(crop_dir, image_w, image_h, in_image.split('/')[-1])
