'''
Leggi il file di testo eventi_unif.txt:
Calcola la media dei numeri nel file di testo.
Calcola la varianza dei numeri nel file di testo.
Calcola la deviazione standard dei numeri nel file di testo.
Calcola la deviazione standard dalla media dei numeri nel file di testo.
'''

import sys
from math import sqrt           # se facessi solo import math dovrei chiamare ogni volta òa radice con math.sqrt()

def controllo_arg() :
    if len(sys.argv) < 2 :
        print("Manca il nome del file da passare a linea di comando.\n")
        sys.exit()


def media (sample) :
    mean = sum(sample) / len(sample)
    return mean


def varianza (sample) :
    var = 0
    somma_quadrata = 0
    for elem in sample :
        somma_quadrata = somma_quadrata + (elem - media(sample))**2
    var = somma_quadrata / (len(sample))
    return var


def varianza_bessel (sample) :
    var = 0
    somma_quadrata = 0
    for elem in sample :
        somma_quadrata = somma_quadrata + (elem - media(sample))**2
    var = somma_quadrata / (len(sample) -1)
    return var


def dev_std (sample) :
     sigma = sqrt(varianza(sample))
     return sigma


def dev_std_media (sample) :
    deviazione_media = dev_std(sample) / sqrt(len(sample))
    return deviazione_media

# ----- MAIN -----

def main () :

    controllo_arg()

    with open(sys.argv[1]) as file :
        sample = [float(x) for x in file.readlines()]           # Qui il casting è obbligatorio!!!
    print("Numero di elmenti nel file: ", len(sample))
    
    print("La media dl campione è: ", media(sample))
    print("La varianza del campione è: ", varianza(sample))
    print("La deviazione standard del campione è: ", dev_std(sample))
    print("La deviazione standard della media: ", dev_std_media(sample))
    
if __name__ == '__main__' :
    main()
