# coding: utf-8
import OpenGL.GL as gl  # OpenGLのモジュール
import glfw  # GLFWのモジュール（窓を作成したりマウス入力を受け付けるため）
import numpy as np
import math


def draw_mesh(
    npXYZ: np.ndarray,
    npTri: np.ndarray,
    face_color: list) -> None:
  '''
  バッファにメッシュを描画する関数
  :param npXYZ: 頂点のXYZ座標
  :param npTri: 三角形のインデックス
  :param face_color: 面の色
  :return:
  '''

  gl.glDisable(gl.GL_LIGHTING)  # ライティングの効果を無視します

  gl.glColor3dv(face_color)
  gl.glBegin(gl.GL_TRIANGLES)
  for i in range(0, npTri.shape[0]):
    i0, i1, i2 = npTri[i, 0], npTri[i, 1], npTri[i, 2]
    gl.glVertex3d(npXYZ[i0, 0], npXYZ[i0, 1], npXYZ[i0, 2])
    gl.glVertex3d(npXYZ[i1, 0], npXYZ[i1, 1], npXYZ[i1, 2])
    gl.glVertex3d(npXYZ[i2, 0], npXYZ[i2, 1], npXYZ[i2, 2])
  gl.glEnd()

  gl.glColor3d(0, 0, 0)
  gl.glBegin(gl.GL_LINES)
  for i in range(0, npTri.shape[0]):
    i0, i1, i2 = npTri[i, 0], npTri[i, 1], npTri[i, 2]
    gl.glVertex3d(npXYZ[i0, 0], npXYZ[i0, 1], npXYZ[i0, 2])
    gl.glVertex3d(npXYZ[i1, 0], npXYZ[i1, 1], npXYZ[i1, 2])
    gl.glVertex3d(npXYZ[i1, 0], npXYZ[i1, 1], npXYZ[i1, 2])
    gl.glVertex3d(npXYZ[i2, 0], npXYZ[i2, 1], npXYZ[i2, 2])
    gl.glVertex3d(npXYZ[i2, 0], npXYZ[i2, 1], npXYZ[i2, 2])
    gl.glVertex3d(npXYZ[i0, 0], npXYZ[i0, 1], npXYZ[i0, 2])
  gl.glEnd()


def make_unit_cylinder(
    ndiv_circ: int,
    ndiv_length: int) -> tuple:
  '''
  半径１，高さ１の円筒のメッシュをnumpyの配列として作る
  :param ndiv_circ: 円周の分割数
  :param ndiv_length: 円筒の高さの分割数
  :return: None
  '''

  # 円筒の頂点座標
  npXYZ = np.zeros((ndiv_circ * (ndiv_length + 1), 3), dtype=np.float64)
  for j in range(0, ndiv_length + 1): # 長さ方向の分割ループ
    for i in range(0, ndiv_circ): # 円周方向の分割ループ
      npXYZ[j * ndiv_circ + i, 0] = (1.0 / ndiv_length) * j
      npXYZ[j * ndiv_circ + i, 1] = math.cos(math.pi * 2.0 / ndiv_circ * i)
      npXYZ[j * ndiv_circ + i, 2] = math.sin(math.pi * 2.0 / ndiv_circ * i)

  # 円筒の頂点インデックス
  npTri = np.zeros((ndiv_circ * ndiv_length * 2, 3), dtype=np.uint32)
  for j in range(0, ndiv_length): # 長さ方向の分割ループ
    for i in range(0, ndiv_circ): # 円周方向の分割ループ
      npTri[(j * ndiv_circ + i) * 2 + 0, 0] = (j + 0) * ndiv_circ + (i + 0) % ndiv_circ
      npTri[(j * ndiv_circ + i) * 2 + 0, 1] = (j + 0) * ndiv_circ + (i + 1) % ndiv_circ
      npTri[(j * ndiv_circ + i) * 2 + 0, 2] = (j + 1) * ndiv_circ + (i + 0) % ndiv_circ
      npTri[(j * ndiv_circ + i) * 2 + 1, 0] = (j + 1) * ndiv_circ + (i + 1) % ndiv_circ
      npTri[(j * ndiv_circ + i) * 2 + 1, 1] = (j + 1) * ndiv_circ + (i + 0) % ndiv_circ
      npTri[(j * ndiv_circ + i) * 2 + 1, 2] = (j + 0) * ndiv_circ + (i + 1) % ndiv_circ

  return npXYZ, npTri


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

  if not window:  # 窓が作れなかった時の処理
    glfw.terminate()
    raise RuntimeError('Could not create an window')

  glfw.make_context_current(window)

  # OpenGLの情報を表示
  print('Vendor :', gl.glGetString(gl.GL_VENDOR))
  print('GPU :', gl.glGetString(gl.GL_RENDERER))
  print('OpenGL version :', gl.glGetString(gl.GL_VERSION))

  gl.glClearColor(1.0, 1.0, 1.0, 1.0)  # 初期化した時のバッファの色（背景色）の設定
  gl.glEnable(gl.GL_DEPTH_TEST)  # Z-バッファ法による隠面消去を有効にする
  gl.glEnable(gl.GL_POLYGON_OFFSET_FILL)
  gl.glPolygonOffset(1.0, 1.0)

  # 円筒のメッシュを作る
  npXYZ, npTri = make_unit_cylinder(16, 16)  # 長さ方向に１６分割，円周方向に１６分割
  npXYZ[:, 0] = (npXYZ[:, 0] - 0.5) * 3.0 # x方向の長さ３，中心が原点に合わせる
  npXYZ[:, 1:2] *= 0.3 # 半径を0.3にする

  # リグウェイトを作る
  npRig = np.zeros((npXYZ.shape[0], 2), dtype=np.float64)
  npRig[:, 1] = np.tanh(npXYZ[:, 0] * 2) * 0.5 + 0.5
  npRig[:, 0] = 1.0 - npRig[:, 1]

  time = 0.0
  while not glfw.window_should_close(window):  # main loop
    time += 0.01

    # ボーンの回転行列を作る
    theta = math.sin(time)
    npRot = np.zeros((2, 3, 3), dtype=np.float64)
    npRot[0, :, :] = np.eye(3)
    npRot[1, 2, 2] = 1
    npRot[1, 0, 0] = +math.cos(theta)
    npRot[1, 1, 1] = +math.cos(theta)
    npRot[1, 0, 1] = +math.sin(theta)
    npRot[1, 1, 0] = -math.sin(theta)

    # メッシュを変形する
    npXYZ1 = np.zeros_like(npXYZ)
    for ib in range(2):
      npXYZ1[:, :] += npRig[:, ib].reshape(npRig.shape[0], 1) * np.dot(npXYZ, npRot[ib, :, :])

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)  # 描画用のバッファを背景色で塗りつぶす

    gl.glMatrixMode(gl.GL_PROJECTION)  # 今から投影行列を指定
    gl.glLoadIdentity()  # 単位行列を投影行列に指定
    # 並行投影行列を掛ける．
    gl.glOrtho(-2.0, +2.0,  # 画面左端が-2，右端が+2
               -2.0, +2.0,  # 画面下端が-2，上端が+2
               -2.0, +2.0)  # 画面の奥行き-2~+2までの範囲を描画

    gl.glMatrixMode(gl.GL_MODELVIEW)  # 今からモデルビュー行列を指定
    gl.glLoadIdentity()  # 単位行列をモデルビュー行列に指定

    draw_mesh(npXYZ1, npTri, [1, 0, 0])  # メッシュを

    glfw.swap_buffers(window)  # 描画用のバッファと，表示用のバッファを入れ替えて画面を更新
    glfw.poll_events()  # イベントの受けつけ

  glfw.terminate()


if __name__ == "__main__":
  main()
