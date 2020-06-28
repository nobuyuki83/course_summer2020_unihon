# レポート課題１　６月２８日　梅谷担当




- 締め切りは約一ヶ月後です７月２５日（土）２３：５９
- 遅れても減点するだけなので，できるだけ提出してください．
- 技術的な問題で何かつまずいたら（環境構築ができないなど）Slackで教えて下さい



レポートについて説明した回の講義スライド：https://www.dropbox.com/s/nkcdxr43kxlzjtx/lec09_pythonopengla.pdf?dl=0



## 課題の提出方法

- ローカル・レポジトリに移動
  - ローカル・レポジトリが無い場合は[課題１の解説書](../kadai1/readme.md)を参考にしてクローンする

```bash
cd visproc_(ユーザ名)　# レポジトリのトップに移動
```

- report1という名前のブランチを*masterから派生して*作る→課題を開始する
```bash
git checkout master   # マスターブランチに移動
git pull              # リモートのmasterブランチをローカルに反映（コンフリクトがあればそれを解決）
git branch -a         # masterブランチにいることを確認
git branch report1    # masterブランチから派生したreport1というブランチを作成
git checkout report1  # report1ブランチに移動
git branch -a         # report1ブランチにいることを確認
```

- 課題の内容をこなした後にアップロードする
```bash
cd visproc_(ユーザ名)   # レポジトリのトップに移動
git branch -a   # 現在report1というブランチにいることを再確認
git add .       # 変更されたファイルをステージする
git status      # ステージされたファイルを確認する
git commit -m "completed report1"         # 変更をコミットする．コメントはなんでもよい
git push --set-upstream origin report1    # リモートレポジトリのreport1というブランチにプッシュする
```

- ブラウザでプルリクエストを作成　→　６月１２日の授業スライドを参考にして下さい
  
  - プルリクエストは教員が確認してから閉じるので，*勝手に閉じないで*ください．
  
  - プルリクエストは*１つの課題あたりに１つ*開いて下さい（複数開かない）
  
    

***

## 問１：データベースからの取得と平均

New York大学の [Sam Roweis研究室のページ](https://cs.nyu.edu/~roweis/) から，以下の顔画像のデータセットをダウンロードして，このディレクトリに保存します(重いのでGitHubにはアップロードしないで下さい)．

https://cs.nyu.edu/~roweis/data/frey_rawface.jpg

この画像は２０ｘ２８ピクセルのサイズの顔のグレースケール画像がグリッド上に並んでいます．この画像の顔の平均を計算するコードを```pcaface.py```の中に書いて下さい．また平均の顔を以下に貼って下さい

- 平均の顔の画像は```average.png```という名前にしてください．
- ↓↓↓平均の顔を貼り付けて下さい．



- ポイント１：一つ一つの顔を切り出す処理が```pcaface.py```に書いてあるのでよく参考にして下さい．
- ポイント２：平均を取ったりする計算にはデータ形式がnumpy.uint8のような１バイト整数型だとバッファオーバーフローを起こしてしまう恐れがあるので，numpy.float64型などの浮動小数点型を使います．







## 問２：顔の主成分分析

集めた顔に対して主成分分析を行って下さい．第一主成分から第五主成分までをそれぞれ平均画像から加えた時にどのような顔が出てくるのか調べるようなコードを```pcaface.py```の中に書いて下さい．

- 第一次モードから第五モードまでを平均から引いたり足したりした画像を```mode1.png```や```model5.png```のような名前で保存して下さい．まだそれぞれについてどのような顔が得られたのかを記述して下さい．
- ↓↓↓に画像を貼り付けて下さい





- ポイント１：プログラムが正しく実行されていると，面白い，分かりやすい結果が得られるはずです．結果が微妙な時は何かが間違っています．
- ポイント２：numpyの固有値計算で出力される固有値ベクトルの集まった行列ですが，列が固有ベクトルに対応します．





## 問３：データセットの作成

以下の手順で，顔の画像をインターネットから集め，その画像をOpenCVを使って顔を同じサイズに切り出し，切り出した画像から顔の主成分分析を行い，その過程をできるだけ詳しく記述して下さい．

1. url.txtというファイルにflickerなどの画像共有サービスや，google画像検索などを使って集めた画像のurlを書いてこのフォルダに置いて下さい（写真自体は重たいのでレポジトリに加えない）．
2. url.txtに書いてある画像のurlから，画像をダウンロードしてOpenCVを使って顔を検出し，同じサイズに切り出すようなPythonのプログラムを```dataset.py```という名前で書いてこのフォルダに保存して下さい．また画像を問１のように一枚の画像になるように繋げて貼り付けて```dataset.png```という名前にして保存して貼り付けて下さい．
3. 問１，問２と同じく主成分分析を計算するプログラムを書き，結果を表示して議論して下さい．



↓↓↓以下に問３について実験した内容，考察について詳しく書いて下さい．









---





## 参考になるWebサイトなど



主成分分析

- [主成分分析(Wikipedia)](https://ja.wikipedia.org/wiki/主成分分析)
- [主成分分析の考え方(Logics of Blue)](https://logics-of-blue.com/principal-components-analysis/)
- [意味がわかる主成分分析(Qiita)](https://qiita.com/NoriakiOshita/items/460247bb57c22973a5f0)

Numpy

- [Numpyで固有値を計算（numpy.linalg.eig）](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html)
- [NumPyで行列の固有値、固有ベクトルを求めるlinalg.eig関数の使い方](https://deepage.net/features/numpy-eigenvalue-vector.html)

OpenCV

- [Python, OpenCVで顔検出と瞳検出（顔認識、瞳認識）](https://note.nkmk.me/python-opencv-face-detection-haar-cascade/)

Markdown

- [Markdownチートシート](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)



