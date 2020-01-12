'''
Created on 1 janv. 2020

@author: redZA
'''
from random import randint
from operator import __truediv__
from math import sqrt
#variables
''' 1/ 
    cette fonctions factorise un nombre (n)
    sous la forme 
    n -1 = (2^s) * d
''' 
def fact(n):
    s = 0
    d = n - 1 
    while((d >> 1) << 1 == d): # on vérifier chaque fois si d est un pair ou impair
        #diviser par 2
        d= d >> 1
        #pour chaque division on ajout s aaugment s avec 1 
        s += 1
    return s , d
#------------

''' 2/ 
    cette function affiche un tableau de 
    N        |    témoin on nou 
    
    
'''
def rap(n):
    i = 1
    print("N\t|\tA\t|\tTémoins ?")
    while( i <= n ):
        print(n,"\t|\t",i,"\t|\t",temoin(n, i))
        i += 2

''' 3/ 
    cette function permet de retourner un nombre aléloitre par défaut
    la valeur de ce nombre varie entre 1 et n (entré)
    pour retourner une liste on met : 
    alea(n , combien de nombre à retourner)
'''
def alea(n, nbr = 1):
    if(nbr == 1):
        o = randint(1,n)
        while((o >> 1) << 1 == 0):
            o = randint(1,n)
        return o
    else:
        li = list()
        while(nbr != 0):
            o = randint(1,n)
            while((o >> 1) << 1 == 0):
                o = randint(1,n)
            li.append(o)
        return li
            
''' 4/ 
    cette function affiche d'une liste de taille K des valeur 
    aléatoire entre 1 et n , si elle sont des témoins 
    de miller par rapport à n  
    miller_rabin(le nombre à tester , le nombre des valeurs 
'''  
def miller_rabin(n,k):
    print("n\t|\tn\t|\tNature")
    i = 1
    while(i <= k):
        a = alea(n-1)
        print(n,"\t|\t",a,"\t|\t",temoin(n, a))
        i += 1
    '''
    for i in alea(n,nbr=k):
        print(n,"\t|\t",i,"\t|\t",temoin(n, i))
    '''
        
'''
    Vérfier si n est un témoin à la base a
'''
def temoin(n,a):
    [s , d] = fact(n)
    x = pow(a,d) % n
    e = n -1
    for i in range(1,s):
        x = pow(x,2) % n 
        if(x == 1 or x == -1 or x - e == 0 ):
            return True
    return False

def graph(n):
    f = open("outfile2.csv",'w+')
    p = 3
    while(p <= n):
        base = 2
        nbr_temoins = 0
        nbr_entiers = 0
        while(base <= p-1):
            if(temoin(p, base) == True):
                nbr_temoins += 1
            nbr_entiers +=1
            base +=1
        s = str(p)+"\t"+str(nbr_temoins*100/nbr_entiers)+"\n"
        f.write(s)
        p+= 1 
    f.close()

def graph2(n):
    f = open("outfile0.csv",'w+')
    p = 3
    while(p <= n):
        if(p % 2 == 0):
            p+= 1 
            continue
        base = 2
        nbr_temoins = 0
        nbr_entiers = 0
        while(base <= p-1):
            if(temoin(p, base) == True):
                nbr_temoins += 1
            nbr_entiers +=1
            base +=1
        s = str(p)+"\t"+str(nbr_temoins*100/nbr_entiers)+"\n"
        f.write(s)
        p+= 1 
    f.close()
    
def verfier_si_premier(n):
    max = int(sqrt(n))+1
    o = 2
    while(o <= max):
        test = int(n/o)
        if((o*test) == n):
            return False
        o += 1
    return True

def fermet_number(k):
    a = 2 >> k
    return( 2 >> a)

def mersenne_number(k):
    a = (2 >> k) - 1
    return a   
'''
    Cette fonctionne calcule le nombre de fermet et mersenne utilisant 1 jusqu'au k
    et vérifier si un nombre premier ou pas
'''
def tested_fermet_mersenne(k):
    for i in range(k):
        t = fermet_number(i)
        print("k = ",i,"Fermet : ", t)
        print("Nombre premier : " , verfier_si_premier(t))
        t = mersenne_number(i)
        print("k = ",i,"Mersenne : ", t)
        print("Nombre premier : " , verfier_si_premier(t))
        
        
        
def power_fast(x,n):
    if(n == 1):
        return x 
    elif(n&1 == 0):
        r = power_fast(x, n >> 1) 
        r = (r * r) %15
        return r 
    elif(n&1 == 1):
        r = power_fast(x, n >> 1) 
        r = (r * r * x) 
        return r 
#graph(1000)
graph2(1001)