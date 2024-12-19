# Librerie necessarie affinchè la library.py funzioni
import sys
from math import sqrt, ceil, pow
import numpy as np
import time
import random

#commento prova GitHub

# ----------------- TIME -----------------

'''
Posso far partire la libreria tima per vedere il tempo di esezuione dell'intero programm o di un pezzo di questo. Per farlo importo la libreria time (import time) ed in un punto del programma assegnerò la variabile (che posso definire come voglio)

t_start = time.time()
... funzione di cui si vuole sapere il tempo di esecuzione
t_end = time.time()

# a schermo printerò

print(f"Tempo impiegato per eseguire: {(t_end - t_start):.2f} secondi.")    # il .2 serve a stabiliare il numero di cifre significative, se ne voglio 3 userò .3

# se il tempo necessario a completare l'operazione è molto breve posso usare

print(f"Tempo impiegato per eseguire: {1000*(t_end - t_start):.6f} millisecondi.")
'''

#----------------- OPERAZIONI CON LISTE -----------------

# ------ Funzioni Built-in ------
'''
len(lista): Restituisce il numero di elementi nella lista.
sum(lista): Calcola la somma di tutti gli elementi numerici nella lista.
max(lista): Restituisce il valore massimo nella lista.
min(lista): Restituisce il valore minimo nella lista.
sorted(lista): Restituisce una nuova lista ordinata senza modificare l'originale.
reversed(lista): Restituisce un iteratore per scorrere la lista in ordine inverso.
'''

# ------ Metodi delle Liste ------
'''
lista.append(elemento): Aggiunge un elemento alla fine della lista.
lista.extend(altra_lista): Estende la lista aggiungendo tutti gli elementi di un’altra lista.
lista.insert(indice, elemento): Inserisce un elemento in una posizione specifica.
lista.remove(elemento): Rimuove la prima occorrenza di un elemento.
lista.pop([indice]): Rimuove e restituisce un elemento dalla lista (di default l’ultimo).
lista.clear(): Rimuove tutti gli elementi dalla lista.
lista.index(elemento): Restituisce l’indice della prima occorrenza di un elemento.
lista.count(elemento): Restituisce il numero di occorrenze di un elemento nella lista.
lista.sort(): Ordina la lista in loco (modifica la lista originale).
lista.reverse(): Inverte l’ordine degli elementi nella lista in loco.
'''

# ------ Operatori Utili ------
'''
Concatenazione: lista1 + lista2             # restituisce una nuova lista combinata.
Ripetizione: lista * n restituisce          # una lista ripetuta n volte.
Verifica presenza: elemento in lista        # restituisce True se l’elemento è presente.
Slicing: lista[start:stop:step]             # estrae una porzione della lista. Ad esempio lista[:50] prende solo i primi 50 elementi.    lista[50:] gli ultimi 50           lista[0:25:1] prende 1, 2, 3,..., 25
'''

# ----------------- OPERAZIONI CON ARRAY -----------------

# ------ Creazione e Inizializzazione ------
'''
np.array([1, 2, 3]): Crea un array da una lista o tupla.
np.zeros((2, 3)): Crea un array di zeri con forma specificata.
np.ones((3, 4)): Crea un array di uni con forma specificata.
np.full((2, 2), 7): Crea un array pieno di un valore specifico.
np.eye(3): Crea una matrice identità.
np.arange(start, stop, step): Crea un array con valori equidistanti.
np.linspace(start, stop, num): Crea un array di valori equidistanti tra start e stop.
'''

# ------ Proprietà degli Array ------

'''
array.shape: Restituisce la forma (dimensioni) dell'array.
array.size: Numero totale di elementi nell'array.
array.ndim: Restituisce il numero di dimensioni dell'array.
array.dtype: Tipo di dato degli elementi dell'array.
'''

# ------ Operazioni Matematiche ------
'''
np.sum(array, axis=None): Calcola la somma degli elementi lungo un asse.
np.mean(array, axis=None): Calcola la media.
np.max(array, axis=None) / np.min(array, axis=None): Restituisce il valore massimo o minimo.
np.std(array) / np.var(array): Calcola la deviazione standard o la varianza.
np.prod(array): Prodotto degli elementi dell'array.
np.cumsum(array): Somma cumulativia.
np.cumprod(array): Prodotto cumulativo
'''

# ------ Operazioni di Modifica ------
'''
array.reshape(new_shape): Cambia la forma dell'array.
array.flatten(): Appiattisce l'array in un array monodimensionale.
np.transpose(array): Calcola la trasposta.
array.T: Alias per trasposta.
np.concatenate([array1, array2], axis=0): Unisce array lungo un asse.
np.split(array, indices): Divide l'array in sotto-array.
'''

# ------ Selezione e Mascheramento ------

'''
array[index]: Accede a un elemento o sotto-array.
array[:, 1]: Slicing; estrae tutti gli elementi della colonna 1.
array[array > 5]: Restituisce gli elementi che soddisfano una condizione.
'''

# ------ Operazioni Logiche ------

'''
np.all(array > 0) / np.any(array > 0): Verifica se tutti o almeno uno degli elementi soddisfano la condizione.
np.where(array > 5): Restituisce gli indici degli elementi che soddisfano una condizione.
np.isin(array, [2, 3]): Verifica se gli elementi appartengono a un insieme.
'''

# ------ Operazioni Avanzate ------

'''
np.dot(array1, array2): Prodotto scalare o matriciale.
np.linalg.inv(array): Calcola l'inversa di una matrice.
np.linalg.eig(array): Restituisce autovalori e autovettori.
np.sort(array, axis=-1): Ordina gli elementi lungo un asse.
'''



# ----------------- LETTURA E SCRITTURA FILE .TXT -----------------

# Funzione di controllo degli argomenti da modificare di volta in volta nel main
def controllo_arg() :
    if len(sys.argv) != num_arg :       # Super NB! Nel main inserirò una variabile int chiamata num_arg. prima di chiamare la funzione (Ad esempio: num_arg = int(3) se gli argomenti da passare a linea di comando sono 3 (nome del file compreso) )
        print("Inserire il nome del file (compresa l'estensione) e ... .\n")
        sys.exit()

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Se voglio creare un array copio questo nel main
'''
    with open(sys.argv[1]) as file :
        sample = np.array([float(x) for x in file.readlines()])       # Qui il casting è obbligatorio!!!
    print("Numero di elmenti nel file: ", len(sample))
'''

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Se voglio creare una lista copio questo nel main
'''
    with open(sys.argv[1]) as file :
        sample = [float(x) for x in file.readlines()]           # Qui il casting è obbligatorio!!!
    print("Numero di elmenti nel file: ", len(sample))
'''



# ----------------- MATPLOTLIB -----------------


# Funzione sturges per il binnaggio (funziona discretamente bene, ma conviene sempre veerificare)
def sturges (N_eventi) :
    return ceil (1 + np.log2 (N_eventi))

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Istogramma
'''
    bin_edges = np.linspace(x_min, x_max, Nbin)         # Regola la dimensione dei bin e Nbin = numero di bin
    fig, ax = plt.subplots (nrows = 1, ncols = 1)
    ax.hist (sample, bins=bin_edges ,color = 'orange')  # Spesso conviene usare bins = 'auto' evitando di scrivere la linea di codice con bin_edges, per farlo però bisogna importare numpy
    ax.set_title ('Nome istogramma', size = 14)
    ax.set_xlabel ('x')
    ax.set_ylabel ('y')
    ax.grid ()                                          # Se voglio la griglia
    
    plt.savefig ('nome_del_grafico.png')
    plt.show ()                                         # Da mettere rigorosamente dopo il savefig
'''

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Disegno di una distribuzione
'''
    x_axis = np.linspace(x_min, x_max, 100)
    
    fig, axes = plt.subplots(nrows = 1, ncols = 1, figsize = (10, 5))   # 1 riga, 1 colonna
    axes.plot(x_axis, funzione_da_inserire (x_axis), label="PDF")       # con esponenziale.pdf uso la funzione predefinita nella libreria scipy
    axes.legend()
    axes.grid()
    axes.set_title("Funzione di densità di probabilità (PDF)")
    #plt.plot(x_del_punto, y_del_punto, marker = "o", color = "red")    # questo serve per mettere un punto con coordinate x ed y
    plt.savefig("nome dell'immagine.png")
    plt.show()                                                          # da mettere rigorosamente alla fine perchè blocca il porgramma
'''

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Disegno di una distribuzione una accanto all'altra
'''
    x_axis = np.linspace(0, 10, 100)

    # Creazione di una figura con due subplot affiancati
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))  # 1 riga, 2 colonne
    
    # Primo grafico: PDF
    axes[0].plot(x_axis, funzione_da_inserire.pdf(x_axis), label="PDF")   # con esponenziale.pdf uso la funzione predefinita nella libreria
    axes[0].legend()
    axes[0].grid()
    axes[0].set_title("Funzione di densità di probabilità (PDF)")

    # Secondo grafico: CDF
    axes[1].plot(x_axis, funzione_da_inserire.cdf(x_axis), label="CDF")     # con esponenziale.cdf uso la funzione predefinita nella libreria
    axes[1].legend()
    axes[1].grid()
    axes[1].set_title("Funzione di distribuzione cumulativa (CDF)")

    plt.tight_layout()  # Questo aggiusta automaticamente spazi tra i grafici
    plt.savefig("grafici_PDF_CDF_affiancati.png")
    plt.show()
'''

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Opzioni grafiche
'''
    fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize = (10, 5))     # numero righe e colonne e dimensione figura

    ax.set_title ("nome grafico", fontsize = 14)
    ax.set_xlabel ("nome asse x", fontsize = 12)
    ax.set_ylabel ("nome asse y", fontsize = 12)
    
    # se voglio la barra degli errori:
    ax.errorbar (sample, valore_y, xerr = 0.0, yerr = errori,                       # nell'ordine: valori x, valori y, errore sulla x, errori sulle y
        markersize = 5,                             # dimensione del punto
        fmt = 'o',                                  # tipo di marker (punto)
        color = 'blue',                             # colore della linea
        linestyle = '--',                           # tipo di linea
        ecolor = 'red',                             # colore della barra di errore
        elinewidth = 1.5,                           # spessore barre errori
        capsize = 5,                                # lunghezza cappello barre errori
        capthick = 1.5,                             # spessore cappello barre errori
        label = "label della linea")                # label

    ax.legend (fontsize = 10, loc = 'best')                         # loc = 'best' mette la legenda dove è c'è spazio
    ax.grid (color = 'gray', linestyle = ':', linewidth = 0.5)      # impostazioni della griglia

    plt.savefig ("nome_file.png")
    plt.show ()                                     # da mettere alla fine se no blocca tutto
'''

# ----------------- FUNZIONI UTILI -----------------

#Funzione fattoriale
def fattoriale (N) :
    if N == 0 :
        return 1
    return fattoriale (N-1) * N
    
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione coeff. binomiale
def coeff_binom (N, k) :
    if N == 0 & N < k :
        return 0
    return fattoriale (N) / fattoriale (k) * fattoriale (N-1)
    
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione esponenziale
def esponenziale (x, tau) :
    if tau == 0 :
        return 1
    return (np.exp (-1 * x / tau)) / tau

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Funzione che genera n valori con la sequenza di Fibonacci
def Fibonacci (n) :

    # Se il numero fino a cui voglio contare è minore o uguale a zero faccio in modo che il programma mi restituisca una lista vuota.
    if n <= 0 :
        return []
    
    # Se il numero fino a cui voglio contare è 1 allora la lista avrà solo il numero 1
    elif n == 1 :
        return [1]
    
    # definisco una lista iniziale con almeno due numeri (i primi due)
    lista_fibo = [0, 1]
    contatore = len(lista_fibo)            # Conta il numero di elementi nella lista
    
    while (contatore < n) :
        prossimo_num = lista_fibo[contatore-1] + lista_fibo[contatore-2]        # Somma il numero precedente all'i-esimo al i-esimo meno due
        lista_fibo.append(prossimo_num)         # Aggiunge il prossimo numero alla fine della lista
        contatore = contatore + 1       # Incrementa il numero di elementi nella lista alla fine di ofni iterazione
    return lista_fibo

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Funzione per risolvere equazioni di secondo grado
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


# ----------------- NUMERI PSEUDOCASUALI -----------------

# Default dalla libreria random
'''
random.random()     # genera numeri pseudocasuali tra 0 ed 1

random.randint(min, max)    # genera numeri pseudocasuali tra min e max

random.seed(seed)       # dove seed va passato nel main o lina di comando o in input, basta chiamare questa funzione una sola volta
'''

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Distribuzione uniforme tra x_min e x_max con seed scelto in auto
def rand_range (x_min, x_max) :
    return x_min + random.random() * (x_max - x_min)

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# genera N numeri pseudo-casuali distribuiti fra x_min ed x_max a partire da un seed
def seed_range (xMin, xMax, N, seed = 0.) :
    if seed != 0. :
        random.seed (float (seed))
    randlist = []
    for i in range (N):
        # Return the next random floating point number in the range 0.0 <= X < 1.0
        randlist.append (rand_range (xMin, xMax))
    return randlist

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione che genera numeri pseudocasuali tramite l'argoritmo Try And Catch e distribuzione uniforme rand_range
def rand_TAC (f, x_min, x_max, y_max) :
    x = rand_range (x_min, x_max)
    y = rand_range (0, y_max)
    while (y > f (x)) :
        x = rand_range (x_min, x_max)
        y = rand_range (0, y_max)
    return x

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
# Funzione rand_TAC con la funzione norm.pdf di scipy.stats. da implementare nel main con un ciclo for
def rand_TAC_norm (f, x_min, x_max, y_max, loc, scale) :
    x = rand_range (x_min, x_max)
    y = rand_range (0, y_max)
    while (y > f(x, loc, scale)) :
        x = rand_range (x_min, x_max)
        y = rand_range (0, y_max)
    return x

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione che genera numeri pseudocasuali partendo dal teorema centrale del limite
def rand_TCL (xMin, xMax, N = 1000) :
    y = 0.
    for i in range (N) :
        y = y + rand_range (xMin, xMax)
    y /= N
    return y

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Funzione bisezione NON ricorsiva per la ricerca degli zeri
def bisezione (
    f,                  # funzione di cui trovare lo zero
    x_min,              # minimo dell'intervallo
    x_max,              # massimo dell'intervallo
    prec = 0.0001) :    # precisione della funzione
    x_ave = x_min
    while ((x_max - x_min) > prec) :
        x_ave = 0.5 * (x_max + x_min)
        if (f (x_ave) * f (x_min) > 0.) :
            x_min = x_ave
        else :
            x_max = x_ave
    return x_ave

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione bisezione ricorsiva per la ricerca degli zeri
def bisezione_ric (f, x_min, x_max, precision = 0.0001) :
    x_ave = 0.5 * (x_max + x_min)
    if ((x_max - x_min) < precision) :
        return x_ave
    if (f (x_ave) * f (x_min) > 0.) :
        return bisezione_ric (f, x_ave, x_max, precision)
    else :
        return bisezione_ric (f, x_min, x_ave, precision)
        
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione aurea per ricerca del minimo
def sezione_aurea_min (
    f,                      # funzione di cui trovare lo zero
    x0,                     # estremo sx dell'intervallo
    x1,                     # estremo dx dell'intervallo
    precision = 0.0001) :   # precisione della funzione

    r = 0.618
    x2 = 0.
    x3 = 0.
    larghezza = abs (x1 - x0)
     
    while (larghezza > precision):
        x2 = x0 + r * (x1 - x0)
        x3 = x0 + (1. - r) * (x1 - x0)
      
        # si restringe l'intervallo tenendo fisso uno dei due estremi e spostando l'altro
        if (f (x3) > f (x2)):
            x0 = x3
        else :
            x1 = x2
        larghezza = abs (x1-x0)
    return (x0 + x1) / 2.

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione aurea ricorsiva per ricerca del minimo
def sezione_aurea_ric_min (f, x0, x1, precision = 0.0001) :
    r = 0.618
    x2 = x0 + r * (x1 - x0)
    x3 = x0 + (1. - r) * (x1 - x0)
    larghezza = abs (x1 - x0)                #valore assoluto
        
    if (larghezza < precision) :
        return 0.5 * (x1 + x0)
        
    if (f (x3) > f (x2)) :
        return sezione_aurea_ric_min (f, x3, x1, precision)
        
    else :
        return sezione_aurea_ric_min (f, x0, x2, precision)

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione aurea per ricerca del massimo
def sezione_aurea_max (
    f,                      # funzione di cui trovare lo zero
    x0,                     # estremo dell'intervallo
    x1,                     # altro estremo dell'intervallo
    precision = 0.0001) :   # precisione della funzione

    r = 0.618
    x2 = 0.
    x3 = 0.
    larghezza = abs (x1 - x0)
     
    while (larghezza > precision):
        x2 = x0 + r * (x1 - x0)
        x3 = x0 + (1. - r) * (x1 - x0)
      
        # si restringe l'intervallo tenendo fisso uno dei due estremi e spostando l'altro
        if (f (x3) < f (x2)) :
            x0 = x3
        else :
            x1 = x2
        larghezza = abs (x1-x0)
    return (x0 + x1) / 2.

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione aurea ricorsiva per la ricerca del massimo
def sezione_aurea_ric_max (f, x0, x1, precision = 0.0001) :
    r = 0.618
    x2 = x0 + r * (x1 - x0)
    x3 = x0 + (1. - r) * (x1 - x0)
    larghezza = abs (x1 - x0)              #valore assoluto
        
    if (larghezza < precision) :
        return 0.5 * (x1 + x0)
        
    if (f (x3) < f (x2)) :
        return sezione_aurea_ric_max (f, x3, x1, precision)
        
    else :
        return sezione_aurea_ric_max (f, x0, x2, precision)
        
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione da implimentare nel main per la generazione di numeri pseudocasuali secondo una distribuzione esponenziale
def rand_exp_inversa (t) :
    return -1. * np.log (1 - random.random()) * t

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione da implimentare nel main per la generazione di numeri pseudocasuali secondo una distribuzione esponenziale dove y dipende da un seed scelto da me
def exp_inversa_seed (t, y) :
    return -1 * np.log (1 - y) * t    # se voglio usar un seed diverso da quello basato sull'orario posso usare random.seed(seed) prima di chiamare questa funzione che dovrà contenere random.random()

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Rand poissoniana per singolo evento
def rand_pois (mean, t_m = 1.) :
    t_tot = rand_exp_inversa (t_m)
    N_evt = 0
    while (t_tot < mean) :
        N_evt = N_evt + 1
        t_tot = t_tot + rand_exp_inversa (t_m)
    return N_evt

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Rand poissoniana per N eventi
def rand_pois_Neventi (mean, N, t_m = 1.) :
    v = []
    for i in range(N) :
        x = rand_pois(mean, t_m)
        v.append(x)
    return v

#  ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Rand per i decadimenti radioattivi     (è uguale a rand_pois ma cambiano solo i nomi delle variabili per chiarezza)
def rand_pois_new (t_misura, t_dec) :
    t = rand_exp_inversa(t_dec)
    N_evt = 0
    while (t < t_misura) :
        N_evt = N_evt + 1
        t = t + rand_exp_inversa(t_dec)
    return N_evt

#  ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione per il calcolo dell'integrale (area) e scarto secondo il metodo Hit Or Miss
def integral_HOM (f, x_min, x_max, y_min ,y_max, N_punti) :
    x_coord = []
    y_coord = []
    for _ in range (N_punti) :
        x_coord.append (rand_range (x_min, x_max))
        y_coord.append (rand_range (y_min, y_max))
    
    points_under = 0
    for x, y in zip (x_coord, y_coord) :             #zip per iterare su più liste in contemporanea
        if (f (x) > y) :
            points_under = points_under + 1
    
    A_rett = (x_max - x_min) * (y_max - y_min)
    frac = float (points_under) / float (N_punti)
    integral = A_rett * frac
    integral_incertezza = A_rett**2 * frac * (1-frac) / N_punti
    return integral, integral_incertezza

#  ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

#Funzione likelihood logaritmica
def loglikelihood (an_array, pdf, para) :
    result = 0.
    for x in an_array :
        if pdf (x, para) > 0. :
            result = result + np.log (pdf (x, para))
    return result
    
#  ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----



# ----------------- STATISTICHE -----------------

# Media con array
def media (sample) :
    mean = np.sum(sample)/len(sample)
    return mean
    
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Varianza con array
def varianza (sample) :
    somma_quadrata = 0
    somma_quadrata = np.sum( (sample - media(sample))**2 )
    var = somma_quadrata/(len(sample))
    return var

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Varianza con corr. di Bessel con array
def varianza_bessel (sample) :
    somma_quadrata = 0
    somma_quadrata = np.sum( (sample - media(sample))**2 )
    var = somma_quadrata/(len(sample) - 1)
    return var

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Deviaz. standard con array
def dev_std (sample) :
    sigma = np.sqrt(varianza(sample))
    return sigma

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Deviaz. standard della media con array
def dev_std_media (sample) :
    return dev_std(sample) / (np.sqrt( len(sample) ))

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# LE SEGUENTI DUE FUNZIONI SONO COMMENTATE POICHè NON SONO STATE ANCORA CORRETTE O TESTATE QUINDI ATTENZIONE AD INCLUDERLE NEI PROGRAMMI
'''
# Funzione per il calcolo della skewness (simmetria o asimmetria)
def skewness (sample) :
    mean = media (sample)
    asymm = 0.
    for x in sample:
        asymm = asymm + pow (x - mean,  3)
    asymm = asymm / (sample.N * pow (sample.sigma (), 3))
    return asymm

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Funzione per il calcolo della curtosi
def kurtosis (sample) :
    mean = sample.mean ()
    kurt = 0.
    for x in sample:
        kurt = kurt + pow (x - mean,  4)
    kurt = kurt / (sample.N * pow (sample.variance (), 2)) - 3
    return kurt
'''

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

# Se invece volessi usare delle semplici liste senza i numpy array posso usare le seguenti funzioni (megglio usare numpy che è più veloce)
'''
# Media con lista
def media (lista) :
    mean = sum(lista)/len(lista)
    return mean

# Varianza con lista
def varianza (lista) :
    somma_quadrata = 0
    for elem in lista :
        somma_quadrata = somma_quadrata + (elem - media(lista))**2
    var = somma_quadrata/(len(lista))

# Deviaz. standard con lista
def dev_std (lista) :
    sigma = sqrt(varianza(lista))
    return sigma

# Deviaz. standard della media con lista
def dev_std_media (lista) :
    return dev_std(lista)/sqrt(len(lista))
'''
