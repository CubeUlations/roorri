import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

class ParamGeometry:
  def __init__(self, h=0.1, d_alpha=10., n_alpha=36, omega=[1., 1., 1.]):
    self.h = h
    self.d_alpha = d_alpha
    self.n_alpha = n_alpha
    self.omega = np.array(omega)
    self.e = 0.5 * self.omega

  def __str__(self):
    return "".join([str(v)+", " for v in [self.h, self.d_alpha, self.n_alpha, self.omega, self.e]])


class Geometry(ParamGeometry):
  def __init__(self, pb=ParamGeometry()):
    ParamGeometry.__init__(self, pb.h, pb.d_alpha, pb.n_alpha, pb.omega)
    self.pb = pb
    self.n = None
    xm = []
    i = 1
    while i*self.h < self.e[0]:
      xm.append(i*self.h)
      i += 1
    xm = np.array(xm)
    self.x_marks = np.hstack((-xm[::-1], 0, xm))
    alpha_marks = [i * self.d_alpha for i in xrange(self.n_alpha)]
    for i in xrange(self.n_alpha):
      while alpha_marks[i] > 360: alpha_marks[i] -= 360
      while alpha_marks[i] < 0: alpha_marks[i] += 360

    alpha_marks = list(set(alpha_marks)) #unique
    alpha_marks.sort()
    rad_marks = [a*np.pi/180. for a in alpha_marks]
    for i in xrange(len(rad_marks)):
      if rad_marks[i] > np.pi: pass#rad_marks[i] -= 2*np.pi
    self.rad_marks = np.array(rad_marks)
    self.slope_marks = np.array([(np.cos(r), np.sin(r)) for r in rad_marks])
    self.uv_shape = (len(self.x_marks), len(self.rad_marks))
    self.n_points = self.uv_shape[0] * self.uv_shape[1]
    self.n_alpha = self.uv_shape[1]

    self.name = "Empty"



  def __str__(self):
    s = ParamGeometry.__str__(self)
    s = s + "\n"
    s = s + str(self.uv_shape) + ", " + str(self.x_marks) + ", " + str(self.rad_marks) + ", " + str(self.slope_marks)
    return s



