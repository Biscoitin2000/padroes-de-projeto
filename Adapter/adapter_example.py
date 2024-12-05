# Adaptee: Classe existente com uma interface incompatível
class Retangulo:
    def exibir(self):
        return "Desenhando um retângulo!"

# Target: Interface esperada pelo cliente
class FormaGeométrica:
    def desenhar(self):
        raise NotImplementedError("Este método deve ser implementado!")

# Adapter: Adapta a interface de Retangulo para FormaGeométrica
class RetanguloAdapter(FormaGeométrica):
    def __init__(self, retangulo: Retangulo):
        self.retangulo = retangulo

    def desenhar(self):
        # Traduz a chamada do cliente para o método exibir()
        return self.retangulo.exibir()

# Cliente: Código que espera usar a interface de FormaGeométrica
def cliente_desenha_forma(forma: FormaGeométrica):
    print(forma.desenhar())

# Testando o Adapter
if __name__ == "__main__":
    retangulo = Retangulo()  # Instância da classe existente
    adaptador = RetanguloAdapter(retangulo)  # Adaptador para interface esperada
    cliente_desenha_forma(adaptador)  # Cliente funciona com o adaptador
