'''
Implementare una funzione che calcoli il fattoriale di un numero utilizzando una funzione ricorsiva.
'''

import sys

# ----- ----- Funzioni ----- -----
from library import fattoriale

# Funzione di controllo degli argomenti da modificare di volta in volta nel main
def controllo_arg() :
    if len(sys.argv) < 2 :
        print("Passare a linea di comando il nome del file ed il valore di cui si vuole calcolare il fattoriale.\n")
        sys.exit()

# ----- ----- Main ----- -----

def main () :
    
    controllo_arg()
    
    N = int (sys.argv[1])
    
    #x = fattoriale(N)
    print("Valore del fattoriale: ", fattoriale(N))
    
if __name__ == '__main__' :
    main ()
