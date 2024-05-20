class Animal:
    def __init__(self, patas):
        self.patas = patas
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.
        __dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
    
    def __str__(self):
        return "Mamífero"

class Ave(Animal):
    def __init__(self, cor_bico, **kw): # kw faz a extensão dos atributos
        self.cor_bico = cor_bico
        super().__init__(**kw)
    def __str__(self):
        return 'ave 42'


class Gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        return("Oi, estou falando")


class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, patas):
        # print(Ornitorrinco.__mro__)
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, patas=patas)
    
    def __str__(self):
        return "Ornitorrinco"


gato  = Gato(patas = 4, cor_pelo= "Marrom")
# print(gato)

ornitorrinco = Ornitorrinco(patas = 2, cor_pelo= "vermelho", cor_bico = "laranja")
print(ornitorrinco)
print(ornitorrinco.falar())