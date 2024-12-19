'''
Scrivi un programma che, utilizzando un forciclo, restituisca la sequenza di Fibonacci fino all'n-esimo termine e la memorizzi in un file Python dictionary, dove keyrappresenta l'indice di ciascun elemento e valueil suo valore effettivo.
'''

import sys

def Fibonacci (n) :
    if n == 0 :
        return {}
    
    elif n == 1 :
        return {'a1': 0}
    
    dizionario_fibonacci = {'a1': 0, 'a2': 1}                       # si veda come costruire un dizionario
    elem = len(dizionario_fibonacci)
    
    for i in range (2, n) :
        prossimo_num = dizionario_fibonacci[f'a{i}'] + dizionario_fibonacci[f'a{i-1}']          #si indica con f'...'
        dizionario_fibonacci[f'a{i+1}'] = prossimo_num                                      # attenzione all'assegnazione
    return dizionario_fibonacci
    
    
if __name__ == '__main__' :
    
    n = int(sys.argv[1])
    
    print("Sequenza di Fibonacci fino al numero", n, ":", Fibonacci(n))
