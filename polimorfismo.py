# mesmo nome de função mas assinaturas diferentes, sendo usado para tipos diferentes

class Passaro:
    def voar(self):
        print("Voando....")

class Pardal(Passaro):
    def voar(self):
        print("Pardal está voando")
    

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

# exemplo ruim do uso de herança para herdar um método
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando")


def plano_voo(obj):
    obj.voar()


p1 = Pardal()
p2 = Avestruz()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())