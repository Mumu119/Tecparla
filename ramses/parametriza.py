#! /usr/bin/python3


import numpy as np
import soundfile as sf
from util import *
from prm import * # si poses import prm, hauries de posar prm. davant de les funcions de prm.py
from tqdm import tqdm as tqdm # progress bar

def parametriza(dirPrm, dirSen, *guiSen): # *guiSen es una tupla, et longitud variable i sempre s'ha de posar al final. 
    ficheros = leeLis(*guiSen) # sense estarisc li passeries la llista com a un sol valor amb l'esterisc passa cada element com a un valor separat
    for fichero in tqdm(ficheros, ascii="·🚀#", desc="Processing files"): #🚀
        pathSen = pathName(dirSen, fichero, 'wav')
        sen, fm  = sf.read(pathSen)
        rm = sen.copy() # si poses prm = sen, quan canvies prm canvies sen, per això es fa una copia (a diferèrencia de c++ que es fa una espai especific en memoria)
        pathPrm = pathName(dirPrm, fichero, 'prm')
        chkPathName(pathPrm)
        escPrm(pathPrm, rm)


if __name__ == '__main__':
    from docopt import docopt
    import sys # el nom del programa sera el primer argument es a dir sys.argv[0], el del primer argument del programa sys.argv[1] i així successivament, en una cadena f tot el que posis en {} es substituirà per el seu valor
    sinopsis = f"""
Parametriza senyals de veu

Usage:
    {sys.argv[0]} [options] <guiSen>... 
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version
    
Opcions:
    --dirPrm, -p PATH   Directori a els senyals parametrizats
    --dirSen, -s PATH   Directori amb els fitxers dels senyals d'entrada [default: .]


Arguments:
    <guiSen>...         Fitxer guia
    roollo rolllo rooooooooollloipi
"""

# En atena hi han els apunts on hi han explicaicons de POSIX. Argumento en linea de comandos (es com es diu el fitxer a atenea); Descarregar per casa. 
# Tot el que va despres de usage i una lina en blanc es el que es mostra quan fas --help

    args = docopt(sinopsis, version='Evalua 2024')
    dirPrm = args['--dirPrm']
    dirSen = args['--dirSen']
    guiSen = args['<guiSen>']

    parametriza(dirPrm, dirSen, *guiSen) 