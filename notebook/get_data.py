# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 19:16:12 2021

@author: Celian
"""

import csv
import math 

f_name = "C:/Users/Celian/Desktop/CAPES_INFO/Dossier Oral/CAPES_NSI/data/perso_list_with_desc_clean.csv"
file = open(f_name,encoding="utf-8")
persDetails = list(csv.DictReader(file,delimiter=";"))

f_name = "C:/Users/Celian/Desktop/CAPES_INFO/Dossier Oral/CAPES_NSI/data/edges_clean0.csv"
file = open(f_name)
edges= list(csv.DictReader(file,delimiter=";"))
nodes = []

for pers in persDetails:
    id_=pers["\ufeffid"]
    label_=pers["Nom"]
    size_=(math.log(int(pers["nb_occ"]))*5)+1
    if(pers["type"]=="sorcier"):
        group_="black"
    elif(pers["type"]=="moldu"):
        group_="pink"
    elif(pers["type"]=="creature"):
        group_="grey"
    elif(pers["Maison"]=="Serpentard"):
        group_="green"
    elif(pers["Maison"]=="Gryffondor"):
        group_="red"
    elif(pers["Maison"]=="Poufsouffle"):
        group_="yellow"
    elif(pers["Maison"]=="Serdaigle"):
        group_="blue"
        
    nodes.append({"id":id_,"label":label_,"color":group_,"size":size_})
    
edges2=[]
for e in edges:
    if(int(e["value"])>10):
        edges2.append({"from":e["from"],"to":e["to"]}) 
    