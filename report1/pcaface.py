# coding: utf-8
import cv2.cv2 as cv2
import numpy as np
import math

def main():

  # https://cs.nyu.edu/~roweis/data/frey_rawface.jpg　からダウンロードすること
  img_input = cv2.imread("frey_rawface.jpg")

  # 顔を画像として表示
  cv2.imshow("input",img_input)
  cv2.waitKey(0)

  # 顔を動画として表示
  for ix in range(43):
    for iy in range(45):
      img0 = img_input[(iy+0)*29:(iy+1)*29, (ix+0)*21:(ix+1)*21, :] # Numpyのスライシングの機能を用いて切り出す
      cv2.imshow("input", img0)
      cv2.waitKey(1) # 1msの待ち時間

  # ここで平均を計算
  avg = np.zeros((29,21,3),dtype=np.float64) 
  # ここにコードを書く

  # ここで平均をファイルに保存


  # 平均からの差を集めた行列を作る
  Amat = np.zeros( (nface,21*29),dtype=np.float64 )
  # ここにコードを書く


  # 共分散行列を作る
  # ここにコードを書く


  # 共分散行列の固有ベクトルを計算
  # ここにコードを書く


  # 共分散行列の固有ベクトル＋平均画像を表示
  # ここにコードを書く  


if __name__ == "__main__":
  main()

