'''
Scrivi un programma Python che determini la soluzione delle equazioni del secondo ordine.
'''

import sys
import numpy as np

def soluz_eq_secondo_grado (a, b, c) :

    if a == 0 :                                                     # Non sarebbe una eq. di secondo grado e dividerei per 0 (no buono)
        return print("Non è una equazione di econdo grado")
    
    else :
        delta = (b**2) - (4*a*c)                                        # Calcolo il delta per dividere i casi
        if delta > 0 :
            x1 = (-b + np.sqrt(delta))/(2*a)
            x2 = (-b - np.sqrt(delta))/(2*a)
            return print("Le soluzioni sono\nx1 =", x1, "\nx2 =", x2)
    
        elif delta == 0 :                                               # mi basta stampare una sola soluzione (sono uguali)
            x1 = x2 = -b/(2*a)
            return print("La soluzione è x = ", x1)
    
        #elif delta < 0 :                                                # Dovrei introdurre i complessi (che sbatti)
        else :
            return print("Non eiste soluzione per ogni x appartenente ai numeri reali.")
    
if __name__ == '__main__' :
    
    # Passo i coeff. a linea di comando
    
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
 
    soluz_eq_secondo_grado(a, b, c)     # Richiamo la funzione
