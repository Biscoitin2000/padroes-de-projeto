# Definindo a interface para os produtos
class Veiculo:
    def tipo(self):
        # Método abstrato para ser implementado pelas subclasses
        raise NotImplementedError("Método 'tipo' não implementado.")

# Produtos concretos: classes que implementam a interface Veiculo

class Carro(Veiculo):
    def tipo(self):
        # Implementação concreta para o tipo de veículo Carro
        return "Carro"

class Moto(Veiculo):
    def tipo(self):
        # Implementação concreta para o tipo de veículo Moto
        return "Moto"

# Fábrica de veículos: cria os objetos de forma centralizada

class FabricaVeiculo:
    def criar_veiculo(self, tipo_veiculo):
        # Método de fábrica que cria o veículo dependendo do tipo
        if tipo_veiculo == "carro":
            return Carro()  # Retorna um objeto Carro
        elif tipo_veiculo == "moto":
            return Moto()  # Retorna um objeto Moto
        else:
            raise ValueError(f"Veículo de tipo '{tipo_veiculo}' não reconhecido.")

# Cliente: interage com a fábrica sem se preocupar com a criação dos objetos

def cliente(fabrica, tipo_veiculo):
    veiculo = fabrica.criar_veiculo(tipo_veiculo)  # Chama a fábrica para criar o objeto
    print(f"Veículo criado: {veiculo.tipo()}")  # Exibe o tipo do veículo criado

# Uso do padrão Factory

fabrica = FabricaVeiculo()  # Instanciando a fábrica

cliente(fabrica, "carro")  # Saída: Veículo criado: Carro
cliente(fabrica, "moto")   # Saída: Veículo criado: Moto
