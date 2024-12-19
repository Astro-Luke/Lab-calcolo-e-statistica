'''
Implementare un generatore di numeri pseudo-casuali che utilizzi il metodo try-and-catch per generare numeri pseudo-casuali in base a una distribuzione di probabilità arbitraria.

Prendiamo la funzione di densità di probabilità (pdf) come parametro di input per generare numeri casuali.

Utilizzare la matplotliblibreria per visualizzare la distribuzione dei numeri generati.
'''

import sys
import numpy as np
from library import rand_range, rand_TAC_norm, sturges, seed_range
from scipy.stats import norm
import matplotlib.pyplot as plt
from math import floor


def controllo_arg() :
    if len(sys.argv) < 4 :
        print("Mancano degli argomenti da inserie a riga di comando.\nInserisci x_min, x_max ed N (numero di elementi da generare).")
        sys.exit()


def main () :
    
    x_min = float(sys.argv[1])
    x_max = float(sys.argv[2])
    N = int(sys.argv[3])
    seed = float(sys.argv[4])
    
    loc = 0.
    scale = 1.
    y_max = 1/(2*np.pi)
    
    #sample = seed_range (x_min, x_max, N, seed)
    
    sample = []
    for _ in range (0, N) :
        x = rand_TAC_norm (norm.pdf, x_min, x_max, y_max, loc, scale)
        sample.append(x)
    
    Nbins = sturges (N) + 20     # shift a mano (mio)
    #Nbins = floor (len (sample) / 20.) + 1        # prof
    
    bin_edges = np.linspace(x_min, x_max, Nbins)         # regola la dimensione dei bin e Nbin = numero di bin
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (sample, bins = bin_edges, color = 'orange')
    ax.set_title ('Eventi con TAC', size = 14)
    ax.set_xlabel ('x')
    ax.set_ylabel ('y')
    ax.grid ()          #se voglio la griglia
    
    plt.savefig ('es4_5.png')
    plt.show ()
    
    
if __name__ == '__main__' :
    main ()
