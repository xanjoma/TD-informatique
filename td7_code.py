# -*- coding: utf-8 -*-
"""
Created on Wed May 14 14:55:06 2025

@author: maxjo_ceqfzal
"""

from tkinter import Tk,Canvas
from random import random as rd


class Graphe :
    
    def __init__(self,graph):
        self.root = Tk()
        self.long = 600
        self.haut = 600
        self.can = Canvas(self.root,width=self.long,height=self.haut)
        self.can.grid(column=1,row=1)
        self.graph = graph
        self.nb_som = len(graph)
        self.norm = 50
        self.positions = [ (self.long*rd(),self.haut*rd())
                          for _ in range (self.nb_som) ]
        self.vitesses = [ ( self.long/self.norm*(0.5-rd()),
                           self.haut/self.norm*(0.5-rd()) )
                         for _ in range (self.nb_som) ]
        self.root.bind("<f>",lambda e:self.mouvement())
        
    def run_forever(self):
        self.root.mainloop()
    
    def mouvement(self):
        vit = self.vitesses
        pos = self.positions
        for som in range(self.nb_som):
            x0 = pos[som][0]
            x1 = int(vit[som][0])
            y0 = pos[som][1]
            y1 = int(vit[som][1])
            self.positions[som] = (x0+x1,y0+y1)
        self.draw()
    
    def draw(self):
        self.can.delete('all')
        pos = self.positions
        for i in range(self.nb_som):
            for j in self.graph[i]:
                self.can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
        for (x, y) in pos:
            self.can.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4")
            
   
            
graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]
graph = Graphe(graph)
graph.draw()
graph.run_forever()
