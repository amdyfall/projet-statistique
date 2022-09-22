
#Observation par graphique l’évolution de cette estimation lorsque n varie



#importation des bibliotheques
from scipy import random
import numpy as np
import math
import matplotlib.pyplot as plt

#initialisation des valeurs de a,b et n
a = 0
b = 1
N = 1000


"""Definition de la fonction qui retourne l'expression de la fonction f de I2."""
def f(x):
    return np.sqrt(1-x**2)



aire = []          #initialisation d'un tableau qui contient chaque valeur d'une estimation par la methode jusqu'à n iterations.


for i in range(N):                       #boucle parcourant les valeurs de la v.a suvant une loi uniforme sur l'intervalle [a,b]
    
    xrand = random.uniform(a,b,N)
    
    for i in range(len(xrand)):                        #boucle parcourant jusqu'aux nombres de valeurs possible de la v.a 
        
        
        xrand[i]= random.uniform(a,b)              #l'expression de la variable aleatoire pour chaque valeur i
        
        
        integrale = 0.0                     # initialisation de l'estimation
        
    for i in range(N):
        integrale += f(xrand[i])          # incrementation de l'estimation
        
    result = 4*(b-a)/float(N)*integrale    # incrementation de la valeur de l'estimation par la methode
     
    aire.append(result)  #ajouts de chaque valeur de l'estimation jusqu'à n iterations dans un tableau
    
    
plt.hist(aire,bins = 10, ec = 'black')
plt.xlabel("Aire")
plt.show()