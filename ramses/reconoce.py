#! /usr/bin/env python3

import numpy as np
from ramses.util import *
from ramses.prm import *
from euclidio import Euclidi
from tqdm import tqdm
   

def reconoce(dirRec, dirPrm, ficMod, *guiSen):
    # modelos = np.load(ficMod, allow_pickle=True).item() # Carrega el model de la ruta ficMod que es un diccionari per aixó és fa allow_pickle=True. .item() extreu l'element unic de l'array
    modelos = Euclidi(ficMod=ficMod)
    for sen in tqdm(leeLis(*guiSen)):
        pathPrm = pathName(dirPrm, sen, 'prm')
        prm = leePrm(pathPrm)
        reconocida, minDist = modelos(prm)
        pathRec = pathName(dirRec, sen, 'rec')
        chkPathName(pathRec)
        with open(pathRec, 'wt') as fpRec:
            fpRec.write(f'LBO: , , , {reconocida}')


if __name__ == '__main__':
    from docopt import docopt
    import sys # el nom del programa sera el primer argument es a dir sys.argv[0], el del primer argument del programa sys.argv[1] i així successivament, en una cadena f tot el que posis en {} es substituirà per el seu valor
    sinopsis = f"""
Reconeix senyals de veu

Usage:
    {sys.argv[0]} [options] <guiSen>... 
    {sys.argv[0]} -h | --help
    {sys.argv[0]} --version
    
Opcions:
    --dirRec, -r PATH   Directori amb els fitxers resultants del reconeixement
    --dirPrm, -p PATH   Directori amb els fitxers dels senyals parametritzats [default: .]
    --ficMod, -f FILE   Fitxer amb els models de les paraules

Arguments:
    <guiSen>...         Llista de fitxers GUI amb els senyals a evaluar
    roollo rolllo rooooooooollloipi
"""

# En atena hi han els apunts on hi han explicaicons de POSIX. Argumento en linea de comandos (es com es diu el fitxer a atenea); Descarregar per casa. 
# Tot el que va despres de usage i una lina en blanc es el que es mostra quan fas --help

    args = docopt(sinopsis, version='Evalua 2024')
    dirRec = args['--dirRec']
    dirPrm = args['--dirPrm']
    ficMod = args['--ficMod']
    guiSen = args['<guiSen>']

    reconoce(dirRec, dirPrm, ficMod, *guiSen)