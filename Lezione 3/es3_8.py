'''
Scrivi un programma Python per disegnare una distribuzione esponenziale e la sua funzione cumulativa
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

def main():
    x = 5.0
    esponenziale = expon(0., x)               # expon deriva da scipy.stats
    x_axis = np.linspace(0, 10, 100)

    # Creazione di una figura con due subplot affiancati
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # 1 riga, 2 colonne
    
    # Primo grafico: PDF
    axes[0].plot(x_axis, esponenziale.pdf(x_axis), label="PDF")   # con esponenziale.pdf uso la funzione predefinita nella libreria
    axes[0].legend()
    axes[0].grid()
    axes[0].set_title("Funzione di densità di probabilità (PDF)")

    # Secondo grafico: CDF
    axes[1].plot(x_axis, esponenziale.cdf(x_axis), label="CDF")     # con esponenziale.cdf uso la funzione predefinita nella libreria
    axes[1].legend()
    axes[1].grid()
    axes[1].set_title("Funzione di distribuzione cumulativa (CDF)")

    plt.tight_layout()  # AQuesto aggiusta automaticamente spazi tra i grafici
    plt.savefig("grafici_PDF_CDF_affiancati.png")
    plt.show()
    
if __name__ == '__main__':
    main()
