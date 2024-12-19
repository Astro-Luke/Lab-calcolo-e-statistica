'''
Crea un istogramma unidimensionale riempito con 5 valori e salva l'immagine dell'istogramma in un pngfile
'''

import matplotlib.pyplot as plt

if __name__ == '__main__' :
    lista_val = [1, 2, 2, 3, 5]
    
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (lista_val, color = 'orange')
    ax.set_title("Histogram", size = 14)
    ax.set_xlabel("samples")
    ax.set_ytitle("counter")
    
    plt.savefig('grafico es3_1.png')
    plt.show()
