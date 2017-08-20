#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:02:40 2016
) Scrivere un programma ContaFamiglie.py
 che conti il numero di famiglie il cui 
 reddito è inferiore ad un certo valore.
 Il programma legge un intero k da tastiera
 e crea quindi un array per la
 memorizzazione dei valori. 
 Legge quindi i valori che rappresentano
 i valori dei redditi ed un altro array 
 che memorizza i cognomi delle famiglie. 
 A posizione uguale corrisponde una 
 famiglia ed il suo reddito. Trova 
 quindi il più elevato tra questi redditi
 , quindi trova le famiglie il cui 
 reddito è inferiore al 10 percento 
 del reddito massimo , stampa 
il numero di famiglie e i loro cognomi.
@author: pietrohiramguzzi
"""

def inserisciinformazioni(redditi,cognomi,k):
    contatore=0
    while(contatore<k):
        redditi.append(float(input("ins reddito")))
        cognomi.append(input("ins cognome"))
        contatore=contatore+1

def trovamassimo(redditi):
    posmaxcorrente=0
    for i in range(0,len(redditi)):
        if redditi[i]>redditi[posmaxcorrente]:
            posmaxcorrente=i
    return posmaxcorrente

def trovaestampa(redditi,cognomi,posmax):
    delta=redditi[posmax]*0.1
    sogliareddito=redditi[posmax]-delta
    contatore=0
    for i in range(0,len(redditi)):
        if reddito[i] < sogliareddito:
            print(cognomi[i])
            contatore+=1
    print("Famiglie reddito inferiore"+
          contatore)
def main():
    
