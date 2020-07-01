# coding: utf-8
import OpenGL.GL as gl # OpenGLのモジュール
import glfw # GLFWのモジュール（窓を作成したりマウス入力を受け付けるため）
import math
import numpy as np

def display(
  aXY:np.ndarray,
  aColor:np.ndarray):

  gl.glMatrixMode(gl.GL_PROJECTION) # 今から投影行列を指定
  gl.glLoadIdentity() # 単位行列を投影行列に指定
  # 並行投影行列を掛ける．
  gl.glOrtho(-0.5, +1.5, # 画面左端が-0.5，右端が+1.5
             -0.5, +1.5, # 画面下端が-0.5，上端が+1.5
             -0.5, +1.5) # 画面の奥行き-0.5~+1.5までの範囲を描画

  gl.glMatrixMode(gl.GL_MODELVIEW) # 今からモデルビュー行列を指定
  gl.glLoadIdentity() # 単位行列をモデルビュー行列に指定

  gl.glDisable(gl.GL_LIGHTING) # ライティングの効果を無視します

  gl.glPointSize(5)
  gl.glBegin(gl.GL_POINTS) # 今から点を描画する
  for ixy in range(aXY.shape[0]):
    gl.glColor3dv(aColor[ixy]) # 四角形の色を指定
    gl.glVertex2dv(aXY[ixy]) # 四角形の頂点座標を指定
  gl.glEnd() # 四角形の描画を終える

  # 四角形を描く
  gl.glLineWidth(1)
  gl.glColor(0,0,0)
  gl.glBegin(gl.GL_LINE_LOOP)
  gl.glVertex2d(0, 0)
  gl.glVertex2d(1, 0)
  gl.glVertex2d(1, 1)
  gl.glVertex2d(0, 1)
  gl.glEnd()

def main():

  # glfwの初期化
  if not glfw.init():
    raise RuntimeError('Could not initialize GLFW3')

  # OpenGLのバージョンを指定（この授業では古いOpenGLを使います）
  glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 2)
  glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 1)
  glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_ANY_PROFILE)

  # 窓を作る
  window = glfw.create_window(300, 300, 'Program', None, None)  # 窓を作る(幅と高さ，タイトルを指定)

  if not window: # 窓が作れなかった時の処理
    glfw.terminate()
    raise RuntimeError('Could not create an window')

  glfw.make_context_current(window)

  # OpenGLの情報を表示
  print('Vendor :', gl.glGetString(gl.GL_VENDOR))
  print('GPU :', gl.glGetString(gl.GL_RENDERER))
  print('OpenGL version :', gl.glGetString(gl.GL_VERSION))

  gl.glClearColor(1.0, 1.0, 1.0, 1.0) # 初期化した時のバッファの色（背景色）の設定
  gl.glEnable(gl.GL_DEPTH_TEST) # Z-バッファ法による隠面消去を有効にする

  nPoint = 300 # 点の数
  aXY = np.random.uniform(0,1,(nPoint,2)) # 点のXY座標（初期値は0から1までランダム）
  aUV = np.random.uniform(-1,1,(nPoint,2))*4 # 点の速度（初期値は-1から１までランダム）
  aColor = np.random.uniform(0,1,(nPoint,3)) # 点の色（RGBをランダム）
  gravity = np.array([0,-9.8]) # ｙ方向に重力をかける

  dt = 0.01
  while not glfw.window_should_close(window):   # main loop
    # 後退オイラー法 （問２で重力の効果をこの周辺に入れる）
    aXY += dt*aUV # 速度を元に位置を更新

    # 床を反発させる
    mask = aXY[:,1] < 0 # 床を突き抜けた点を抽出
    aXY[mask,1] *= -1 # 床をつき抜けた点の位置を更新
    aUV[mask,1] *= -0.9 # 速度に反発係数をかける

    # 問３で左右の壁や天井も反発させる

    ####
    gl.glClear( gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT ) # 描画用のバッファを背景色で塗りつぶす
    display(aXY,aColor) # 描画用のバッファに描画する
    glfw.swap_buffers(window) # 描画用のバッファと，表示用のバッファを入れ替えて画面を更新
    glfw.poll_events() # イベントの受けつけ

  glfw.terminate()

if __name__ == "__main__":
  main()