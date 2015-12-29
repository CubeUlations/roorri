from geometry import Geometry
import numpy as np
import rand
from body import Body

DEFAULT_SIGMA = 1e-2

def cuboid(geom=Geometry(), sigma=DEFAULT_SIGMA):
  """(Geometry, float) -> Geometry
  *Description*
  """
  rnd = rand.Gauss(sigma)
  body = Body(geom)
  body.name = "Cuboid"
  p = body.p
  ey = body.e[1]
  ez = body.e[2]
  sy = [1, -1, -1,  1]
  sz = [1,  1, -1, -1]
  rad_bnd = [np.arctan2(sz[i]*ez, sy[i]*ey) for i in range(4)]
  for i in range(4):
    if rad_bnd[i] < 0:
      rad_bnd[i] += 2*np.pi

  for vi in xrange(body.n_alpha):
    rad = body.rad_marks[vi]
    my, mz = body.slope_marks[vi, :]
    quadrant = np.argmax(rad < rad_bnd)
    if quadrant == 0:
      y = ey
      z = ey * mz/my
    elif quadrant == 1:
      y = ez * my/mz
      z = ez
    elif quadrant == 2:
      y = -ey
      z = -ey * mz/my
    elif quadrant == 3:
      y = -ez * my/mz
      z = -ez
    else:
      raise UnboundLocalError
    for ui in xrange(len(body.x_marks)):
      x = body.x_marks[ui]
      x, y, z = rnd(x), rnd(y), rnd(z)
      p[ui, vi] = [x, y, z]
  return body

def ellipsoid(geom=Geometry(), sigma=DEFAULT_SIGMA):
  """(Geometry, float) -> Geometry
  *Description*
  """
  rnd = rand.Gauss(sigma)
  body = Body(geom)
  body.name = "Ellipsoid"
  p = body.p
  ey = body.e[1]
  ez = body.e[2]
  for ui in xrange(len(body.x_marks)):
    x = body.x_marks[ui]
    r = np.sqrt(0.5**2- x**2) #TODO voll falsch, is kugel bisher
    for vi in xrange(body.n_alpha):
      my, mz = body.slope_marks[vi, :]
      y = r*my
      z = r*mz
      x, y, z = rnd(x), rnd(y), rnd(z)
      p[ui, vi] = [x, y, z]
  return body
