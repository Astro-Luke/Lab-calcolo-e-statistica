'''
Use the Python scipy.stat.norm object to determine the area of a normal distributionof its tails outside the range included within an interval of 1, 2, 3, 4, and 5standard deviations around its mean
'''

import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
#import matplotlib.pyplot as plt

def main():
    mean = 0.
    sigma = 1.
    
    # Fattori di deviazione standard
    deviations = [1, 2, 3, 4, 5]
    
    for dev in deviations :
        inf = mean - dev * sigma        # Questo è il limite inferiore dell'intergrazione
        upper = mean + dev * sigma      # limite superiore dell'integrazione
        
        # Calcolo dell'area nelle code
        tail_area = 1 - quad(norm(loc=mean, scale=sigma).pdf, inf, upper)[0]  # faccio 1- ... perchè quello che voglio è l'area delle code e la distribuzione è già normalizzata
        print(f"Deviazioni: {dev}, Area delle code: {tail_area:.5f}")

if __name__ == '__main__':
    main()
