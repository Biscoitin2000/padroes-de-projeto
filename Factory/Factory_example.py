class Veiculo:
    """Interface comum para todos os veículos."""
    def descricao(self):
        raise NotImplementedError("Subclasses devem implementar o método descricao().")

class Carro(Veiculo):
    def __init__(self, modelo):
        self.modelo = modelo

    def descricao(self):
        return f"Este é um carro. Modelo: {self.modelo}"

class Moto(Veiculo):
    def __init__(self, cilindrada):
        self.cilindrada = cilindrada

    def descricao(self):
        return f"Esta é uma moto. Cilindrada: {self.cilindrada}"

class VeiculoFactory:
    """Factory para criar objetos do tipo Veiculo."""
    @staticmethod
    def criar_veiculo(tipo, especificacao):
        if tipo == "carro":
            return Carro(especificacao)
        elif tipo == "moto":
            return Moto(especificacao)
        else:
            raise ValueError(f"Tipo de veículo desconhecido: {tipo}")

# Exemplo de uso
if __name__ == "__main__":
    # Criando veículos usando a factory
    meu_carro = VeiculoFactory.criar_veiculo("carro", "Sedan")
    minha_moto = VeiculoFactory.criar_veiculo("moto", "600cc")

    # Mostrando as descrições
    print(meu_carro.descricao())
    print(minha_moto.descricao())

