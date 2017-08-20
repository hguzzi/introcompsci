class Frazione:
    def __init__(self,num,den):
        self.numeratore=num
        self.denominatore=den
    def getNumeratore(self):
        return self.numeratore
    def getDenominatore(self):
        return self.denominatore
    def __eq__(self,other):
        if ( self.numeratore==other.getNumeratore() and self.denominatore==other.getDenominatore() ):
            return True
        else: return False
       
        
f1=Frazione(2,3)
f2=Frazione(2,3)
if (f1==f2):
    print("uguali")        




