'''
Inserire il calcolo dell'integrale dell'esercizio precedente in un ciclo che, al variare del numero N di punti generati, visualizzi il valore dell'integrale e la sua incertezza.

Rappresentare graficamente l'andamento del valore integrale e della sua incertezza al variare di N su scala logaritmica.

Sovrapponiamo questo comportamento a quello ottenuto completando l'esercizio 8.6.
'''

import matplotlib.pyplot as plt
import numpy as np
import sys
import time

from library import integrale_MonteCarlo

# ----- ----- Funzioni ----- -----

def controllo_arg() :
    if len(sys.argv) != 2 :
        print("Inserire il nome del file (compresa l'estensione) ed il numero di punti con cui generare l'integrale.\n")
        sys.exit()

# ----- ----- Main ----- ----- 

def main () :

    controllo_arg ()

    N = int (sys.argv[1])
    N_max = 1000000

    x_min = 0.          # conosco il risultato tra 0 e pi greco quindi mi faccio furbo
    x_max = np.pi

    value = []          # creo le due liste che dovranno contenere i valori dell'integrale e degli errori
    errori = []
    lista_N = []        # lista degli N per 

    t_start = time.time()       # non è richiesto ma ero curioso
    while (N < N_max) :
        if (N < 5) :            # se sono sotto i 5 punti ne chiedo di più
            print("Inserisci più punti.")
            sys.exit ()

        elif (N > N_max) :      # se input ne passo di più di N_max -> mettere meno punti
            print("Hai inserito troppi punti.")
            sys.exit ()
        
        # calcolo dell'integrale
        val_int, err_int = integrale_MonteCarlo (np.sin, x_min, x_max, N)
        print ("Valore dell'integrale con", N, " punti :\n", val_int, "+/-", err_int, "\n")

        # riempimento delle liste
        value.append (val_int)
        errori.append (err_int)
        lista_N.append(N)
        N = N * 2           # incremento molt. per due per avere un range maggiore

    t_end = time.time()     # stoppo il tempo

    print(f"Tempo impiegato per eseguire: {(t_end - t_start):.2f} secondi.")

    # creazione del grafico
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (10, 5))     # numero righe e colonne e dimensione figura

    ax.set_title ("Grafico integrale Montecarlo", fontsize = 14)
    ax.set_xlabel ("punti sottesi")
    ax.set_ylabel ("valore integrale con errori")
    ax.set_xscale("log")

    ax.errorbar (lista_N, value, xerr = 0.0, yerr = errori,                       # nell'ordine: valori x, valori y, errore sulla x, errori sulle y
        markersize = 5,                             # dimensione del punto
        fmt = 'o',                                  # tipo di marker (punto)
        color = 'blue',                             # colore della linea
        linestyle = '--',                           # tipo di linea
        ecolor = 'red',                             # colore della barra di errore
        elinewidth = 1.5,                           # spessore barre errori
        capsize = 5,                                # lunghezza cappello barre errori
        capthick = 1.5, 
        label = "Andamento della precisione")
    
    ax.legend (fontsize = 10, loc = 'best')
    ax.grid (color = 'gray', linestyle = ':', linewidth = 0.5)      # impostazioni della griglia

    plt.savefig ("es8_8.png")
    plt.show ()


if __name__ == "__main__" :
    main ()