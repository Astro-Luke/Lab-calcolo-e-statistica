'''
Scrivi una pythonlibreria che, dato il nome di un file di testo contenente un campione di eventi come input, sia in grado di leggere il campione e salvarlo in un array numpy, quindi calcolarne la media, la varianza, la deviazione standard, la deviazione standard dalla media, visualizzare il campione in un istogramma con un intervallo di definizione scelto in modo appropriato e un numero di bin. Scrivi un programma di test per la libreria creata.
'''

import sys
from library import controllo_arg, media, varianza, dev_std, dev_std_media
import numpy as np

def main () :
    
    controllo_arg()
    
    with open(sys.argv[1]) as file :
        sample = np.array([float(x) for x in file.readlines()])       # Qui il casting è obbligatorio!!!
    print("Numero di elmenti nel file: ", len(sample))
    
    print("La media è: ", media(sample))
    print("La varianza è: ", varianza(sample))
    print("La deviazione standard è: ", dev_std(sample))
    print("La deviazione standard sulla media è: ", dev_std_media(sample))

if __name__ == '__main__' :
    main()
