# マルチメディア情報処理，梅谷担当分

## 第７回「Pythonを使った画像処理１」

- 日時：6月１２日（木）
- 授業スライド（PDF）：https://www.dropbox.com/s/h4t5aggoad0xn4d/lec07_pythonimage1a.pdf?dl=0
- ミニ課題：[kadai1のフォルダ](kadai1)からお願します．



## 第8回「Pythonを使った画像処理２」

- 日時：6月１８日（木）
- 授業スライド（PDF）：https://www.dropbox.com/s/lop88f1vv5bqbn2/lec08_pythonimage2.pdf?dl=0
- ミニ課題：[kadai2のフォルダ](kadai2)からお願します．



## 第９回「PythonとOpenGL」

- 日時：６月２５日（木）
- 授業スライド(PDF): https://www.dropbox.com/s/q1vo0vxvbn5h6h1/lec09_pythonopengl.pdf?dl=0
- ミニ課題：[kadai3のフォルダ](kadai3/readme.md)からお願いします．




## レポート課題１：「画像の統計的処理」

- 出題日：６月２８日（日）
- 〆切：７月２５日（土）２３時５９分
- [report1のフォルダ](report1) からお願いします．



## 第１０回「物理シミュレーションの基礎」

- 日時：７月２日（木）
- 授業スライド(PDF): https://www.dropbox.com/s/5n7dmaopm6qhsxb/lec10_physicssim.pptx?dl=0
- ミニ課題：[kadai4のフォルダ](kadai4)からお願いします．



## 第１１回「キャラクターアニメーション」

- 日時：７月９日（木）
- ミニ課題：[kadai5のフォルダ](kadai5)からお願いします．



## 第１３回「キャラクターアニメーション２」

- 日時：７月23日（木）
- ミニ課題：[kadai6のフォルダ](kadai6)からお願いします．



***

## トラブルシューティング

- pythonを実行した時に```ModuleNotFoundError: No Module named'cv2'```というエラーが出る
  - 以下のコマンドを実行してpython3にopencvのモジュールをインストール

```bash
pip3 install opencv-python
```



- 上の手順に従ってOpenCVなどのモジュールをインストールしたのにまだもモジュールが無いと言われる
  - python2にOpenCVをインストールしている可能性→```pip3```を使ってインストール
  - python2でプログラムを実行している→```python3```でプログラムを実行



- markdownドキュメントをローカル環境でプレビューしながら編集したい
  - Visual Studio Code，PyCharmなどの統合開発環境
  - Typoraなどのmarkdownエディタを使う



- git cloneした時に，```Repository not found```などというエラーが出る．GitHubのレポジトリのページは見ることができる．
  - 複数のGitHubアカウントを持っているが認証情報が共有されていないのが原因
  - GitHub公式デスクトップアプリを使えばclone&pushできる？[GitHub Desktop](https://desktop.github.com/)
  - 記事を参考にする
    - [https時代のgitアカウントを使い分ける](https://qiita.com/1natsu172/items/a4a3357a0481440ec6a5)
    - [GitHubでssh接続する手順〜公開鍵の生成から〜](https://qiita.com/shizuma/items/2b2f873a0034839e47ce)

