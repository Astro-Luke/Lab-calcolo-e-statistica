'''
Leggi il file di testo eventi_gauss.txt:

Riempi un istogramma con i primi N numeri contenuti nel file, dove N è un parametro della riga di comando durante l'esecuzione del programma.

Selezionare l'intervallo di definizione dell'istogramma e il suo numero di bin in base ai numeri da rappresentare.
'''

import sys
from math import ceil
import matplotlib.pyplot as plt
import numpy as np

def sturges (N_eventi) :
    return ceil (1 + np.log2 (N_eventi))


def main () :
    
    if len(sys.argv) < 3 :
        print("Mancano degli argomenti da passare a linea di comando.\n")
        sys.exit()
    
    N = int(sys.argv[2])
    
    with open(sys.argv[1]) as file :
        sample = [float(x) for x in file.readlines()]           # Qui il casting è obbligatorio!!!
    print("Numero di elmenti nel file: ", len(sample))
    
    primi_num = sample[:N]
    x_min = min(primi_num)
    x_max = max(primi_num)
    
    Nbin = sturges (N)
    
    bin_edges = np.linspace(x_min, x_max, Nbin)
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (primi_num, bins=bin_edges ,color = 'orange')
    ax.set_title ('Istogramma', size = 14)
    ax.set_xlabel ('x')
    ax.set_ylabel ('y')
    ax.grid ()          #se voglio la griglia
    
    plt.savefig ('grafico es3_3.png')
    plt.show ()                      #da mettere rigorosamente dopo il savefig
    
    
if __name__ == '__main__' :
    main ()
