'''
Implementare un generatore di numeri pseudo-casuali che utilizzi il metodo del teorema del limite centrale per generare eventi distribuiti secondo una distribuzione di probabilità gaussiana.

Come si può ottenere una distribuzione normale, cioè una distribuzione gaussiana centrata sullo zero con varianza unitaria?

Verificare visivamente che all'aumentare del numero di eventi aumenta la similarità tra la distribuzione ottenuta e la forma funzionale gaussiana, sia graficamente sia utilizzando i momenti delle distribuzioni calcolati sul campione di eventi generato.
'''

import matplotlib.pyplot as plt
import sys
from library import sturges, rand_TCL
import numpy as np


def controllo_arg() :
    if len(sys.argv) != 4 :
        print("Inserire python3 es4_7.py x_min, x_max ed il numero di numeri N da generare. \n")
        sys.exit()


def main () :
    
    x_min = float(sys.argv[1])
    x_max = float(sys.argv[2])
    N = int(sys.argv[3])
    
    sample = []
    for _ in range (N) :
        sample.append (rand_TCL (x_min, x_max, N))
    
    
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (sample, bins = 'auto', color = 'orange')
    ax.set_title ('Istogramma', size = 14)
    ax.set_xlabel ('x')
    ax.set_ylabel ('y')
    ax.grid ()          #se voglio la griglia
    
    plt.savefig ('grafico es4_7.png')
    plt.show ()
    
if __name__ == '__main__' :
    main ()
