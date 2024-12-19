'''
Scrivi un programma che generi numeri pseudo-casuali distribuiti secondo una funzione esponenziale e li memorizzi in un elenco.

9.10.2. Esercizio 9.2 
Aggiungere al programma precedente il codice sorgente che riempie un istogramma con i numeri presenti nell'elenco in cui sono stati trasferiti e visualizza l'istogramma sullo schermo.

9.10.3. Esercizio 9.3 
Scrivere un programma che traccia il grafico della distribuzione di probabilità esponenziale con un parametro fisso t 0 .

9.10.4. Esercizio 9.4 
Scrivere una funzione likelihood che calcoli la verosimiglianza al variare del parametro t_0, per un campione di eventi pseudo-casuali generati secondo le istruzioni dell'esercizio 1.

In che modo il risultato dipende dal numero di eventi nel campione?
'''

import numpy as np
import matplotlib.pyplot as plt

from library import rand_exp_inversa, sturges, loglikelihood

# funzione esponenziale

def funz_exp (x, t_0) :
    return (1 / t_0) * np.exp(- (x / t_0))

def main() :

    N = 10000  # numero di numeri pseudocasuali da generare
    t_0 = 2.4
    elenco_pseudocasual = []

    x_min = 0.
    x_max = 10.

    for _ in range(N):
        elenco_pseudocasual.append(rand_exp_inversa(t_0))

    Nbin = sturges(N)

    bin_edges = np.linspace(0., 10., Nbin)  # Regola la dimensione dei bin
    fig, ax = plt.subplots(nrows=1, ncols=1)
    ax.hist(elenco_pseudocasual, bins=bin_edges, color='orange')
    ax.set_title('Istogramma', size=14)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid()

    plt.savefig('es9_4_histo.png')

    x_axis = np.linspace(x_min, x_max, 100)

    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10, 5))  # 1 riga, 1 colonna
    axes.plot(x_axis, funz_exp(x_axis, t_0), label="PDF", color="blue")
    axes.legend()
    axes.grid()
    axes.set_title("Funzione di densità di probabilità (PDF)")

    plt.savefig('es9_4_distribuzione.png')

    # manca la parte con la likelihood

if __name__ == "__main__" :
    main()
