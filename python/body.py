import numpy as np
from geometry import Geometry
import matplotlib.pyplot as plt

class Body(Geometry):
  def __init__(self, geom=Geometry()):
    Geometry.__init__(self, geom.pb)
    self.geom = geom
    self.p = self.empty_uv_xyz()
    self.name = "Empty"

  def plot(self):
    p = self.p
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    q = [p[:,:,i].reshape((self.n_points, 1)) for i in range(3)]
    for i in xrange(self.n_points):
      ax.plot(q[0][i], q[1][i], q[2][i], 'o')

  def empty_uv_xyz(self):
    p = np.zeros((self.uv_shape[0], self.uv_shape[1], 3))
    return p
