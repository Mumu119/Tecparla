#! /usr/bin/python3

from util import *
from mar import *
from tqdm import tqdm


def evalua(dirRec, dirMar,  *guiSen):
    """
    docstring
    """
    
    matConf = {} # diccionari (matriu)
    lisPal = set() # conjunt de paraules, sense duplicats
    for sen in tqdm(leeLis(*guiSen), ascii="-/🚀\|"):
        pathRec = pathName(dirRec, sen, 'rec')
        reconocido = cogeTRN(pathRec)
        pathMar = pathName(dirMar, sen, 'mar')
        unidad = cogeTRN(pathMar)
        if unidad not in matConf:
            matConf[unidad] = {}
        if reconocido not in matConf[unidad]:
            matConf[unidad][reconocido] = 0
        matConf[unidad][reconocido] += 1
        lisPal = lisPal | {unidad, reconocido}
    for unidad in sorted(lisPal):
        print(f'\t{unidad}', end='') # end = '' perquè no faci salt de línia
    print()

    for unidad in sorted(lisPal):
        print(unidad, end='')
        for reconocido in sorted(lisPal):
            conf = matConf[unidad][reconocido]
            print(f'\t{conf}', end='')
        print()

    correctas = 0
    total = 0 
    for unidad in sorted(lisPal):
        for reconocido in sorted(lisPal):
            total += matConf[unidad][reconocido]
            if unidad == reconocido:
                correctas += matConf[unidad][reconocido]
    print(f'Precisió = {correctas/total:.2%}')

    

if __name__ == '__main__':
    from docopt import docopt
    import sys # el nom del programa sera el primer argument es a dir sys.argv[0], el del primer argument del programa sys.argv[1] i així successivament, en una cadena f tot el que posis en {} es substituirà per el seu valor
    sinopsis = f"""
Evalua el resultado de un experimento de reconoimineto

Usage:
    {sys.argv[0]} [options] <guiSen>... 
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version
    
Opcions:
    --dirRec, -r PATH   Directori amb els fitxers resultants del reconeixement
    --dirMar, -m PATH   Directori amb els fitxers de les marques [default: .]

Arguments:
    <guiSen>...         Llista de fitxers GUI amb els senyals a evaluar
    roollo rolllo rooooooooollloipi
"""

# En atena hi han els apunts on hi han explicaicons de POSIX. Argumento en linea de comandos (es com es diu el fitxer a atenea); Descarregar per casa. 
# Tot el que va despres de usage i una lina en blanc es el que es mostra quan fas --help

    args = docopt(sinopsis, version='Evalua 2024')
    dirRec = args['--dirRec']
    dirMar = args['--dirMar']
    guiSen = args['<guiSen>']

    evalua(dirRec, dirMar, *guiSen) 