'''
Implementare il metodo di integrazione MC grezzo con la funzione di esempio f(x) = sin(x) .

Scrivere l'algoritmo che calcola l'integrale come una funzione esterna al mainprogramma, assicurandosi che accetti come parametri di input i limiti lungo l' asse x e il numero di punti pseudo-casuali da generare.

Assicuratevi che l'algoritmo restituisca un contenitore con due elementi: il primo elemento è il valore dell'integrale, il secondo è la sua incertezza.
'''

import numpy as np

from library import integrale_MonteCarlo

# ----- ----- Main ----- -----

def main () :

    N = 10000
    x_min = 0.
    x_max = np.pi

    value_integral, inc_integral = integrale_MonteCarlo (np.sin, x_min, x_max, N)       # di fatto è tutto qui dentro

    print("L'area dell'integrale è: ", value_integral, "+/-", inc_integral)

if __name__ == "__main__" :
    main ()

