import cv2
import numpy as np

im=cv2.imread("1.jpg")
im= cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

height, width= im.shape[:2]
kernel=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])

def conv(coord, img):
    crop_img=img[coord[1]:coord[1]+3, coord[0]:coord[0]+3].copy()
    output= np.dot(crop_img, kernel)
    total=np.sum(output)
    return total
    
def thred(x, thred= 100):
    if x> thred:
        return 255
    else:
        return 0

pallete = np.zeros((height, width))

for h_i in range(height-2):
    for w_i in range(width-2):
        pallete[h_i,w_i]= thred(conv((w_i,h_i), im))
#write the img
cv2.imwrite("edge.jpg", pallete)
# cv2.imwrite("hist.jpg",im_hist)