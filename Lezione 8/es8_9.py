'''
Use the hit-or-miss method to estimate the integral underlying a Gaussian probability distribution with μ=0 and σ=1 within a generic interval [a,b].

Calculate the integral contained within the intervals [-kσ, kσ] as k varies from 1 to 5.
'''

import numpy as np

from library import integral_HOM

# ----- ----- Function ----- -----

# funzione gaussiana normalizzata
def gaussiana (x, mean, sigma) :
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ( (x - mean) / sigma )**2)

# ----- ----- main ----- -----

def main () :

    mean = 0.           # parametri della gaussiana
    sigma = 1.

    y_min = 0.              # per la funzione integral_HOM, in questo caso è normalizzata
    y_max = 1.
    N_punti = 100000

    # Funzione gaussiana con mean e sigma fissati
    gaussiana_fixed = lambda x: gaussiana(x, mean, sigma)

    # itero su k tra 1 e 5 (6 è escluso!)
    for k in range (1, 6) :
        integ_value, integ_error = integral_HOM(gaussiana_fixed, -k*sigma, k*sigma, y_min, y_max, N_punti)      # ritorno 2 valori: area ed errore
        print("Valore dell'integrale entro", k, "sigma: ", integ_value, "+/-", integ_error, "\n")
        k = k + 1

if __name__ == "__main__" :
    main ()