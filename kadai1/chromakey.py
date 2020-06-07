
import cv2
import numpy as np

if __name__ == "__main__":
	# グリーンバック画像を読み込む
	front0 = cv2.imread("chromakey.jpg")
	# グリーンバック画像を表示
	cv2.imshow("hchromakey",front0)
	cv2.waitKey()

	# 背景画像を読み込む
	back = cv2.imread("campus.jpg")
	# 背景画像を表示
	cv2.imshow("hchromakey",back)
	cv2.waitKey()

	# グリーンバック画像のサイズを背景画像に合わせる
	front1 = cv2.resize(front0,(back.shape[1],back.shape[0]))
	# サイズを一致させたグリーンバック画像を表示
	cv2.imshow("hchromakey",front1)
	cv2.waitKey()

	# グリーンバック画像の配列を，バイトから浮動小数点に変換
	front1 = front1.astype(np.float64)
	# マスクを作成（マスクはブーリアンの配列）
	mask = front1[:,:,1] > 128

	# マスクを表示（ブーリアンの配列をバイトの配列に変換）
	cv2.imshow("hchromakey",mask.astype(np.uint8)*255)
	cv2.waitKey()

	# マスクをブーリアンの配列から浮動小数点の配列に変換
	dmask = mask.astype(np.float64)	
	synb = dmask*back[:,:,0] # 青チャネルの配列をマスク処理
	syng = dmask*back[:,:,1] # 緑チャネルの配列をマスク処理
	synr = dmask*back[:,:,2] # 赤チャネルの配列をマスク処理
	syn = np.stack([synb,syng,synr],axis=2) # 各チャネルを結合

	# 合成結果を表示
	cv2.imshow("hchromakey",syn.astype(np.uint8))
	cv2.waitKey()

	# 合成結果を保存
	cv2.imwrite("synth.png",syn)
