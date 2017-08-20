# l'applicazione chiede all'utente
# di inserire una serie di numeri
# terminata da 0
# terminato l'inserimento
# chiede di calcolare media/massimo


def inserisci(lista):
    print("Benvenuto, inserisci i valori e termina con zero")
    while(True):
        a=int(input("Numero"))
        if(a!=0):
            lista.append(a)
        else: break

def media(l):
    somma=0.0
    media=0.0
    for x in l:
        somma+=x
    media=somma/len(l)
    return media
    
def massimo(l):
    massimotemporaneo=l[0]
    for x in l:
        if x>massimotemporaneo:
            massimotemporaneo=x
    return massimotemporaneo
            
def main():
    l=list()
    inserisci(l)
    print("inserisci media (0) o massimo (1)")
    sc=int(input("scegli"))
    if(sc==0):
        print(media(l))
    else: print(massimo(l))

main()
    








