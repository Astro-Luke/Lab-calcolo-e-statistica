'''
Utilizzare due grafici a dispersione per confrontare l'evoluzione della deviazione standard della media calcolata per ogni singolo giocattolo con la deviazione standard del campione di medie al variare del numero di eventi generati in un singolo esperimento con un giocattolo.
'''

import numpy as np
import matplotlib.pyplot as plt
import sys

from library import dev_std_media, rand_range

# ----- Function -----

def controllo_arg() :
    if len(sys.argv) != 3 :
        print("Inserire il nome del file (compresa l'estensione), il numero di eventi ed il numero di esperimenti.\n")
        sys.exit()

# ----- Main -----

def main () :
    
    controllo_arg ()
    
    x_min = -10.
    x_max = 10.
    
    N_evet = int (sys.argv[1])
    N_toy = int (sys.argv[2])
    
    while (N_evet_min < N_evet) :
        lista = []
        single_toy_media = []
        for _ in range (N_toy) :
            val_mean = rand_range(x_min, x_max)
            lista.append(val_mean)
            single_toy_media.append( media (lista))
            
        sigma_single = dev_std_media 
    
    fig, ax = plt.subplots ()
    ax.set_title ('sigma of the means', size=14)
    ax.set_xlabel ('number of events')
    ax.set_ylabel ('sigma of the mean')
    ax.scatter(X, sigmas_of_the_mean, label = 'stddev of the mean')
    ax.plot (N_events, means_sigma, color = 'red', label = 'all toys')
    ax.plot (N_events, sigma_of_the_mean, color = 'blue', label = 'single toy')
    ax.set_xscale ('log')
    ax.legend ()
    ax.grid ()

    plt.savefig ("es8_4.png")
    plt.show ()
    
if __name__ == "__main__" :
    main ()
