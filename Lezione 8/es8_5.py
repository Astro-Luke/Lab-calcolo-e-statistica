'''
Si implementi il metodo di integrazione hit-or-miss
con la funzione di esempio *f(x) = sin (x)*.
  * Si scriva l'algoritmo che calcola l'integrale come una funzione esterna al programma ```main```,
    facendo in modo che prenda come parametri di ingresso,
    oltre agli estremi lungo l'asse *x* e l'asse *y*,
    anche il numero di punti pseudo-casuali da generare.
  * Si faccia in modo che l'algoritmo ritorni due elementi:
    il primo elemento sia il valore dell'integrale,
    il secondo sia la sua incertezza.
'''

import sys
import numpy as np
#import matplotlib.pyplot as plt

from library import integral_HOM

# ----- Function -----

def controllo_arg() :
    if len(sys.argv) != 6 :     # perchè sono 6 argomenti che gli passo in totale
        print("Inserire il nome del file (compresa l'estensione), il numero di punti da generare,, minimo e massimo dell'asse x e minimo e massimo dell'asse y.\n")
        sys.exit()

# ----- Main -----

def main () :
    
    N_punti = int(sys.argv[1])      # numero di punti (con più ne metto con più sono preciso)
    x_min = float (sys.argv[2])     # estremi sull'asse x
    x_max = float (sys.argv[3])
    y_min = float (sys.argv[4])     # estremi sull'asse y
    y_max = float (sys.argv[5])
    
    integral, integral_incertezza = integral_HOM (np.sin, x_min, x_max, y_min, y_max, N_punti)
    
    #print("Valore dell'integrale e relativa incertezza: ", value_integral)     # si può fare anche così ma non è molto bello
    
    print("Il valore dell'integrale è: ", integral, "+/-", integral_incertezza)
    
    '''
    non sapevo che nel caso la funzione ritornasse due valori, questi possono essere spezzati come fatto a riga 36. il primo prende il primo valore ritornato, il secondo parametro prende il secondo ritornato
    '''
    
if __name__ == "__main__" :
    main ()
