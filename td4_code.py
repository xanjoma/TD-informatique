# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 14:49:30 2025

@author: maxjo_ceqfzal
"""


import matplotlib.pyplot as plt



def hachage (mot):
    
    h = 0
    
    for car in mot :
        h += ord(car)
        
    return h


class Hashtable:
    
    
    def __init__ (self,hachage,N):
        
        self.taille = N
        self.table = [None]*N
        self.hachage = hachage
    
    
    def put (self,key,value):
        
        N = self.taille
        index = self.hachage(key)%N
        bloc = self.table[index]
        
        if bloc == None:
            bloc = [[key,value]]
            
        else:
            
            for elt in bloc:
                if elt[0] == key:
                    elt[1] = value
            
            bloc.append( (key,value) )
        
        self.table[index] = bloc
    
    
    def get (self,key):
        
        N = self.taille
        index = self.hachage(key)%N
        lim = 0
        
        while lim < N:
            
            bloc = self.table[index]
            
            if not bloc == None:
            
                for elt in bloc:
                    if elt[0] == key:
                        return elt[1]
            
            index = (index+1)%N
            lim += 1
        
        return None
            
        
    def repartition(self):
        
        N = self.taille
        x = range(N)
        y = []
        
        for index in range (N):
            
            bloc = self.table[index]
            
            if bloc == None:
                y.append(0)
            
            else:
                y.append(len(bloc))
            
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()


'''
chargement dico
'''

liste=list()
f = open('frenchssaccent.dic','r')

for ligne in f:
    liste.append(ligne[0:len(ligne)-1])
    
f.close()


'''
tests
'''
        
ht = Hashtable(hachage,4)
print (ht.table)

ht.put('abc',3)
print (ht.table)

print ( ht.get('abc') ) #3

print ( ht.get('aaa') )    #None  

ht.put('cba',5)
print (ht.table)

ht.put('abc',7)
print (ht.table)

print ( ht.get('abc') )    #7

print ( ht.get('cba') )    #5

ht.put('abb',3)
print(ht.table)

ht.repartition()


ht2 = Hashtable(hachage,320)

for mot in liste:
    ht2.put(mot,len(mot))

ht2.repartition()

