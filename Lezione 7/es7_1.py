'''
Generare un campione di numeri pseudo-casuali distribuiti secondo una distribuzione di densità esponenziale con un tempo caratteristico t 0 di 5 secondi.

Visualizzare la distribuzione del campione ottenuto in un istogramma utilizzando il metodo della funzione inversa.

Scrivere tutte le funzioni responsabili della generazione di numeri casuali in una libreria, implementate in file separati dal programma principale.
'''

import matplotlib.pyplot as plt
import sys
import numpy as np

from library import rand_exp_inversa, sturges

# ----- ----- Main ----- -----

def main () :
    
    t = 5.      # tempo caratteristico
    N = 5000         # numero di eventi pseudocasuali da generare
    x_min = 0.
    x_max = 25.
    
    sample = []         # genero la lista che conterrà i numeri pseudocasuali generati
    for _ in range (0, N) :                     # ciclo di riempimento
        sample.append(rand_exp_inversa(t))
    
    # Impostazioni istogramma e creazione
    
    Nbin = sturges(N)                           # (comunque secondo me sta funzione funziona un pò a c***o)
    bin_edges = np.linspace(x_min, x_max, Nbin)         # Regola la dimensione dei bin e Nbin = numero di bin
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (sample, bins = bin_edges ,color = 'orange')  # Da provare anche con bins = 'auto'
    ax.set_title ('Istogramma', size = 14)
    ax.set_xlabel ('x')
    ax.set_ylabel ('y')
    ax.grid ()          #se voglio la griglia
    
    plt.savefig ('es7_1.png')
    plt.show ()                     # da mettere sempre alla fine
    
if __name__ == '__main__' :
    main ()

