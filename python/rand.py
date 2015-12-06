import random

class Gauss:
  def __init__(self, sigma):
    self.sigma = sigma
  def __call__(self, v):
    return random.gauss(v, self.sigma)
