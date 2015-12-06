import generator
import rand
from geometry import Geometry, ParamGeometry
import normals
from body import Body

import matplotlib.pyplot as plt
import numpy as np

#pb = ParamGeometry(n_alpha=16, d_alpha=22.5, h=0.13)
#pb = ParamGeometry(n_alpha=7, d_alpha=360./7, h=0.23)
pb = ParamGeometry(n_alpha=20, d_alpha=360./55, h=0.085)
geom = Geometry(pb)

sigma = 5e-3

for gen in [generator.cuboid, generator.ellipsoid]:
  body = gen(geom, sigma)
  body.plot()
  print body.name

  for nclass in [normals.Central, normals.Sobel, normals.Scharr]:
    nor = nclass(body)
    print nor.name
    d = nor.dot_n_x
    print max(d), min(d)


plt.show()