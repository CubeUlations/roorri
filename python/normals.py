import numpy as np

class Normal:
  def __init__(self, kernel, body):
    self.filter_x = kernel[0]
    self.filter_y = kernel[1]
    self.body = body
    self.name = kernel[2]
    self.n = self.folding(body.p)
    self.dot_n_x = self.dot_normal_x0()

  def folding(self, p):
    body = self.body
    n = body.empty_uv_xyz()
    kernel_x, kernel_y = self.filter_x, self.filter_y
    for ui in xrange(1, body.uv_shape[0] - 1):
      for vi in xrange(1, body.uv_shape[1] - 1):
        p_e =  p[ui+1, vi,   :]
        p_w =  p[ui-1, vi,   :]
        p_c  = p[ui  , vi,   :]
        p_n =  p[ui,   vi+1, :]
        p_s =  p[ui,   vi-1, :]
        p_ne = p[ui+1, vi+1, :]
        p_nw = p[ui-1, vi+1, :]
        p_se = p[ui+1, vi-1, :]
        p_sw = p[ui-1, vi-1, :]
        P = [
          p_nw, p_n, p_ne,
          p_w,  p_c, p_e,
          p_sw, p_s, p_se,
        ]

        pu = sum([P[i] * kernel_x[i] for i in range(9)])
        pv = sum([P[i] * kernel_y[i] for i in range(9)])
        m = np.cross(pu, pv)
        m /= np.linalg.norm(m)
        n[ui, vi, :] = -m
    return n

  def dot_normal_x0(self):
    p = self.body.p
    n = self.n
    d = []
    for ui in xrange(1, self.body.uv_shape[0] - 1):
      for vi in xrange(1, self.body.uv_shape[1] - 1):
        ni = n[ui, vi, :]
        pi = p[ui, vi, :]
        qi = pi / np.linalg.norm(pi)
        d.append(-np.dot(ni, qi))
    return d


class Central(Normal):
  def __init__(self, body):
    CENTRAL = (
      [
      0,  0, 0,
      -1, 0, 1,
      0,  0, 0
      ], [
      0, -1, 0,
      0,  0, 0,
      0,  1, 0
      ], "central"
    )
    Normal.__init__(self, CENTRAL, body)


class Sobel(Normal):
  def __init__(self, body):
    SOBEL= (
      [
      -1, 0, 1,
      -2, 0, 2,
      -1, 0, 1
      ], [
      -1, -2, -1,
       0,  0,  0,
       1,  2,  1
      ], "sobel"
    )
    Normal.__init__(self, SOBEL, body)

class Scharr(Normal):
  def __init__(self, body):
    SCHARR = (
      [
      -3,  0,  3,
      -10, 0, 10,
      -3,  0,  3
      ], [
      -3, -10, -3,
       0,   0,  0,
       3,  10,  3
      ], "scharr"
    )
    Normal.__init__(self, SCHARR, body)


def sobel(body):
  n = body.empty_uv_xyz()
  p = body.p
  for ui in xrange(1, body.uv_shape[0] - 1):
    for vi in xrange(1, body.uv_shape[1] - 1):
      p_c  = p[ui  , vi,   :]
      p_e  = p[ui+1, vi,   :]
      p_w  = p[ui-1, vi,   :]
      p_n  = p[ui,   vi+1, :]
      p_s  = p[ui,   vi-1, :]
      p_ne = p[ui+1, vi+1, :]
      p_nw = p[ui-1, vi+1, :]
      p_se = p[ui+1, vi-1, :]
      p_sw = p[ui-1, vi-1, :]

      P = [
        p_nw, p_n, p_ne,
        p_w,  p_c, p_e,
        p_sw, p_s, p_se,
      ]

      pu = sum([P[i] * SOBEL_X[i] for i in range(9)])
      pv = sum([P[i] * SOBEL_Y[i] for i in range(9)])
      m = np.cross(pu, pv)
      m /= np.linalg.norm(m)
      n[ui, vi, :] = -m
  return n

def central(body):
  n = body.empty_uv_xyz()
  p = body.p
  for ui in xrange(1, body.uv_shape[0] - 1):
    for vi in xrange(1, body.uv_shape[1] - 1):
      p_e = p[ui+1, vi, :]
      p_w = p[ui-1, vi, :]
      p_n = p[ui, vi+1, :]
      p_s = p[ui, vi-1, :]
      pu = p_w - p_e
      pv = p_s - p_n
      m = np.cross(pu, pv)
      m /= np.linalg.norm(m)
      n[ui, vi, :] = m
  return n


def dot_normal_x0(body, n):
  p = body.p
  d = []
  for ui in xrange(1, body.uv_shape[0] - 1):
    for vi in xrange(1, body.uv_shape[1] - 1):
      ni = n[ui, vi, :]
      pi = p[ui, vi, :]
      qi = pi / np.linalg.norm(pi)
      d.append(-np.dot(ni, qi))
  return d

def structure_tensor(body, n):
  p = body.p
  e = []
  for ui in xrange(1, body.uv_shape[0] - 1):
    for vi in xrange(1, body.uv_shape[1] - 1):
      pass
