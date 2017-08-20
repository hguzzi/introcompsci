# #
# #
# #
# Vogliamo verificare se data 
# una lista di liste (matrice)
# tutte le righe hanno la somma degli elementi pari a k
k=10
[ 4 , 3, 3]
[ 4 , 4, 2]
[ 5, 5 , 5]


def somma(vet):
    somma=0
    for x in vet:
        somma+=x
    return somma

def controllarighe(m,k):    
    sommauguali=True
    for x in m:
        if(somma(x)!=k):
            sommauguali=False
            
non esiste nessuna riga 
con element dispari


data una matrice m verificare
che ogni riga  abbia al massimo 2 
valori uguali a zero





