# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 14:52:49 2025

@author: maxjo_ceqfzal
"""

from tkinter import Tk,Canvas,Button

root = Tk()
can = Canvas(root,width=500,height=200)
can.grid(column=1,row=1)
h = 20
w = 20
fils = 4


def read_word(can,mot,h,w,y0,couleur):
    
    x0 = 1
    
    for car in mot:
        
        if car == 'H':
            x1 = x0+h
            y1 = y0
            can.create_line(x0,y0,x1,y1,fill=couleur)
            x0 = x1
            y0 = y1
        
        if car == 'U':
            x1 = x0+h
            y1 = y0-w
            can.create_line(x0,y0,x1,y1,fill=couleur)
            x0 = x1
            y0 = y1
        
        if car == 'D':
            x1 = x0+h
            y1 = y0+w
            can.create_line(x0,y0,x1,y1,fill=couleur)
            x0 = x1
            y0 = y1


'''read_word(can, 'HUHHDUH', h, w, 100, 'blue')'''


def entrelacs(L,fils):
    
    assert fils <= 8
    
    #   1° partie : création liste des mots dessinables
    
    mots = ['H']*fils
    indices = {}
    
    for i in range (fils):
        indices[i]=i
    
    for melee in L:
        
        for i in range (fils):
            
            ind = indices[i]
            
            if ind == melee:
                mots[i] += 'D'
                indices[i] += 1
            
            elif ind == melee+1:
                mots[i] += 'U'
                indices[i] -= 1
            
            else:
                mots[i] += 'H'
            
            mots[i] += 'H'
    
    #   2° partie : dessin des lignes brisées
    
    couleurs = ['blue','red','black','green','orange','brown','pink','grey']
    
    for i in range (fils):
        
        read_word(can, mots[i], h, w, i*w+10, couleurs[i])



entrelacs( [2,1,1,0,2],4 )
root.mainloop()
        


