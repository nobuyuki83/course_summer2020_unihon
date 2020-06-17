
# coding: utf-8

import cv2 as cv2
import numpy as np

if __name__ == "__main__":
	# 画像を読み込む
	img_org = cv2.imread("lena.png")

	# 何もしないフィルタ（３ｘ３）
	kernel_3x3 = np.array([ [ 0,  0,  0],
                            [ 0,  1,  0],
                            [ 0,  0,  0]
                            ], np.float32)

	# フィルタをかける
	img_filter = cv2.filter2D(img_org, ddepth=-1, kernel=kernel_3x3)

	# 画像を表示する
	cv2.imshow("filtered",img_filter)
	cv2.waitKey(0)

	# 画像を保存する
	cv2.imwrite("filtered_0.png",img_filter)

