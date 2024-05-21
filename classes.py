# características: modelo, ano e valor = atributos
# comportamentos: buzinar, parar e correr(vendas de bicicletas) = métodos
# fazendo teste git
nro_marcha = 1
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18, marcha=1): # método construtor, inicalizador
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marcha = marcha

    def buzinar(self):
        print('Plim plim...')


    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada")

    def correr(self):
        print("Vrummmmm")

    def trocar_marcha(self):
        print("Trocando marcha")
        _self = self

        def _trocar_marcha():
            if nro_marcha > _self.marcha:
                print("Marcha trocada")
            else:
                print("Não foi possível trocar de marcha")


    #def __str__(self):
    #    return f"Bicicleta: cor={self.cor}, modelo{self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.
        __dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
Bicicleta.buzinar(b2)
print(b2.cor)
b2.correr()