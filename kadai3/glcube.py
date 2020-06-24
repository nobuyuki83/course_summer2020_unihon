# coding: utf-8
import OpenGL.GL as gl # OpenGLのモジュール
import glfw # GLFWのモジュール（窓を作成したりマウス入力を受け付けるため）
import math

# バッファに回転する立方体を描画する関数
def display(time: float):
  # 立方体の頂点座標のリスト
  aXYZ = [
    [-1., -1., -1.],
    [+1., -1., -1.],
    [-1., +1., -1.],
    [+1., +1., -1.],
    [-1., -1., +1.],
    [+1., -1., +1.],
    [-1., +1., +1.],
    [+1., +1., +1.],
  ]
  # 立方体の面の頂点インデックス
  aQuad = [
    [0, 1, 5, 4],
    [2, 6, 7, 3],
    [0, 2, 3, 1],
    [4, 5, 7, 6],
    [0, 4, 6, 2],
    [1, 3, 7, 5],
  ]
  # 立方体の面の色
  aColorQuad = [
    [1, 0, 0], # 赤
    [0, 1, 0], # 青
    [0, 0, 1], # 緑
    [0, 1, 1], # 黄色
    [1, 0, 1], # シアン
    [1, 1, 0], # 紫
  ]

  gl.glMatrixMode(gl.GL_PROJECTION) # 今から投影行列を指定
  gl.glLoadIdentity() # 単位行列を投影行列に指定
  # 並行投影行列を掛ける．
  gl.glOrtho(-2.0, +2.0, # 画面左端が-2，右端が+2
             -2.0, +2.0, # 画面下端が-2，上端が+2
             -2.0, +2.0) # 画面の奥行き-2~+2までの範囲を描画

  gl.glMatrixMode(gl.GL_MODELVIEW) # 今からモデルビュー行列を指定
  gl.glLoadIdentity() # 単位行列をモデルビュー行列に指定

  '''
  # x軸回りに回転するアフィン変換行列をモデルビュー行列にかける
  gl.glMultMatrixd([
    [1,               0,               0, 0],
    [0, +math.cos(time), -math.sin(time), 0],
    [0, +math.sin(time), +math.cos(time), 0],
    [0,               0,               0, 1] ])
  '''

  # y軸回りに回転するアフィン変換行列をモデルビュー行列にかける
  gl.glMultMatrixd([
    [+math.cos(time), 0, -math.sin(time), 0],
    [              0, 1,               0, 0],
    [+math.sin(time), 0, +math.cos(time), 0],
    [              0, 0,               0, 1]])

  '''
  # z軸回りに回転するアフィン変換行列をモデルビュー行列にかける
  gl.glMultMatrixd([
    [+math.cos(time), -math.sin(time), 0, 0],
    [+math.sin(time), +math.cos(time), 0, 0],
    [              0,               0, 1, 0],
    [              0,               0, 0, 1]])
  '''

  gl.glDisable(gl.GL_LIGHTING) # ライティングの効果を無視します

  gl.glBegin(gl.GL_QUADS) # 今から四角形を描画する
  for iquad, quad in enumerate(aQuad):
    gl.glColor3dv(aColorQuad[iquad]) # 四角形の色を指定
    gl.glVertex3dv(aXYZ[quad[0]]) # 四角形の頂点座標を指定
    gl.glVertex3dv(aXYZ[quad[1]]) # 四角形の頂点座標を指定
    gl.glVertex3dv(aXYZ[quad[2]]) # 四角形の頂点座標を指定
    gl.glVertex3dv(aXYZ[quad[3]]) # 四角形の頂点座標を指定
  gl.glEnd() # 四角形の描画を終える



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

  time = 0.0
  while not glfw.window_should_close(window):   # main loop
    time += 0.01
    gl.glClear( gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT ) # 描画用のバッファを背景色で塗りつぶす
    display(time) # 描画用のバッファに描画する
    glfw.swap_buffers(window) # 描画用のバッファと，表示用のバッファを入れ替えて画面を更新
    glfw.poll_events() # イベントの受けつけ

  glfw.terminate()

if __name__ == "__main__":
  main()