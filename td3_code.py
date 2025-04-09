# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 14:58:29 2025

@author: maxjo_ceqfzal
"""



class Tree:
    
    
    def __init__(self, label, *children):
        
        self.__label = label
        self.__children = children
        
    def label(self):
        
        return self.__label
    
    def children(self):
        
        return tuple(self.__children)
    
    def nb_children(self):
        
        return len(self.__children)
    
    def child(self, i):
        
        return self.children()[i]
    
    def is_leaf(self):
        
        if self.nb_children() == 0:
            return True
        else:
            return False
        
    def depth(self):
        
        if self.is_leaf():
            return 0
        
        else:
            Child = Tree(self.child(0))
            return 1+Child.depth()

    def __str__(self):
        
        arbre = self.label()
        arbre += self.children()
        
        return arbre
