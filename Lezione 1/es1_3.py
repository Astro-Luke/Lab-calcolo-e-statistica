'''
Scrivi un programma che, utilizzando un whileciclo, restituisca la sequenza di Fibonacci fino all'n-esimo termine e la memorizzi in un file python list.

N.B.  Di fatto questo programma risolve anche l'esercizio 1.5'''

import sys

def Fibonacci (n) :

    # Se il numero fino a cui voglio contare è minore o uguale a zero faccio in modo che il programma mi restituisca una lista vuota.
    if n <= 0 :
        return []
    
    # Se il numero fino a cui voglio contare è 1 allora la lista avrà solo il numero 1
    elif n == 1 :
        return [1]
    
    # definisco una lista iniziale con almeno due numeri (i primi due)
    lista_fibo = [0, 1]
    contatore = len(lista_fibo)             # Conta il numero di elementi nella lista
    
    while (contatore < n) :
        prossimo_num = lista_fibo[contatore-1] + lista_fibo[contatore-2]        # Somma il numero precedente all'i-esimo al i-esimo meno due
        lista_fibo.append(prossimo_num)         # Aggiunge il prossimo numero alla fine della lista
        contatore = contatore + 1       # Incrementa il numero di elementi nella lista alla fine di ofni iterazione
    return lista_fibo

if __name__ == '__main__' :

    n = int(sys.argv[1])        # Passo a linea di comando il numero di iterazioni
    
    print("Sequenza di fibonacci fino al numero", n, ":", Fibonacci(n))
