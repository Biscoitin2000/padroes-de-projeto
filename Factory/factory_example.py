from abc import ABC, abstractmethod

# Produto abstrato
class Product(ABC):
    @abstractmethod
    def operation(self):
        pass
