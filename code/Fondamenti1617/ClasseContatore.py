# Contatore
# -> DATI 
# -> Operazioni / Funzioni

class Contatore :
    # valore 
    def __init__(self):
        self.valore=0
    def reset(self):
        self.valore=0
    def incrementa(self):
        self.valore=self.valore+1
    def getValore(self):
        return self.valore
    def incrementa2(self,a):
        self.valore=self.valore+a
        
        
### Costruzione dell'oggetto
c=Contatore()
# c Parametro Implicito
c.incrementa()
c.incrementa()
c.incrementa2(6)
c.incrementa2(6)
print(c.getValore())    

