import pywt
import numpy as np
import matplotlib.pyplot as plt
import random
import cv2
import os 

def channelTransform(ch1,ch2, shape):
    cooef1 = pywt.dwt2(ch1, 'db5', mode = 'periodization')
    cooef2 = pywt.dwt2(ch2, 'db5', mode = 'periodization')
    cA1, (cH1, cV1, cD1) = cooef1
    cA2, (cH2, cV2, cD2) = cooef2

    cA = (cA1+cA2)/2
    cH = (cH1 +cH2)/2
    cV = (cV1+cV2)/2
    cD = (cD1+cD2)/2
    fincoC = cA, (cH,cV,cD)
    outImageC = pywt.idwt2(fincoC, 'db5', mode = 'periodization')
    outImageC = cv2.resize(outImageC,(shape[0],shape[1])) 
    return outImageC

def fusion(img1, img2,imagename):
    # Params
    FUSION_METHOD = 'mean' # Can be 'min' || 'max || anything you choose according theory

    # Read the two image
    I1 = cv2.imread(img1)
    I2 = cv2.imread(img2)

    # Resizing image if both are in different shapes
    I2 = cv2.resize(I2,(I1.shape[1],I1.shape[0])) 
    
    #print (I1.shape)
    #print (I2.shape)
    ## Seperating channels
    iR1 = I1.copy()
    iR1[:,:,1] = iR1[:,:,2] = 0
    iR2 = I2.copy()
    iR2[:,:,1] = iR2[:,:,2] = 0

    iG1 = I1.copy()
    iG1[:,:,0] = iG1[:,:,2] = 0
    iG2 = I2.copy()
    iG2[:,:,0] = iG2[:,:,2] = 0

    iB1 = I1.copy()
    iB1[:,:,0] = iB1[:,:,1] = 0
    iB2 = I2.copy()
    iB2[:,:,0] = iB2[:,:,1] = 0

    shape = (I1.shape[1], I1.shape[0])
    # Wavelet transformation on red channel
    outImageR = channelTransform(iR1, iR2, shape)
    outImageG = channelTransform(iG1, iG2, shape)
    outImageB = channelTransform(iB1, iB2, shape)

    outImage = I1.copy()
    outImage[:,:,0] = outImage[:,:,1] = outImage[:,:,2] = 0
    outImage[:,:,0] = outImageR[:,:,0]
    outImage[:,:,1] = outImageG[:,:,1]
    outImage[:,:,2] = outImageB[:,:,2] 

    outImage = np.multiply(np.divide(outImage - np.min(outImage),(np.max(outImage) - np.min(outImage))),255)
    outImage = outImage.astype(np.uint8)
    #print(outImage)
    
    loc = 'final_fused_image/child/control/'+imagename
    cv2.imwrite(loc,outImage)
    #print(loc)

    return loc



print('starting fusion...')
def fuse_all(folder_path_1,folder_path_2):
    
    image_1_list=os.listdir(folder_path_1)
    image_2_list=os.listdir(folder_path_2)
    for i in range(len(image_2_list)):
        if image_2_list[i] in image_1_list:
            image_1_path=folder_path_1+image_1_list[i]
            image_2_path=folder_path_2+image_2_list[i]
            

            fusion(image_1_path,image_2_path,image_2_list[i])

            
            
    







folder_path_1='D:/mamtadiproject/data/Child 2-10/sMRI - bkp/Control/'
folder_path_2='D:/mamtadiproject/data/Child 2-10/fMRI - bkp/Control/'
fuse_all(folder_path_1,folder_path_2)

print()
print()
print()
print('**********')
print()
print("fusion done successfully")
print()
print()
print('**********')