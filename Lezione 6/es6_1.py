'''
Determinare lo zero della funzione g(x) = cos(x) utilizzando il metodo di bisezione nell'intervallo (0, 4).

Quali controlli sono stati omessi nell'implementazione dell'algoritmo descritto nel testo della lezione che potrebbero accelerare il risultato?
'''

import matplotlib.pyplot as plt
from library import bisezione
import numpy as np
import sys
import time

# ----- ----- Funzioni ----- -----

def controllo_arg() :
    if len(sys.argv) != 3 :
        print("Manca il nome del file da passare a linea di comando.\n")
        sys.exit()

# ----- ----- Main ----- -----

def main () :

    x_min = float(sys.argv[1])      # Passaggio argomenti a linea di comando
    x_max = float(sys.argv[2])

    controllo_arg ()                # Controllo che tutti gli argomenti siano stati inseriti
    
    t_start = time.time()           # inizio a misurare il tempo
    zero = bisezione(np.cos, x_min, x_max)      # cerco lo zero con la funzione bisezione
    t_end = time.time()             # fermo il tempo
    
    print("Lo zero della funzione si trova nel punto: (",zero,", 0)")
    print(f"Tempo impiegato per eseguire: {(t_end - t_start):.2f} secondi.")    #Stampa del tempo impiegato a cercare lo zero
    
    
    # Impostazini e creazione grafico
    x_axis = np.linspace(x_min, x_max, 100)
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))  # 1 riga, 1 colonna
    axes.plot(x_axis, np.cos(x_axis), label="funzione")   # con esponenziale.pdf uso la funzione predefinita nella libreria scipy
    axes.legend()
    axes.grid()
    axes.set_title("Zero funzione cos(x)")
    plt.plot(zero, 0., marker="o", color="red")
    plt.savefig("es6_1.png")
    plt.show()
    
if __name__ == '__main__' :
    main ()
