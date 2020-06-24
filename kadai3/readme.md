# ミニ課題１　６月１８日　梅谷担当３


授業スライド：
- 締め切りは土曜日の夜までです(日曜日に採点したいので)
- 遅れても少し減点するだけなので，できるだけ提出してください．
- 技術的な問題で何かつまずいたら（環境構築ができないなど）Slackで教えて下さい


## 課題の提出方法

- ローカル・レポジトリに移動
  - ローカル・レポジトリが無い場合は[課題１の解説書](../kadai1/readme.md)を参考にしてクローンする

```bash
cd visproc_(ユーザ名)　# レポジトリのトップに移動
```

- kadai2という名前のブランチを*masterから派生して*作る→課題を開始する
```bash
git checkout master   # マスターブランチに移動
git pull              # リモートのmasterブランチをローカルに反映（コンフリクトがあればそれを解決）
git branch -a         # masterブランチにいることを確認
git branch kadai3     # masterブランチから派生したkadai3というブランチを作成
git checkout kadai3   # kadai3ブランチに移動
git branch -a         # kadai3ブランチにいることを確認
```

- 課題の内容をこなした後にアップロードする
```bash
cd visproc_(ユーザ名)   # レポジトリのトップに移動
git branch -a   # 現在kadai3というブランチにいることを再確認→いなければkadai3をチェックアウト
git add .       # 変更されたファイルをステージする
git status      # ステージされたファイルを確認する
git commit -m "completed kadai3"         # 変更をコミットする．コメントはなんでもよい
git push --set-upstream origin kadai3    # リモートレポジトリのkadai3というブランチにプッシュする
```

- ブラウザでプルリクエストを作成　→　６月１２日の授業スライドを参考にして下さい
  
  - プルリクエストは教員が確認してから閉じるので，*勝手に閉じないで*ください．
  
  - プルリクエストは１つの課題あたりに１つ開いて下さい（複数開かない）
  
    

***



## 課題の準備

以下のコマンドで，Python3にOpenGLに関係するモジュールをインストールする．

```bash
pip3 install PyOpenGL
pip3 install glfw
```





---



## 問題１プログラムの実行確認

三次元の立方体を表示するプログラム```glcube.py```を実行して，実行した様子をスクリーンショット画像を撮ってこのドキュメントに貼り付けて下さい．



↓↓↓スクリーンショット画像をここに貼り付ける





## 問題2 ：三次元オブジェクトの回転

現在の```glcube.py```のプログラムは立方体がｙ軸回りに回転します．これを改良して軸```(1,1,1)```の周りに回転するようなプログラムにして下さい．

- ポイント１：三次元物体の回転は４ｘ４のアフィン変換行列を使って記述されます．
- ポイント１：プログラム中の物体のアフィン変換行列を定義している部分を見つけてそれを改変して下さい．
- ポイント２：任意の軸回りのアフィン変換行列は，ロドリゲス回転公式（参考文献やオンライン検索エンジンを参照）を使えば求まります．

---





## 参考になるWebサイトなど

OpenGL
- [Python + GLFW + OpenGL](https://qiita.com/Dhichisutto/items/76ec93c690caf20cedb9)
- [GLUTによる「手抜き」OpenGL入門](https://tokoik.github.io/opengl/libglut.html)
- [モデルビュー変換(OpenGL入門)](http://wisdom.sakura.ne.jp/system/opengl/gl11.html)
- [射影変換(OpenGL入門)](http://wisdom.sakura.ne.jp/system/opengl/gl12.html)
- [Python3で始めるOpenGL4](https://codelabo.com/posts/20200228175104)

ロドリゲスの回転公式

- [ロドリゲスの回転公式]([https://ja.wikipedia.org/wiki/%E3%83%AD%E3%83%89%E3%83%AA%E3%82%B2%E3%82%B9%E3%81%AE%E5%9B%9E%E8%BB%A2%E5%85%AC%E5%BC%8F](https://ja.wikipedia.org/wiki/ロドリゲスの回転公式))

Markdown

- [Markdownチートシート](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)

  



