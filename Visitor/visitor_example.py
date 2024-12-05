from abc import ABC, abstractmethod

# Elementos da Interface
class LibraryItem(ABC):
    @abstractmethod
    def accept(self, visitor):
        """Aceita um visitante."""
        pass

# Elementos Estruturais
class Book(LibraryItem):
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def accept(self, visitor):
        return visitor.visit_book(self)

class CD(LibraryItem):
    def __init__(self, title, price, artist):
        self.title = title
        self.price = price
        self.artist = artist

    def accept(self, visitor):
        return visitor.visit_cd(self)

# Interface do Visitor
class Visitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        """Visita um objeto do tipo Book."""
        pass

    @abstractmethod
    def visit_cd(self, cd):
        """Visita um objeto do tipo CD."""
        pass

# Estutura do Visitor
class PriceCalculatorVisitor(Visitor):
    def __init__(self):
        self.total_price = 0

    def visit_book(self, book):
        print(f"Calculando preço do livro: {book.title} - ${book.price:.2f}")
        self.total_price += book.price

    def visit_cd(self, cd):
        print(f"Calculando preço do CD: {cd.title} - ${cd.price:.2f}")
        self.total_price += cd.price

    def get_total_price(self):
        return self.total_price

# Codgo Cliente
if __name__ == "__main__":
    # Coleção de itens na biblioteca
    items = [
        Book("O Hobbit", 19.99, "J.R.R. Tolkien"),
        CD("Dark Side of the Moon", 39.99, "Pink Floyd"),
        Book("Dom Quixote", 29.99, "Miguel de Cervantes"),
        CD("Back in Black", 49.99, "AC/DC")
    ]

    # Visitante para calcular o preço
    price_calculator = PriceCalculatorVisitor()

    # Aplicando o visitante em cada item
    for item in items:
        item.accept(price_calculator)

    # Resultado final
    print(f"\nPreço total dos itens: ${price_calculator.get_total_price():.2f}")
