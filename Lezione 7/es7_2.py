'''
Utilizzare il risultato del primo esercizio per simulare un esperimento di conteggio con caratteristiche di Poisson:

Scegliere un tempo caratteristico t_0 per un processo di decadimento radioattivo;

Scegliere un tempo di misura t_M per la finestra di conteggio;

In un ciclo, simulare N pseudo-esperimenti di conteggio, dove, per ciascuno di essi, viene generata una sequenza di eventi casuali con una caratteristica intertemporale dei fenomeni di Poisson, finché il tempo totale trascorso è maggiore del tempo di misurazione, contando il numero di eventi generati che rientrano nell'intervallo.

Compila un istogramma con i conteggi simulati per ciascun esperimento.
'''


import numpy as np
import matplotlib.pyplot as plt
import sys
import random

from library import sturges, rand_pois_new

# ----- ----- Funzioni ----- -----

def controllo_arg() :
    if len(sys.argv) < 2 :
        print("Passare a linea di comando il nome del file (compresa l'estensione) e il numero di eventi da generare.\n")
        sys.exit()
        
# ----- ----- Main ----- -----

def main () :

    controllo_arg()
    
    N = int(sys.argv[1])    # numero di eventi pseudocasuali
    
    t_0 = 3.1       # parametro decadimento
    t_m = 15.       # tempo misura
    
    sample = []
    for _ in range (N) :
        sample.append(rand_pois_new(t_m, t_0))

    Nbin = sturges(N) + 18      # il 18 l'ho messo io a mano 
    
    bin_edges = np.linspace(0., 2*t_m, Nbin)         # Regola la dimensione dei bin e Nbin = numero di bin
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (sample, bins = bin_edges, color = 'orange')  # Spesso conviene usare bins = 'auto' evitando di scrivere la linea di codice con bin_edges, per farlo però bisogna importare numpy
    ax.set_title ('Istogramma poissoniana', size = 14)
    ax.set_xlabel ('t (s)')
    ax.set_ylabel ('Conteggi')
    ax.grid ()          #se voglio la griglia
    
    plt.savefig ('es7_2.png')
    plt.show ()                     #da mettere rigorosamente alla fine
    
if __name__ == "__main__" :
    main ()
