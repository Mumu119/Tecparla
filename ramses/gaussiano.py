import numpy as np 
from util import *
from scipy.stats import multivariate_normal

class Gaussia:
    def __init__(self, *, lisFon=None, ficMod=None):
        if lisFon and ficMod or not (lisFon or ficMod):
            raise("ERROR: lisFon o ficMod han de ser diferents de None")
        if lisFon:
            self.unidades = leeLis(lisFon)
            self.media = {}
            self.varianza = {}
            self.gaussiana = {}
        else:
            with open(ficMod, 'rb') as fpMod:
                self.media = np.load(fpMod, allow_pickle=True).item()
                self.varianza = np.load(fpMod, allow_pickle=True).item()
                self.unidades = self.media.keys()
            self.gaussiana = {}
            for unidad in self.unidades:
                self.gaussiana[unidad] = multivariate_normal(mean=self.media[unidad], cov=self.varianza[unidad], allow_singular=True)
                
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
            self.media[unidad]= self.total[unidad] / self.numFon[unidad]
            self.varianza[unidad] = self.total2[unidad] / self.numFon[unidad] - self.media[unidad] ** 2
            distancia += (self.total2[unidad] / self.numFon[unidad] - self.media[unidad] ** 2)
            print(f'{self.total[unidad]=}')
        self.gaussiana[unidad] = multivariate_normal(mean=self.media[unidad], cov=self.varianza[unidad], allow_singular=True) 

    def printEvo(self):
        print(f'{self.media}')

    def escMod(self, ficMod):
        chkPathName(ficMod)
        with open(ficMod, 'wb') as fpMod:
            np.save(fpMod, self.media)
            np.save(fpMod, self.varianza)
            
    def __call__(self, prm):
        minDist = np.inf
        for unidad in self.unidades:
            probabilidad = self.gaussiana[unidad](prm)
            if probabilidad > maxProb:
                maxProb = probabilidad
                reconocida = unidad
        return reconocida, -minDist

