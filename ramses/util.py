from pathlib import Path

def leeLis(*ficLis):
    lista = []

    for fichero in ficLis:
        with open(fichero, 'rt') as fpLis: #Per defecte en py sempre es read text (rt)
            lista += (palabra.strip() for palabra in fpLis) #.strip() treu el retorn de carro final 
    return lista 


def pathName(dir, nom, ext):
    """
    bla, bla, bla...
    """
    return dir + '/' + nom + '.' + ext 


def chkPathName(path):
    """
    bla, bla, bla...
    """

    Path(path).parent.mkdir(parents=True, exist_ok=True)   #parent = dir raiz mkdir, crea directori, parents = true (crea els pares si fa falta 'pare/fill/net?')  exist_ok (si ja existeix el crea igualment)
    
