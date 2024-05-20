# capacidade de uma classe filha herdar ou derivar características e comportamnetos da classe pai
# representa os relacionamentos do mundo real
# reutilizaçõo de código
# é de matureza transitiva, porém dificulta a manutenção
# herança simples é quando uma classe filha herda apenas de uma classe pai
# herança múltpla é quando uma classe filha herda de várias classes pai

class Veiculo: 
    def __init__(self, modelo, ano, fabricante, placa):
        self.modelo = modelo
        self.ano = ano
        self.fabricante = fabricante
        self.placa = placa
    
    def ligar_motor(self):
        print("Ligando o motor")
    
    def __str__(self):
         return f"Modelo: {self.modelo}, Ano: {self.ano}, Fabricante: {self.fabricante}, Placa: {self.placa}"
    
    
class Motocicleta (Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, modelo, ano, fabricante, placa, carregado):
        super().__init__(modelo, ano, fabricante, placa,) # sobrescrevendo o método
        self.carregado = carregado

    def esta_carregado(self):
        print(f'{'Sim' if self.carregado else 'Não'} estou carregado')

moto = Motocicleta(modelo="CB300", ano=2012, fabricante="Honda", placa="FBO1234" )
carro = Carro("Astra", 2001, "Chevrolet", "RIR6952")
caminhao = Caminhao("Bi-Motor", 2005, "Mercedez", "KIK8745", False)

print(caminhao)
print(moto)
print(carro)