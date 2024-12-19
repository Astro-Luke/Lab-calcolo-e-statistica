'''
All'interno di un programma Python, l'ora corrente può essere ottenuta con la timelibreria:
import time
time_snapshot = time.time ()
print (time_snapshot)

Confronta le prestazioni temporali delle operazioni elemento per elemento eseguite tra due elenchi rispetto alla stessa operazione eseguita in forma compatta tra due array NumPy

A partire da quale dimensione le differenze cominciano a essere significative?
'''

import time
import numpy as np

# Prodotto tra elementi usando le funzionalità di numpy
def prodotto_numpy (N) :                               # N dimensione dell'array
    
    array_uno = np.arange(0, N, 1)
    array_due = np.arange(0, N, 1)

    prodotto_array = array_uno * array_due
    

# Prodotto di elementi usando le liste
def prodotto_liste (N) :

    lista_uno = list(range(N))
    lista_due = list(range(N))
    
    for a, b in zip(lista_uno, lista_due) :
        prodotto_liste = a * b

# ---------- MAIN -----------

if __name__ == '__main__' :
    
    N = 10000000
    
    start_np = time.time()
    prodotto_numpy(N)
    end_np = time.time()
    
    start_list = time.time()
    prodotto_liste(N)
    end_list = time.time()
    
    print("Con", N, "elementi:\n")
    print(f"Tempo impiegato per array numpy: {(end_np - start_np):.3f} secondi.")
    print(f"Tempo impiegato per liste: {(end_list - start_list):.3f} secondi.\n")
