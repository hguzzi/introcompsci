def fatt_ricorsivo(n):
    if(n==0):
        return 1
    else: 
        #print(n,"* fatt",n-1)
        return n*int(fatt_ricorsivo(n-1))


        
        
        
def fib_ric(n):
    if(n==0):
        return 0
    if (n==1):
        return 1
    else: return fib_ric(n-1)+fib_ric(n-2)

def massimoRicorsivo(lista):
    if(len(lista)==1):
        return lista[0]
    else:
        if(lista[0]> massimoRicorsivo(lista[1:])):
            return lista[0]
        else: 
            return massimoRicorsivo(lista[1:])
            
            
            
            
            
            
            
           
DRAFT
7.3 esempi di programmi ricorsivi
def massimoIterativo(lista):
massimo=lista[0]
for y in lista:
if y>massimo:
massimo=y
return massimo
def massimoRicorsivo(lista):
if(len(lista)==1):
return lista[0]
else:
if(lista[0]>massimoRicorsivo(lista[1:])):
return lista[0]
else: return massimoRicorsivo(lista[1:])
print(massimoIterativo([100,21,3,104,33,44]))
print(massimoRicorsivo([100,21,3,104,33,44]))


[100,21,21,104,21,44] 21


# scrittura del caso base


def calcoloOccRic(item,lista):
    if(len(lista)==1):
        if(lista[0]==item):
            return 1
        else: return 0
        else:
            if(lista[0]==item):
                return 1+calcoloOccRic(item,lista[1:])
            else:
                return 0+calcoloOccRic(item,lista[1:])









    
    
#print(fatt_ricorsivo(6)) 
#print(fib_ric(10))   