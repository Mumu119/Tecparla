import re

# Serveix per les marques!

def cogeTRN(pathMar):
    #LHD: SAM, 6.0
    #SRC: train/u,337
    #LBO 0, ,511,u
    #ELF:

    reLBO = re.compile(r'LBO:\s*\d*,\s*\d*,\s*\d*,\s*(?P<TRN>.*)')

    with open(pathMar, 'rt') as fpMar:
        for linea in fpMar:
            if (match := reLBO.match(linea)):
                return match['TRN']