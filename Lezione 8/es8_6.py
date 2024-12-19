'''
Si inserisca il calcolo dell'integrale dell'esercizio precedente in un ciclo che,
al variare del numero *N* di punti generati, mostri il valore dell'integrale
e della sua incertezza.
  * Si utilizzi uno scatter plot per disegnare gli andamenti del valore dell'integrale
    e della sua incertezza, al variare di *N* con ragione logaritmica.
'''

import sys
import numpy as np
import matplotlib.pyplot as plt
import time

from library import integral_HOM

# ----- Function -----

def controllo_arg() :
    if len(sys.argv) != 2 :
        print("Inserire il nome del file (compresa l'estensione) ed il numero di punti da generare per l'integrazione.\n")
        sys.exit()

# ----- Main -----

def main () :
    
    controllo_arg ()
    
    N_punti = int (sys.argv[1])         # punti sotto la curva
    N_punti_max = 1000000
    x_min = 0.          # scelgo tra 0 e pi greco perchè so quanto vale quindi posso vedere al volo se è corretto
    x_max = np.pi
    y_min = 0.
    y_max = 1.          # tanto seno e coseno hanno ampiezza 1
    
    valore = []         # lista che conterrà il valore dell'area
    errori = []         # lista che conterrà l'errore sull'area
    N_lista = []        # lista degli N per il grafico
    
    t_start = time.time ()                      # non è richiesto ma volevo confrontare l'Hit-Or-Miss e Monte Carlo
    
    while (N_punti < N_punti_max) :
        if (N_punti < 5) :                      # se ho meno di 5 punti ne chiedo di inserirne di più
            print("Hai immesso troppi pochi punti, inseriscina un numero compreso tra 10 e 1000000")
            sys.exit()
        elif (N_punti > N_punti_max) :          # se ne metto troppi ne chiedo di meno
            print("Hai inserito più punti del massimo consentito dal programma")
            sys.exit()
        
        # calcolo dell'integrale
        val_integral, val_incertezza = integral_HOM (np.sin, x_min, x_max, y_min, y_max, N_punti)
        print ("Valore dell'integrale con", N_punti, " punti :\n", val_integral, "+/-", val_incertezza, "\n")
        
        # riempimento delle liste
        valore.append (val_integral)
        errori.append (val_incertezza)
        N_lista.append (N_punti)
        
        # incremento i numeri di 10 se no ciaonee
        N_punti = N_punti * 2

    t_end = time.time ()    # stoppo il tempo

    # stampa del tempo
    print(f"Tempo impiegato per eseguire: {(t_end - t_start):.2f} secondi.")

    # Creazione del grafico
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (10, 5))  # 1 riga, 1 colonna

    ax.set_title ("Grafico integrali Hit Or Miss", fontsize = 14)
    ax.set_xlabel ("Punti creati")
    ax.set_ylabel ("Valore dell'integrale con errori")
    ax.set_xscale("log")
    ax.errorbar (N_lista, valore, yerr = errori,            # si mi sono divertito a giocare con il grafico
        markersize = 5,
        fmt = 'o',
        linestyle = '--',
        ecolor = 'red',
        elinewidth = 1.5,
        capsize = 5,
        capthick = 1.5,
        color = 'blue',
        label = "Andamento della precisione")

    ax.legend (fontsize = 10, loc = 'best')
    ax.grid (color = 'gray', linestyle = ':', linewidth = 0.5)

    plt.savefig ("es8_6.png")
    plt.show ()
    
    
if __name__ == "__main__" :
    main ()
