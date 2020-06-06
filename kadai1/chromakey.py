
import cv2
import numpy as np

if __name__ == "__main__":
	img0 = cv2.imread("chromakey.jpg")
	cv2.imshow("hchromakey",img0)
	cv2.waitKey()

	img1 = cv2.imread("campus.jpg")
	cv2.imshow("hchromakey",img1)
	cv2.waitKey()

