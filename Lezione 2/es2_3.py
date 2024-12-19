'''
Crea un array unidimensionale contenente la sequenza dei primi 50 numeri naturali pari

Crea un array unidimensionale contenente la sequenza dei primi 50 numeri naturali dispari

Crea un array unidimensionale contenente la somma elemento per elemento dei due array precedenti
'''


import numpy as np

def seq_naturali (N) :
    
    # Gnero due array per ospitare i numeri pari e dispari (attenzione alla lunghezza dei vettori che deve essere la stessa e, poichè uno parte da 0 (pari) l'altro parte da 1)
    array_pari = np.arange(0, N, 2)
    array_disp = np.arange(1, N, 2)
    
    print("Sequenza numeri pari:", array_pari)
    print("Sequenza numeri dispari:", array_disp)

    return array_pari, array_disp                       # questa riga va alla fine dela funzione seq_naturali se no esci dalla funzione!

def somma (array_pari, array_disp) :
    array_somma = array_pari + array_disp
    print("Array con la somma dell'elemento i-esimo dell'array pari con l'elemento i-esimo dell'array dispari", array_somma)
    #return array_somma


if __name__ == '__main__' :
    
    N = int(100)
    
    array_pari, array_disp = seq_naturali(N)   # li metto uno dopo l'altro se no me li scrive due volte
    
    somma(array_pari, array_disp)
