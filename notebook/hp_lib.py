# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 13:11:05 2021

@author: Celian
"""
from networkx import all_pairs_shortest_path_length

def degree_of_separation(G):
    dist=all_pairs_shortest_path_length(G)
    sep_degree=0
    n=0
    for d in dist:
        k1=d[0]
        for k2 in d[1].keys():
            if(k1!=k2):
                sep_degree+=d[1][k2]
                n+=1
    return sep_degree/n
        