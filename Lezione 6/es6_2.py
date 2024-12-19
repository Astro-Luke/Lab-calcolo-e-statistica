'''
Eseguire l'esercizio precedente utilizzando una funzione ricorsiva.

Quale delle due implementazioni è più veloce?
'''

import matplotlib.pyplot as plt
from library import bisezione_ric
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

    x_min = float(sys.argv[1])      # Passo a linea di comando gli argomenti
    x_max = float(sys.argv[2])

    controllo_arg()                 # controllo che siano stati passati correttamente tutti gli argomenti

    t_start = time.time()           # inizio a misurare il tempo
    zero = bisezione_ric(np.cos, x_min, x_max)      # cerco lo zero con la funzione bisezione ricorsiva
    t_end = time.time()             # fermo il tempo
    
    print("Lo zero della funzione si trova nel punto: (",zero,", 0)")
    print(f"Tempo impiegato per eseguire: {(t_end - t_start):.2f} secondi.")    # stampo il tempo impiegato a cercare lo zero
    
    # Creazione ed impostazioni del grafico
    x_axis = np.linspace(x_min, x_max, 100)

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))  # 1 riga, 1 colonna
    axes.plot(x_axis, np.cos(x_axis), label="funzione")   # con esponenziale.pdf uso la funzione predefinita nella libreria scipy
    axes.legend()
    axes.grid()
    axes.set_title("Zero coseno con ricorsione")
    plt.plot(zero, 0., marker="o", color="red")
    plt.savefig("es6_2.png")
    plt.show()
    
if __name__ == '__main__' :
    main ()
