# -*- coding: utf-8 -*-
"""
Created on Wed May  7 14:57:15 2025

@author: maxjo_ceqfzal
"""


from tkinter import Tk,Canvas,Button


class App:
    
    
    def __init__(self, data1, data2):
        
        self.root = Tk()
        self.longueur = 500
        self.hauteur = 200
        self.can = Canvas(self.root,width=self.longueur,height=self.hauteur)
        self.can.grid(column=1,row=1)
        self.data = Data(data1,data2)
    
    def run_forever(self):
    
        self.root.mainloop()
    
    def redraw(self):
        
        self.root.destroy()
        
    def read_word(self,mot,y0,couleur):
        
        x0 = 1
        h = self.hauteur // 10
        w = self.longueur // 20
        
        for car in mot:
            
            if car == 'H':
                x1 = x0+h
                y1 = y0
                self.can.create_line(x0,y0,x1,y1,fill=couleur)
                x0 = x1
                y0 = y1
            
            if car == 'U':
                x1 = x0+h
                y1 = y0-w
                self.can.create_line(x0,y0,x1,y1,fill=couleur)
                x0 = x1
                y0 = y1
            
            if car == 'D':
                x1 = x0+h
                y1 = y0+w
                self.can.create_line(x0,y0,x1,y1,fill=couleur)
                x0 = x1
                y0 = y1
    
    
    def read_words(self):
        
        mots = self.data.entrelacs()
        
        couleurs = ['blue','red','black','green','orange','brown','pink','grey']
        
        w = self.longueur // 20
        
        for i in range (self.data.fils):
            self.read_word(mots[i], i*w+10, couleurs[i])



class Data:
    
    
    def __init__(self, L, n):
        
        self.croisements = L
        self.fils = n
        
    def entrelacs (self):
        
        fils = self.fils
        croisements = self.croisements
        
        assert fils <= 8
                
        mots = ['H']*fils
        indices = {}
        
        for i in range (fils):
            indices[i]=i
        
        for melee in croisements:
            
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
        
        return mots
         
        
        
        
        
        
if __name__ == "__main__":
    
    app = App([2,1,1,0,2],4)
    app.read_words()
    app.run_forever()
