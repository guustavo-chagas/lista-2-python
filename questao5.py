class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Meu nome é {self.nome} e eu tenho {self.idade} anos.")
