class Restaurante:
    def __init__(self, nome, endereco, receita):
        self.nome = nome
        self.endereco = endereco
        self.receita = receita

    def mostrar_nome(self):
        print(self.nome)

    def mostrar_endereco(self):
        print(self.endereco)

    def mostar_receita(self):
        print(self.receita)

    def ordem(self, quantia):
        self.receita += quantia

r1 = Restaurante("Pizzaria 123", "rua da esperança", 16)
r1.mostar_receita()

r1.ordem(200)
r1.ordem(500)
r1.mostar_receita()

