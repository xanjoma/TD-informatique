# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 15:45:58 2025

@author: maxjo_ceqfzal
"""

import unittest
from td3_code import Tree

A = Tree('a')
G = Tree('g', 'a')
F = Tree('f', 'a', 'b')

class TestTree(unittest.TestCase):
    
    def test_label(self):
        
        self.assertEqual(A.label(), 'a')
        self.assertEqual(G.label(), 'g')
        self.assertEqual(F.label(), 'f')
        
    def test_children(self):
        
        self.assertEqual(G.children(), ('a',))
        self.assertEqual(F.children(), ('a','b'))
        
    def test_nb_children(self):
        
        self.assertEqual(A.nb_children(), 0)
        self.assertEqual(G.nb_children(), 1)
        self.assertEqual(F.nb_children(), 2)

    def test_child(self):
        
        self.assertEqual(G.child(0), 'a')
        self.assertEqual(F.child(1), 'b')
        
    def test_is_leaf(self):
        
        self.assertTrue(A.is_leaf())
        self.assertFalse(G.is_leaf())
        self.assertFalse(F.is_leaf())
    
    def test_depth(self):
        
        self.assertEqual(A.depth(), 0)
        self.assertEqual(G.depth(), 1)
        self.assertEqual(F.depth(), 1)

        

if __name__ == '__main__' :
    unittest.main()

    
