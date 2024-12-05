from abc import ABC, abstractmethod

# Produto abstrato
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass

# Produto concreto
class ConcreteProductA(Product):
    def operation(self):
        return "Produto A criado."
