import numpy as np

def escPrm(pathPrm, prm):
    """
    Escriu el prm en un fitxer binari
    """

    with open(pathPrm, 'wb') as fpPrm: #si en comptes de 'wb' poses 'ab' o 'wb+' fara un append en comptes de sobreesciure, en la documentació esta tot 
        np.save(fpPrm, prm)

def leePrm(pathPrm):
    """
    Llegeix el prm d'un fitxer binari
    """

    with open(pathPrm, 'rb') as fpPrm:
        return np.load(fpPrm)
