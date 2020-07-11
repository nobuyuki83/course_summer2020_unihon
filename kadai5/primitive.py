# coding: utf-8
import OpenGL.GL as gl # OpenGLのモジュール
import glfw # GLFWのモジュール（窓を作成したりマウス入力を受け付けるため）
import math

def draw_mesh(aXYZ:list, aTri:list, face_color:list):
  '''
  バッファにメッシュを描画する関数
  :param aXYZ: 頂点のXYZ座標
  :param aTri: 三角形のインデックス
  :param face_color: 面の色
  :return:
  '''

  gl.glDisable(gl.GL_LIGHTING) # ライティングの効果を無視します

  # メッシュの面を描画
  gl.glColor3d(*face_color)
  gl.glBegin(gl.GL_TRIANGLES) # 今から三角形を描画する
  for tri in aTri:
    gl.glVertex3dv(aXYZ[tri[0]]) # 三角形の頂点座標を指定
    gl.glVertex3dv(aXYZ[tri[1]]) # 三角形の頂点座標を指定
    gl.glVertex3dv(aXYZ[tri[2]]) # 三角形の頂点座標を指定
  gl.glEnd() # 面の描画を終える

  # メッシュの辺を描画
  gl.glColor3d(0,0,0)
  gl.glBegin(gl.GL_LINES) # 今から線を描画する
  for tri in aTri:
    gl.glVertex3dv(aXYZ[tri[0]]) # 三角形の頂点座標を指定
    gl.glVertex3dv(aXYZ[tri[1]]) # 三角形の頂点座標を指定
    gl.glVertex3dv(aXYZ[tri[1]]) # 三角形の頂点座標を指定
    gl.glVertex3dv(aXYZ[tri[2]]) # 三角形の頂点座標を指定
    gl.glVertex3dv(aXYZ[tri[2]]) # 三角形の頂点座標を指定
    gl.glVertex3dv(aXYZ[tri[0]]) # 三角形の頂点座標を指定
  gl.glEnd() # 線の描画を終える


def draw_cube(
    edge_length: float,
    position: list,
    face_color):
  '''
  立方体を描画する
  :param edge_length: 辺の長さ
  :param position: 中心の三次元座標
  :param face_color: 面の色
  :return: None
  '''

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
  for xyz in aXYZ:
    xyz[0] = xyz[0]*0.5*edge_length + position[0]
    xyz[1] = xyz[1]*0.5*edge_length + position[1]
    xyz[2] = xyz[2]*0.5*edge_length + position[2]

  # 立方体の三角形の頂点インデックス
  aTri = [
    [0, 1, 5], [0, 5, 4],
    [2, 6, 7], [2, 7, 3],
    [0, 2, 3], [0, 3, 1],
    [4, 5, 7], [4, 7, 6],
    [0, 4, 6], [0, 6, 2],
    [1, 3, 7], [1, 7, 5]
  ]
  draw_mesh(aXYZ, aTri, face_color)


def draw_disc_normalZ(
    radius:float,
    position: list,
    ndiv_circumference: int,
    face_color):

  '''
  Z軸が法線の円盤を描画する
  :param radius: 半径
  :param ndiv_circumference:　円周の分割数
  :param face_color: 面の色
  :return: None
  '''

  # 問２では以下をプログラミングする
  aXYZ = [] # ３次元座標のリスト
  aTri = [] # 三角形のインデックス
  draw_mesh(aXYZ, aTri, face_color)


def draw_sphere(
    radius: float,
    position: list,
    ndiv_latitude:int,
    ndiv_longtitude:int,
    face_color: list):

  '''
  球を描画する
  :param radius: 半径
  :param position: 三次元座標
  :param ndiv_latitude: 緯度の分割数
  :param ndiv_longtitude: 経度の分割数
  :param face_color: 面の色
  :return:
  '''

  # 問３では以下をプログラミングする
  aXYZ = [] # ３次元座標のリスト
  aTri = [] # 三角形のインデックス
  draw_mesh(aXYZ, aTri, face_color)


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

    gl.glMatrixMode(gl.GL_PROJECTION)  # 今から投影行列を指定
    gl.glLoadIdentity()  # 単位行列を投影行列に指定
    # 並行投影行列を掛ける．
    gl.glOrtho(-2.0, +2.0,  # 画面左端が-2，右端が+2
               -2.0, +2.0,  # 画面下端が-2，上端が+2
               -2.0, +2.0)  # 画面の奥行き-2~+2までの範囲を描画

    gl.glMatrixMode(gl.GL_MODELVIEW)  # 今からモデルビュー行列を指定
    gl.glLoadIdentity()  # 単位行列をモデルビュー行列に指定

    # [0,0,0]の位置に辺の長さ1の立方体を描画
    draw_cube(edge_length=1,position=[0,0,0], face_color=[1,0,0])

    # [1,0,0]の位置に半径0.5の円を描画 -> 問２
    draw_disc_normalZ(radius=0.5,position=[1,0,0],ndiv_circumference=32, face_color=[0,1,0])

    # [-1,0,0]の位置に半径0.5の球を描画 -> 問３
    draw_sphere(radius=0.5,position=[-1,0,0],ndiv_latitude=32,ndiv_longtitude=32, face_color=[0,0,1])

    glfw.swap_buffers(window) # 描画用のバッファと，表示用のバッファを入れ替えて画面を更新
    glfw.poll_events() # イベントの受けつけ

  glfw.terminate()

if __name__ == "__main__":
  main()