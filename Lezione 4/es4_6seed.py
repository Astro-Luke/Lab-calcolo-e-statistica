'''
Implementare un generatore di numeri pseudo-casuali che utilizzi il metodo della funzione inversa per generare eventi distribuiti secondo una distribuzione di probabilità esponenziale.

Utilizzare la matplotliblibreria per visualizzare la distribuzione dei numeri generati.
'''

import numpy as np
import matplotlib.pyplot as plt
import sys
import random

from library import rand_range, exp_inversa_seed, sturges

# ----- ----- ----- ----- ----- ----- ----- -----

def controllo_arg() :
    if len(sys.argv) < 4 :
        print("Manca il nome del file da passare a linea di comando.\n")
        sys.exit()

# ----- main -----

def main () :
    
    t = float(sys.argv[1])
    N = int(sys.argv[2])
    seed = float(sys.argv[3])
    
    controllo_arg()
    
    if t <= 0 :
        print("Il parametro t dell'esponenziale deve essere positivo!")
        exit()
    
    x_min = 0.
    x_max = 10.
    
    # imposto il seed
    random.seed(seed)
    
    sample = []
    for _ in range (0, N) :
        sample.append (exp_inversa_seed (t, random.random()) )  # Non c'è bisogno di riscrivere random.seed(seed) poichè è già stato inizializzato, se lo richiamassi qui reinizializzerei il seed ogni volta
    
    Nbin = sturges(N) + 5           # shift a mano
    #print("Numero di bin: ", Nbin)
    
    bin_edges = np.linspace(x_min, x_max, Nbin)
    
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (sample, bins = bin_edges ,color = 'orange')
    ax.set_title ('Istogramma', size = 14)
    ax.set_xlabel ('x')
    ax.set_ylabel ('y')
    ax.grid ()          #se voglio la griglia
    
    plt.savefig ('grafico es4_6.png')
    plt.show ()                             # da mettere rigorosamente dopo il savefig
    
if __name__ == '__main__' :
    main()
