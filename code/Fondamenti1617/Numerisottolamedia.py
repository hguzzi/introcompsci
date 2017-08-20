#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 09:17:34 2016

@author: pietrohiramguzzi

Scrivere un programma NumeriSottolaMedia.py 
che conti il numero dei giorni 
in cui la temperatura è al di sotto 
della media. 
Il programma legge 10 valori di 
temperatura (float) 
da tastiera e li memorizza in un array. 
Quindi calcola la media e visualizza il 
numero dei giorni in cui la temperatura è al 
di sotto della media. 

"""

def inseriscivalori(l):
    contatore=0
    while(contatore<10):
        l.append(int(input("inserisci valore")))
        contatore+=1

def calcolamedia(l):
    somma=0.0
    for x in l:
        somma+=x
    media=somma/len(l)
    return media

def stampavalorisottomedia(l,m):
    for x in l:
        if(x<m):
            print(x)
def main():
    l=list()
    inseriscivalori(l)
    med=calcolamedia(l)
    print("Media",med)
    stampavalorisottomedia(l,med)

main()
    
    