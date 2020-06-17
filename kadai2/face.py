# coding: utf-8

import cv2 as cv2
import numpy as np

if __name__ == "__main__":

	# 顔の検出クラスを取得
	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

	# 画像を読み込む
	img_org = cv2.imread("group.jpg")

	# グレイスケールモデルに変換
	img_gray = cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)

	cv2.imshow('img_gray',img_gray)
	cv2.waitKey(0)

	# 顔を検出する
	faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

	# facesはNumpy配列で，データはint32型，Nｘ４の２次元配列
	print(type(faces),faces.dtype,faces.shape)

	mask = np.zeros([img_org.shape[0],img_org.shape[1]],dtype=np.float32)

	img_rects = img_org.copy()  # 入力画像の配列を深いコピー
	for (x,y,w,h) in faces:
		# それぞれの検出結果についてimg_orgに青色の四角形を書く
		cv2.rectangle(img_rects,(x,y),(x+w,y+h),(255,0,0),thickness=1) # 太さ１四角形を描画

		# それぞれの検出結果についてmaskに円を書く
		center_position = (int(x+0.5*w),int(y+0.5*h)) # 円の中心
		radius = int((w+h)*0.3) # 円の半径
		cv2.circle(mask,center_position,radius,1.0,thickness=-1) # 塗りつぶしの円を描画


	# 入力画像に四角形などが上書きされた画像を描画
	cv2.imshow('img',img_rects)
	cv2.waitKey(0)

	# マスク画像を描画
	cv2.imshow('img',mask)
	cv2.waitKey(0)

	# 背景画像（単色塗りつぶし）
	back = np.zeros([img_org.shape[0],img_org.shape[1],3],dtype=np.float32)
	back[:,:,0] = 0.5
	back[:,:,1] = 0.8
	back[:,:,2] = 0.7		

	# 前景画像をfloat形式の画像に変換
	front = img_org.astype(np.float32)/255.0

	img_synth = back
	# ここでマスクを使って合成して下さい．

	# 画像をfloatからuint8に変換
	img_synth = (img_synth*255.0).astype(np.uint8)

	# マスク画像を描画
	cv2.imshow('synth',img_synth)
	cv2.waitKey(0)

	cv2.imwrite("detect.png",img_synth)
