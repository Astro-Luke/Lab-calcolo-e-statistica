'''
Scrivi un programma Python che trovi l'elenco dei numeri interi primi inferiori a 100, partendo dal presupposto che 2 è un numero primo
'''

def primo (n) :

    lista = []
    
    if n < 2 :
        return False
    
    divisori = []
    for i in range (2, n) :
        if n%i == 0 :
            
        i = i + 1
    print(lista)


if __name__ == '__main__' :

    primo(100)
