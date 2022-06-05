import os
import cv2
import numpy as np
from tqdm import tqdm

def Preprocessing(images_in_path, inputs_out_path, outputs_out_path):

    img_names = os.listdir(images_in_path)
    img_paths = [images_in_path + n for n in img_names]
    listed = zip(img_paths, img_names)

    fmat = np.zeros(512)
    fmat[0::3] = 1
    for every in range(3):
        emat = np.zeros(512)
        fmat = np.concatenate((fmat, emat))
    fmat = np.resize(fmat, (512*512))
    fmat = np.reshape(fmat, (512, 512))

    for j, i in tqdm(listed, total=len(img_paths), desc='j-loop'):

        img = cv2.imread(j, 0)

        inv = np.bitwise_not(img)

        height=img.shape[0]
        width =img.shape[1]

        if height > width:
            h=0
            w=(height-width)//2 #Padding both sides to make a square.

        elif height < width:
            h=(width-height)//2 #Padding top and bottom to make a square.
            w=0

        else:
            h=0
            w=0

        padded = cv2.copyMakeBorder(src=img, top=h, bottom=h, left=w, right=w, borderType=cv2.BORDER_CONSTANT, value=0)

        resized = cv2.resize(padded,(512,512))

        thv, denv = cv2.threshold(resized, 25, 255, cv2.THRESH_TOZERO)

        cv2.imwrite(outputs_out_path + i, denv)



        thv, denv = cv2.threshold(denv, 55, 255, cv2.THRESH_TOZERO)
        
        ret,th = cv2.threshold(denv,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        
        fragmented = th * fmat

        cv2.imwrite(inputs_out_path + i, fragmented)



    print('Done preprocessing.')

Data = Preprocessing(images_in_path='/path/to/raw/images/',
                     inputs_out_path='/path/to/preprocessed/input/images/',
                     outputs_out_path='/path/to/preprocessed/output/and/mask/images/')
