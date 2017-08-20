def verificatuttizero(M):
    condizione=True
    for x in M:
        for y in x:
            if(y!=0):
                condizione=False
    return condizione


def verificatuttiugualik(M,k):
    condizione=True
    for x in M:
        for y in x:
            if(y!=k):
                condizione=False
    return condizione


# somma degli elementi di una matrice
# che siano divisibili per 4

def sommadivisibili(m,z):
    somma=0
    for x in m:
        for y in x:
            if(y%z==0):
                somma+=y
    return somma

    
#
l=[12,32,1,10,500]
massimo=
    massimocorrente=12
minimocorrente=1
    
    
    
    
    def trovamassimo(l):
    massimocorrente=l[0]
        for x in l:
            if(massimocorrente<x):
                massimocorrente=x
    return massimocorrente

def trovamassimo2(m):
    massimocorrente=m[0][0]
    for x in m:
        for y in x:
            if (massimocorrente<y):
                massimocorrente=y
    return massimocorrente

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
