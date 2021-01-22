import cv2

im=cv2.imread("handcraft.jpg")

#edge detection
im_sobel_x= cv2.Sobel(im, cv2.CV_64F, 1, 0, ksize=3)
im_sobel_x= cv2.convertScaleAbs(im_sobel_x)

#histgram equalization
img_yuv= cv2.cvtColor(im, cv2.COLOR_BGR2YUV)
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
im_hist = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

#write the img
cv2.imwrite("edge_hand.jpg", im_sobel_x)
cv2.imwrite("hist.jpg",im_hist)