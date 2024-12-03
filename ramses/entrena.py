#! /usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from util import *
from prm import *
from mar import *
from tqdm import tqdm

def entrena(dirPrm, dirMar, lisFon, ficMod, *figGui):
    unidades = leeLis(lisFon)
    total = {unidad : 0 for unidad in unidades} #crea el diccionari amb les vocals i els valors a 0
    numFon = {unidad : 0 for unidad in unidades}
    modelo = {}
    for senyal in tqdm(leeLis(*figGui), ascii="-/|\|"):
        pathMar = pathName(dirMar, senyal, 'mar')
        unidad = cogeTRN(pathMar)
        pathPrm = pathName(dirPrm, senyal, 'prm')
        prm = leePrm(pathPrm)
        total[unidad] += prm
        numFon[unidad] += 1
    for unidad in unidades:
        modelo[unidad] = total[unidad] / numFon[unidad]
    chkPathName(ficMod)
    with open(ficMod, 'wb') as fpMod:
        np.save(fpMod, modelo) # Guarda el model com a diccionari. Si les dades no son nd.array es poden utilitzar de manera maliciosa. Escriu sobre un fitxer binari obert de manera que no afegira el .npy


if __name__ == '__main__':
    from docopt import docopt
    import sys # el nom del programa sera el primer argument es a dir sys.argv[0], el del primer argument del programa sys.argv[1] i així successivament, en una cadena f tot el que posis en {} es substituirà per el seu valor
    sinopsis = f"""
Entrena el reconeixedor de veu

Usage:
    {sys.argv[0]} [options] <figGui>... 
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version
    
Opcions:
    --dirMar, -m PATH   Directori amb els fitxers de marca
    --dirPrm, -p PATH   Directori amb els fitxers dels senyals parametritzats [default: .]
    --lisFon, -l FILE   Fitxer amb la llista de fonemes
    --ficMod, -f FILE   Fitxer amb els models de les paraules

Arguments:
    <figGui>...         Llista de fitxers amb les figures
    roollo rolllo rooooooooollloipi
"""

# En atena hi han els apunts on hi han explicaicons de POSIX. Argumento en linea de comandos (es com es diu el fitxer a atenea); Descarregar per casa. 
# Tot el que va despres de usage i una lina en blanc es el que es mostra quan fas --help

    args = docopt(sinopsis, version='Evalua 2024')
    dirMar = args['--dirMar']
    dirPrm = args['--dirPrm']
    lisFon = args['--lisFon']
    ficMod = args['--ficMod']
    figGui = args['<figGui>']   

    entrena(dirPrm, dirMar, lisFon, ficMod, *figGui)
    
