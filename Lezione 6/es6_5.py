'''
Eseguire l'esercizio precedente utilizzando una funzione ricorsiva.

Quale delle due implementazioni è più veloce?
'''

import numpy as np
import matplotlib.pyplot as plt
import time

from library import sezione_aurea_ric_min

# ----- Funzioni -----

def polinomio (x) :
    a = 1.
    b = 7.3
    c = 4.
    return a * (x**2) + b * x + c

def main () :
    
    x_min = -10.
    x_max = 10.
    
    t_start = time.time()
    minimo = sezione_aurea_ric_min(polinomio, x_min, x_max)
    t_end = time.time()
    
    print("Il minimo della funzione è: ", minimo)
    print(f"Tempo impiegato per eseguire: {1000*(t_end - t_start):.6f} millisecondi.")
    
    x_axis = np.linspace(x_min, x_max, 100)
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))  # 1 riga, 1 colonna
    axes.plot(x_axis, polinomio(x_axis), label="funzione")   # con esponenziale.pdf uso la funzione predefinita nella libreria scipy
    axes.legend()
    axes.grid()
    axes.set_title("Minimo funzione polinomio")
    plt.plot(minimo, polinomio(minimo), marker="o", color="red")
    plt.savefig("es6_5.png")
    plt.show()
    
if __name__ == '__main__' :
    main ()

