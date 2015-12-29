import random

class Gauss:

  def __init__(self, sigma):
    """(Gauss, int) -> NoneType
    *Description*
    """
    self.sigma = sigma

  def __call__(self, v):
    """(Gauss, Type(v)) -> Type(random.gauss(v, self.sigma))
    *Description*
    """
    return random.gauss(v, self.sigma)
