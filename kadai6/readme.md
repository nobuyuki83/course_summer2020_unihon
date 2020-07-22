# ミニ課題6　７月23日　第13回目（梅谷担当）

- 締め切りは土曜日の夜までです(日曜日に採点したいので)
- 遅れても少し減点するだけなので，できるだけ提出してください．
- 技術的な問題で何かつまずいたら（環境構築ができないなど）Slackで教えて下さい



## 課題の提出方法

- ローカル・レポジトリに移動
  - ローカル・レポジトリが無い場合は[課題１の解説書](../kadai1/readme.md)を参考にしてクローンする

```bash
cd visproc_(ユーザ名)　# レポジトリのトップに移動
```

- kadai5という名前のブランチを*masterから派生して*作る→課題を開始する
```bash
git checkout master   # マスターブランチに移動
git pull              # リモートのmasterブランチをローカルに反映（コンフリクトがあればそれを解決）
git branch -a         # masterブランチにいることを確認
git branch kadai6     # masterブランチから派生したkadai6というブランチを作成
git checkout kadai6   # kadai6ブランチに移動
git branch -a         # kadai6ブランチにいることを確認
```

- 課題の内容をこなした後にアップロードする
```bash
cd visproc_(ユーザ名)   # レポジトリのトップに移動
git branch -a   # 現在kadai5というブランチにいることを再確認→いなければkadai4をチェックアウト
git add .       # 変更されたファイルをステージする
git status      # ステージされたファイルを確認する
git commit -m "completed kadai6"         # 変更をコミットする．コメントはなんでもよい
git push --set-upstream origin kadai6    # リモートレポジトリのkadai5というブランチにプッシュする
```

- ブラウザでプルリクエストを作成　→　６月１２日の授業スライドを参考にして下さい
  
  - プルリクエストは教員が確認してから閉じるので，*勝手に閉じないで*ください．
  
  - プルリクエストは１つの課題あたりに１つ開いて下さい（複数開かない）
  
    

***



## 課題の準備

もしも，```numpy```, ```PyOpenGL```，```glfw```がインストールされていない場合，以下のコマンドでそれぞれインストールする．

```bash
pip3 install numpy
pip3 install PyOpenGL
pip3 install glfw
```

---



## 問題１プログラムの実行確認

線形ブレンドスキニング```rigging.py```を実行して，実行した様子をスクリーンショット画像を撮ってこのドキュメントに貼り付けて下さい．

↓↓↓スクリーンショット画像をここに貼り付ける





## 問題2: プログラムの説明

```rigging.py```の130行目付近の以下のプログラムについて,どういう処理をしているのか言葉で説明せよ.
変数の意味や，その変数がどのように使われているかなど，できるだけ詳しく説明して下さい．

```python
    for ib in range(2):
      npXYZ1[:, :] += npRig[:, ib].reshape(npRig.shape[0], 1) * np.dot(npXYZ, npRot[ib, :, :])
```

↓↓↓以下に説明を加える



## 問題３：ボーンの回転

```rigging.py```の120行目付近を変更して，円筒の左側が，右側に合わせて左右対称に変形するようにせよ．
またスクリーンショットをとってこのドキュメントに貼り付けよ．

↓↓↓スクリーンショット画像をここに貼り付ける





---



## 参考になるWebサイトなど

OpenGL
- [Python + GLFW + OpenGL](https://qiita.com/Dhichisutto/items/76ec93c690caf20cedb9)

Markdown
- [Markdownチートシート](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)

線形ブレンドスキニング
- [Linear Blend Skinning](https://www.pixelfondue.com/blog/2017/10/27/how-it-works-linear-blend-skinning)
- [スケルタルアニメーション (Wikipedia)](https://ja.wikipedia.org/wiki/%E3%82%B9%E3%82%B1%E3%83%AB%E3%82%BF%E3%83%AB%E3%82%A2%E3%83%8B%E3%83%A1%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3)  



