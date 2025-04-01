# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 14:51:45 2025

@author: maxjo_ceqfzal
"""




"""
Exercice 1/2
"""


#chargement_dico

liste=list()
f = open('frenchssaccent.dic','r')

for ligne in f:
    liste.append(ligne[0:len(ligne)-1])
    
f.close()


#fonction transforme liste tirage en dico tirage

def liste_vers_dico(L):
    
    dico={}
    
    for elt in L:
        if elt not in dico:
            dico[elt]=1
        else:
            dico[elt]+=1
    
    return dico


#fonction mot valide pour être solution

def mot_valide(mot,tirage):
    
    tirage=liste_vers_dico(tirage)
    
    for carac in mot:
        if carac not in tirage:
            return False
        else:
            tirage[carac]-=1
    
    for lettre in tirage:
        if tirage[lettre]<0:
            return False
    
    return True


#fontion renvoyant les mots possibles à partir du tirage

def mots_possibles(tirage):
    
    mots_pos=[]
    
    for mot in liste:
        if mot_valide(mot,tirage):
            mots_pos.append(mot)
    
    return mots_pos


#fonction trouver mot le plus long

def mot_plus_long(tirage):
    
    mots_pos=mots_possibles(tirage)
    max=(0,'')
    
    for mot in mots_pos:
        lg = len(mot)
        if lg>max[0]:
            max=(lg,mot)
    
    return max[1]
            

#tests exo 2

tirage1 = ['b', 'p', 'd', 'w', 's', 'y', 'w', 'i']
tirage2 = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']

print(mot_plus_long(tirage1))
print(mot_plus_long(tirage2))


"""
Exercice 3
"""


#dictionnaire décrivant la valeur des lettres

val_lettres={'a':1, 'e':1, 'i':1, 'l':1, 'n':1, 'o':1, 'r':1, 's':1, 't':1, 'u':1,
             'd':2, 'g':2, 'm':2,
             'b':3, 'c':3, 'p':3,
             'f':4, 'h':4, 'v':4,
             'j':8, 'q':8,
             'k':10, 'w':10, 'x':10, 'y':10, 'z':10}


#fonction caculant score d'un mot

def score(mot):
    
    score = 0
    
    for lettre in mot:
        score+=val_lettres[lettre]
        
    return score


#fonction qui trouve le mot à plus grand score

def max_score(liste_mots):
    
    max = (0,'')
    
    for mot in liste_mots:
        points = score(mot)
        if points>max[0]:
            max=(points,mot)
            
    return max


#tests exo 3

mot1='a'
mot2='lettre'
mot3='scrabble'
liste1_mots=['rte', 'ver', 'ce', 'etc', 'cet', 'ex', 'cr', 'et', 'ter', 'te', 'ct']

print(score(mot1))
print(score(mot2))
print(score(mot3))
print(max_score(liste1_mots))


"""
Exercice 4
"""


#identification joker dans un tirage

def joker_dans_tirage(tirage):
    
    for elt in tirage:
        if elt=='?':
            return True
    return False


#fonction mot valide pour être solution
            
def mot_valide_v2(mot,tirage):
    
    tirage=liste_vers_dico(tirage)
    
    bool_joker=joker_dans_tirage(tirage)
    joker=[]    #lettres remplacées par le joker
    
    for carac in mot:
        
        if carac in tirage:
            tirage[carac]-=1
        else:
            if bool_joker:
                tirage['?']-=1
                joker.append(carac)
            else:
                return (False,[])
    
    for lettre in tirage:
        if tirage[lettre]<0:
            return (False,[])
    
    return (True,joker)


#fontion renvoyant les mots possibles à partir du tirage
#et leurs lettres remplacées par un joker

def mots_possibles_v2(tirage):
    
    mots_pos = []
    joker = joker_dans_tirage(tirage)
    
    if not joker:
        return mots_possibles(tirage)
    
    mots_pos=[]
    
    for mot in liste:
        if mot_valide_v2(mot,tirage)[0]:
            mots_pos.append((mot,mot_valide_v2(mot, tirage)[1]))
            
    return mots_pos
    

#fonction renvoyant le mot avec le plus de score

def score_v2(mot,lettres_joker):
    
    score = 0
    
    for lettre in mot:
        score+=val_lettres[lettre]
    
    for lettre in lettres_joker:
        score-=val_lettres[lettre]
        
    return score
    

#fonction qui trouve le mot à plus grand score

def max_score_v2(liste_mots_jokers):
    
    max = (0,'')
    
    for elt in liste_mots_jokers:
        points = score_v2(elt)
        if points>max[0]:
            max=(points,elt)
            
    return max


#test exo 4

tirage_joker = ['z','x','c','v','r','r','t','?']
mots_pos = mots_possibles_v2(tirage_joker)
print( max_score_v2(mots_pos) )




