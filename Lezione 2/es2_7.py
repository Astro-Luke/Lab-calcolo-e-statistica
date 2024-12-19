'''
Scrivere una libreria Python contenente funzioni per eseguire le seguenti operazioni sugli array NumPy 1D:

Calcola la media dei suoi elementi

Calcola la varianza dei suoi elementi

Calcola la deviazione standard dei suoi elementi

Calcola la deviazione standard dalla media dei suoi elementi
'''

import numpy as np

def media (array) :
    somma = array.sum()
    mean = somma/len(array)
    return mean
    
def varianza (array) :
    mean = media(array)
    somma_quadrata = 0
    for i in array :
        somma_quadrata = somma_quadrata + (i - mean)**2
    return somma_quadrata/len(array)
    
def varianza_bessel (array) :
    mean = media(array)
    somma_quadrata = 0
    for i in array :
        somma_quadrata = somma_quadrata + (i - mean)**2
    return somma_quadrata/ (len(array) - 1)

def dev_standard (array) :
    var = (varianza(array))**0.5
    return var

#def dev_standard_media (array) :
#    sigma_mean = dev_standard(array)/((len(array))**0.5)
#    return sigma_mean
    
def dev_standard_media (array) :
    sigma_mean = dev_standard(array)/ np.sqrt((len(array)))
    return sigma_mean
    
    
# ----- MAIN ------
if __name__ == '__main__' :

    array_prova = np.array([2.8, 12, 98.1, 126.1, 73.7, 98.3, 72.1, 6, 97.3, 83.9, 23.8])

    print("La media è: ", media(array_prova))
    print("La varianza è: ", varianza(array_prova))
    print("La deviazione standard è: ", dev_standard(array_prova))
    print("La deviazione standard della media è: ", dev_standard_media(array_prova))
