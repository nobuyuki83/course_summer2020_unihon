# ミニ課題５　７月９日　第１１回目（梅谷担当）

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
git branch kadai5     # masterブランチから派生したkadai5というブランチを作成
git checkout kadai5   # kadai5ブランチに移動
git branch -a         # kadai5ブランチにいることを確認
```

- 課題の内容をこなした後にアップロードする
```bash
cd visproc_(ユーザ名)   # レポジトリのトップに移動
git branch -a   # 現在kadai5というブランチにいることを再確認→いなければkadai4をチェックアウト
git add .       # 変更されたファイルをステージする
git status      # ステージされたファイルを確認する
git commit -m "completed kadai5"         # 変更をコミットする．コメントはなんでもよい
git push --set-upstream origin kadai5    # リモートレポジトリのkadai5というブランチにプッシュする
```

- ブラウザでプルリクエストを作成　→　６月１２日の授業スライドを参考にして下さい
  
  - プルリクエストは教員が確認してから閉じるので，*勝手に閉じないで*ください．
  
  - プルリクエストは１つの課題あたりに１つ開いて下さい（複数開かない）
  
    

***



## 課題の準備

もしも，```PyOpenGL```，```glfw```がインストールされていない場合，以下のコマンドでそれぞれインストールする．

```bash
pip3 install PyOpenGL
pip3 install glfw
```

---



## 問題１プログラムの実行確認

立方体を描画する```primitive.py```を実行して，実行した様子をスクリーンショット画像を撮ってこのドキュメントに貼り付けて下さい．

↓↓↓スクリーンショット画像をここに貼り付ける





## 問題2: 円盤の表示

```primitive.py```の９４行目付近を変更して，右側に円盤を表示して下さい．


↓↓↓スクリーンショット画像をここに貼り付ける



- ポイント：円盤の中心と，円周上に点を配置して，それらを結びましょう



## 問題３：球の表示

```primitive.py```の１１７行目付近を変更して，左側に球を表示して下さい．

↓↓↓スクリーンショット画像をここに貼り付ける



- ポイント１：緯度線と経度線の間に等間隔に点を配置しましょう．南極点と北極点の点が重複しないようにしましょう．
- ポイント２：緯度と経度について知らない人はインターネット検索などをして参考にして下さい．



---



## 参考になるWebサイトなど

OpenGL
- [Python + GLFW + OpenGL](https://qiita.com/Dhichisutto/items/76ec93c690caf20cedb9)

Markdown
- [Markdownチートシート](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)

  



