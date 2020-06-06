
import cv2
import numpy as np

if __name__ == "__main__":
	# 画像を読み込む
	img = cv2.imread("warped.png")

	# 入力画像のサイズを取得
	img_size = (img.shape[1],img.shape[0])

	# ここでアフィン行列を定義してください（現在は単位行列でなにもしていない）
	M = np.float32([[1.0,0.0,0.0],[0.0,1.0,0.0]])

	# 画像を変形する
	dst = cv2.warpAffine(img,M,img_size)

	# 画像を表示する
	cv2.imshow("hoge",dst)
	cv2.waitKey()

	# 画像を保存する
	cv2.imwrite("recovered.png",dst)

