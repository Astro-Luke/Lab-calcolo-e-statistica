'''
Scrivi un programma che, dato un numero N_max, generi N_toys esperimenti giocattolo, ciascuno contenente un campione di N_max eventi che seguono una distribuzione scelta, e ne calcoli la media.

Aggiungere al programma precedente un istogramma che visualizzi la distribuzione delle medie tra gli esperimenti giocattolo.
'''

import sys
import matplotlib.pyplot as plt
import numpy as np

from library import media, rand_TAC, sturges

# ----- ----- Funzioni ----- -----

# Funzione di controllo degli argomenti da modificare di volta in volta nel main
def controllo_arg() :
    if len(sys.argv) != 3 :
        print("Inserire il nome del file (compresa l'estensione), numero massimo di numeri pseudocasuali da generare e numero di toy experiment.\n")
        sys.exit()

# ----- ----- Main ----- -----

def main () :
    
    controllo_arg ()
    
    N_max = int(sys.argv[1])
    N_toys = int(sys.argv[2])
    
    x_min = -10.
    x_max = 10.
    y_max = 1.
    
    array_mean = []     # lista che conterrà le medie
    
    for j in range (N_toys) :       # primo ciclo sugli experimenti
        sample = []                 # creo ogni volta una lista per ogni esperimento
        for i in range (N_max) :
            value = rand_TAC (np.sin, x_min, x_max, y_max)
            sample.append(value)                                # riempio la lista
        array_mean.append(media (sample))                       # riempio la lista delle medie con le medie dei singoli sample
    
    Nbin = sturges(N_toys)
    print("Numero di bin generati: ", Nbin)     # è solo un controllo
    
    bin_edges = np.linspace(min(array_mean), max(array_mean), Nbin)         # Regola la dimensione dei bin, come minimo ho preso il minimo dell'array e lo stesso per il massimo
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (array_mean, bins = bin_edges, color = 'orange')
    ax.set_title ('Istogramma delle medie', size = 14)
    ax.set_xlabel ('x')
    ax.set_ylabel ('y')
    ax.grid ()          #se voglio la griglia
    
    plt.savefig ('es8_2.png')
    plt.show ()
    
if __name__ == '__main__' :
    main()
