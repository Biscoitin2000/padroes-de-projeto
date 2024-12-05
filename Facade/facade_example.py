# Subsistemas individuais

class SistemaDeSom:
    def ligar(self):
        print("Sistema de som ligado.")

    def desligar(self):
        print("Sistema de som desligado.")

class SistemaDeIluminacao:
    def ligar(self):
        print("Iluminação ligada.")

    def desligar(self):
        print("Iluminação desligada.")

class Projetor:
    def ligar(self):
        print("Projetor ligado.")

    def desligar(self):
        print("Projetor desligado.")

class Tela:
    def levantar(self):
        print("Tela levantada.")

    def abaixar(self):
        print("Tela abaixada.")


# O Facade

class CinemaFacade:
    def __init__(self):
        self.som = SistemaDeSom()
        self.iluminacao = SistemaDeIluminacao()
        self.projetor = Projetor()
        self.tela = Tela()

    def iniciarFilme(self):
        print("Iniciando o filme...")
        self.som.ligar()
        self.iluminacao.desligar()
        self.projetor.ligar()
        self.tela.levantar()

    def finalizarFilme(self):
        print("Finalizando o filme...")
        self.som.desligar()
        self.iluminacao.ligar()
        self.projetor.desligar()
        self.tela.abaixar()


# Cliente

def main():
    cinema = CinemaFacade()
    
    # Inicia o filme
    cinema.iniciarFilme()

    print("\nAssistindo ao filme...\n")

    # Finaliza o filme
    cinema.finalizarFilme()

if __name__ == "__main__":
    main()
