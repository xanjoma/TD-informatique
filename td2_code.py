# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 14:51:54 2025

@author: maxjo_ceqfzal
"""


"""
Exercice 1
"""

class Polynomial:
    
    def __init__(self,liste):
        self.value = liste
        
    def __str__(self):
        
        L = self.value
        ch = ''
        i = len(L)-1
        
        while i>=0:
            
            if L[i]==0:
                None
            
            else:
            
                if L[i]==1:
                    
                    if i==0:
                        ch+=f'{L[0]}'
                        
                    elif i==1:
                        ch+=' + X'
                    
                    else:
                        ch+=f' + X^{i}'
                
                else:
                    
                    if i==0:
                        ch+=f'{L[0]}'
                        
                    elif i==1:
                        ch+=f' + {L[1]}X'
                    
                    else:
                        ch+=f' + {L[i]}X^{i}'
                
            i-=1
        
        if ch[1]=='+':
            ch=ch[2:]
            
        return ch


    def __add__(self,p2):
        
        L1 = self.value
        L2 = p2.value
        L = []
        
        if len(L1)<len(L2):
            
            for i in range (len(L1)):
                L.append(L1[i]+L2[i])
            
            for i in range (len(L1),len(L2)):
                L.append(L2[i])
            
        else:
            
            for i in range (len(L2)):
                L.append(L1[i]+L2[i])
                
            for i in range (len(L2),len(L1)):
                L.append(L1[i])
                
        return Polynomial(L)
    
    
liste1 = [1,1]
liste2 = [0,1,0,4]
p1 = Polynomial(liste1)
p2 = Polynomial(liste2)
print(str(p2))
print(p1+p2)


