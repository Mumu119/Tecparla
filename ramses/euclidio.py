import numpy as np 
from util import *

class Euclidi:
    def __init__(self, *, lisFon=None, ficMod=None):
        if lisFon and ficMod or not (lisFon or ficMod):
            raise("ERROR: lisFon o ficMod han de ser diferents de None")
        if lisFon:
            self.unidades = leeLis(lisFon)
            self.modelo = {}
        else:
            with open(ficMod, 'rb') as fpMod:
                self.modelo = np.load(fpMod, allow_pickle=True).item()
                self.unidades = self.modelo.keys()
    
    def inicMod(self):
        self.total = {unidad : 0 for unidad in self.unidades}
        self.total2 = {unidad : 0 for unidad in self.unidades}
        self.numFon = {unidad : 0 for unidad in self.unidades}

    def ___add___(self, prm, unidad):
        self.total[unidad] += prm
        self.total2[unidad] += prm ** 2
        self.numFon[unidad] += 1
    
    def recaMod(self):
        distancia = 0 
        for unidad in self.unidades: 
            self.modelo[unidad]= self.total[unidad] / self.numFon[unidad]
            distancia += (self.total2[unidad] / self.numFon[unidad] - self.modelo[unidad] ** 2)
        self.distancia = np.sum(distancia) ** 0.5 

    def printEvo(self):
        print(f'{self.distancia = :.2f}')

    def escMod(self, ficMod):
        chkPathName(ficMod)
        with open(ficMod, 'wb') as fpMod:
            np.save(fpMod, self.modelo)
            
    def __call__(self, prm):
        minDist = np.inf
        for unidad in self.unidades:
            distancia = np.sum((prm - self.modelo[unidad]) ** 2) # Calcula la distancia euclidiana entre el prm i el model
            if distancia < minDist:
                minDist = distancia
                reconocida = unidad
        return reconocida, -minDist
            

