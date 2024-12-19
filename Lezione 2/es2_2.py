'''
Crea un array NumPy unidimensionale contenente una sequenza di numeri interi da 1 a 100

Partendo da questo, crea un array NumPy unidimensionale contenente in ogni voce la somma dei numeri interi da 1 fino all'indice di quella voce
'''

import numpy as np

def somma_voci () :

    array = np.arange(1, 101)                   # Genero l'aray di 100 numeri tra 1 e 101
    somma_array = np.cumsum(array)                 # Cumsum fa la somma di tutti i numeri precedenti
    
    print ("Array con somme voci: ", somma_array)
    return
    
if __name__ == '__main__' :

    somma_voci()
