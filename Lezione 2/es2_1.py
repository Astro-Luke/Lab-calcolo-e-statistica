'''
Crea array NumPy unidimensionali utilizzando diverse tecniche di generazione
'''

import numpy as np

def crea_array(N):
    # Creo un bell'array di soli zeri
    zero_array = np.zeros(N)

    # Creo un bel vettore di elementi vuoti
    vuoto_array = np.empty(N)

    # Creo un array di float a partire da una lista
    lista = [1.4, 83.0, 274.1, 843.9, 2378.4]
    float_array = np.array(lista)

    # Creo un array contenente tutti i numeri interi tra 0 e 25 con arange
    step = 1
    int_array = np.arange(0, 26, step)

    # Creo un array contenete numeri double con linspace
    doub_array = np.linspace(0., 26., 20)

    print("Array di zeri: ", zero_array)
    print("Array vuoto: ", vuoto_array)
    print("Array di float: ", float_array, "\na partire dalla lista: ", lista)
    print("Array di interi con arange: ", int_array)
    print("Array di double con linspace: ", doub_array)

if __name__ == '__main__':
    crea_array(10)          # 10 è il numero di elementi per gli array vuoto e di zeri
