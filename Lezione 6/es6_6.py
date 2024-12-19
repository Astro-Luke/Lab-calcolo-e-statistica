'''
Completa i due esercizi precedenti trovando il massimo di una funzione scelta.
'''

import numpy as np
import matplotlib.pyplot as plt
import time

from library import sezione_aurea_max

# ----- Funzioni -----

def function (x) :
    return np.exp(-x**2)

def main () :
    
    x_min = -5.
    x_max = 5.
    
    t_start = time.time()
    massimo = sezione_aurea_max(function, x_min, x_max)
    t_end = time.time()
    
    print("Il massimo della funzione è: ", massimo)
    print(f"Tempo impiegato per eseguire: {1000*(t_end - t_start):.6f} millisecondi.")
    
    x_axis = np.linspace(x_min, x_max, 100)
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))  # 1 riga, 1 colonna
    axes.plot(x_axis, function(x_axis), label = "funzione")   # con esponenziale.pdf uso la funzione predefinita nella libreria scipy
    axes.legend()
    axes.grid()
    axes.set_title("Massimo funzione e^(-x^2)")
    plt.plot(massimo, function(massimo), marker="o", color="red")
    plt.savefig("es6_6.png")
    plt.show()
    
if __name__ == '__main__' :
    main ()

