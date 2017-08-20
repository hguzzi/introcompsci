

# riceve in ingresso due liste s1, s2
# restituisce True se le liste sono 
# uguali

def verifica(s1,s2):
    uguali=True
    if(len(s1)!=len(s2)):
        return False
    for i in range(0,len(s1)):
        if(s1[i] != s2[i]):
            uguali=False 
    return uguali
    

    
# restituisce true se le stringhe
# s1 e s2 hanno al massimo k caratter
# diversi

def verifica1(s1,s2,k):
    diversi=0
    for i in range(0,len(s1)):
        if(s1[i]!=s2[i]):
            diversi+=1
    if(diversi>k):
        return False
    else: return True
    
#sasso sosta

def verificaanagramma(s1,s2):
        uguali=True
        for x in s1:
            if (x in s2 == False):
                uguali=False
        for y in s2:
            if (y in s1 == False):
                uguali=False
        return uguali
        
# verifica sottostringa
        
    
    
    
    
    
    
    
    
    