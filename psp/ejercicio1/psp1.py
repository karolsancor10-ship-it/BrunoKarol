from PyQt5 import QtDesigner, uic
from load
def __init__(self, xk, listax, listay):
    
    self.xk = xk
    self.listax = listax
    #[13,650,99,150,128,302,95,945,368,961]
    self.listay = listay
    #[186,699,123,272,291,331,199,1890,788,1601]
    self.n = len(self.x)

def calcular(self):
    #SUMATORIA
    sumx = sum(self.x)
    sumy = sum(self.y)
    sumxy = sum(x*y for x, y in zip(self.x, self.y))
    sumx2 = sum(x**2 for x in self.x)
    sumy2 = sum(y**2 for y in self.y)

 # PROMEDIOS
    xavg = sumx / self.n
    yavg = sumy / self.n

    # B1 (pendiente)
    b1 = (sumxy - self.n * xavg * yavg) / (sumx2 - self.n * (xavg**2))

    # B0 (intercepto)
    b0 = yavg - b1 * xavg

    # r (correlación)
    import math
    numerador = (self.n * sumxy) - (sumx * sumy)
    denominador = math.sqrt((self.n * sumx2 - sumx**2) *(self.n * sumy2 - sumy**2))= numerador / denominador

    # r^2
    r2 = r**2

    # Yk (predicción)
    yk = b0 + b1 * self.xk

    return b0, b1, r, r2, y