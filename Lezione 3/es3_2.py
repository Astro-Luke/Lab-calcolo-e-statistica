'''
Leggere il file di testo eventi_unif.txt :

Visualizza sullo schermo i primi 10 elementi positivi.

Conta il numero di eventi contenuti nel file.

Determina i valori minimo e massimo tra i numeri salvati nel file.
'''

import matplotlib.pyplot as plt
import sys
import numpy as np

def controllo_arg() :
    if len(sys.argv) < 2 :
        print("Manca il nome del file da passare a linea di comando.\n")
        sys.exit()

'''
def lettura_file () :
    with open(sys.argv[1]) as file :
        sample = [x for x in file.readlines()]
    print("Elementi nel file: ", len(sample))
'''


#----- MAIN -----

def main() :
    
    # Verifico che siano stati passati tutti gli argomenti
    controllo_arg()

    # Leggo il file
    with open(sys.argv[1]) as file :
        sample = [x for x in file.readlines()]
    print("Elementi nel file: ", len(sample))

    primi = []
    for i in range (0, 10) :
        primi.append(sample[i])
    print("I primi 10 numeri sono: ", primi)

    massimo = max(sample)
    minimo = min(sample)
    
    print("\nMassimo del campione: ", massimo, "\nMinimo del campione: ", minimo)

if __name__ == '__main__' :
    main()
