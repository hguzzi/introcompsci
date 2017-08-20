class FiguraGeometrica:
    def __init__(self,n):
        self.nome=n
    def getNome(self):
        return self.nome

class Triangolo(FiguraGeometrica):
    def __init__(self,n,l1,l2,l3):
        super().__init__(n)
        self.lato1=l1
        self.lato2=l2
        self.lato3=l3
    def perimetro(self):
        return self.lato1+self.lato2+self.lato3
    def nome(self):
        return self.getNome()

t=Triangolo(50,10,20,30)
a=t.nome()

    
