#Estimation Monte Carlo avec n=1000

#importation des bibliotheques
import numpy.random
import matplotlib.pyplot as plt
import random
import math 
import numpy


"""definition de la methode de monte carlo integrationMonteCarlo qui prend comme parametre
une fonction f ou esperance, les valeurs de l'intervalle [a,b], et une valeur n, predefinie le nombre de simulations"""

def integrationMonteCarlo(fonction,a,b,N):
    
    
    x=a+(b-a)*numpy.random.random_sample(N)      #incrementation de x, l'expression de la variable aleatoire
    
    p=1.0/(b-a)                            #p, la densité de probabilité uniforme sur [a,b]
    
    f = fonction(x)       #expression de l'esperance de la variable aleatoire x.
    
    somme = 4*f.sum()/(N*p)
    
    return (somme)           #retourne une valeur pour chaque estimation jusqu'à n iterations.

"""Definition de la fonction qui retourne l'expression de la fonction f de I2."""
def f(x):
    return numpy.sqrt(1-x**2)              #retourne l'expression de la fonction f de I2.



integrale = integrationMonteCarlo(f,0,1,1000)  #Incrementation et appel de fonction integrationMonteCarlo

#Affiche la valeur de l'estimation
print(integrale)
