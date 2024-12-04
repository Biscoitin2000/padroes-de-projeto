 --- PULL REQUEST ---

-FORMAS DE DESCRIÇÃO DO PADRÃO-

# (nome do padrão);
EX: Facade

# Conceito
EX: O Facade atua como uma fachada (ou "frente") para um subsistema complexo, expondo uma 
interface simplificada para o cliente enquantomantém a complexidade oculta.

# Problema que Resolve;
EX: Facilita a interação com sistemas complexos ao oferecer uma interface única e clara, evitando que
os clientes lidem diretamente com várias interfaces e classes.


# Quando Usar;
EX:- Para simplificar o uso de um subsistema complexo.
   - Quando deseja criar uma abstração de nível mais alto para um conjunto de funcionalidades relacionadas.
   - Quando deseja reduzir o acoplamento entre clientes e classes internas de um subsistema.

# Vantagens;
EX: - Simplifica o uso de subsistemas complexos.
    - Reduz o acoplamento entre o cliente e os componentes internos do subsistema.
    - Permite alterar os subsistemas sem impactar o cliente.

 # Desvantagens
EX: - Pode se tornar um ponto de risco único (single point of failure) se concentrar muita lógica.
    - Pode esconder detalhes importantes de funcionamento do subsistema.   


-REQUISITOS PARA A IMPLEMENTAÇÃO DO PADÃO NO REPOSITÓRIO- 
Recriar em liguagem de programação py(pyton) um similar de seu padrão para sua ultilização em nosso repositório, fazer testes e verificar sua coerencia com o padrão desenvolvido pelo mesmo.

EXEMPLO DE UM DE NOSSOS PADRÃO:

# Subsystem A: Movie Selector
class MovieSelector:
    def select_movie(self, movie):
        print(f"Movie '{movie}' selected.")

# Subsystem B: Seat Manager
class SeatManager:
    def reserve_seat(self, seat_number):
        print(f"Seat {seat_number} reserved.")

# Subsystem C: Payment Processor
class PaymentProcessor:
    def process_payment(self, amount):
        print(f"Payment of ${amount} processed.")

# Facade
class CinemaFacade:
    def __init__(self):
        self.movie_selector = MovieSelector()
        self.seat_manager = SeatManager()
        self.payment_processor = PaymentProcessor()

    def book_ticket(self, movie, seat_number, amount):
        self.movie_selector.select_movie(movie)
        self.seat_manager.reserve_seat(seat_number)
        self.payment_processor.process_payment(amount)
        print("Booking successful!")

# Client Code
if __name__ == "__main__":
    # Example usage of the Facade
    cinema = CinemaFacade()
    cinema.book_ticket("Inception", 42, 15.00)



-DETALHES DO OQUE INCLUIR NA DOCUMENTAÇÃO-

Repetindo os passos amostrados anteriormente na pasta com seu projeto padrão deve conter a DESCRIÇÃO DE SEU PADRÃO cojunto com seu UML DO PADRÃO (EM DIAGRAMA), e por fim anexado na pasta ter um TESTE DE SEU PADRÃO EM PY (PYTON) conforme amostrado a baixo
EX:
- padroes-de-projeto/
- - - Facade/                       # Pasta para o padrão Facade
- - - - - - UML_Facade              # Diagrama UML do padrão
- - - - - - facade_example.py       # Exemplo prático do padrão em Python


 
 -ESTRUTURA DO REPOSITÓRIO-
 
_ padroes-de-projeto/
 __    README.md‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  # Introdução geral e visão do projeto
   __  CONTRIBUTING.md‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ # Diretrizes para contribuição
     __Factory/‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ # Pasta para o padrão Factory
       ___    UML_Factory‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ # Diagrama UML do padrão
        ___   factory_example.py‎ ‎ ‎ ‎ # Exemplo prático do padrão em Python
     Singleton/‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎‎# Pasta para o padrão Singleton
           UML_Singleton‎‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎‎# Diagrama UML do padrão
           singleton_example.py‎ ‎ # Exemplo prático do padrão em Python
     Adapter/‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ # Pasta para o padrão Adapter
           UML_Adapter.png‎ ‎ ‎ ‎ ‎ ‎ ‎ # Diagrama UML do padrão
           adapter_example.py‎ ‎ ‎ ‎ ‎# Exemplo prático do padrão em Python
     Visitor/‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ # Pasta para o padrão Visitor
           UML_Visitor           # Diagrama UML do padrão
           visitor_example.py    # Exemplo prático do padrão em Python
     Facade/                     # Pasta para o padrão Facade
           UML_Facade            # Diagrama UML do padrão
           facade_example.py     # Exemplo prático do padrão em Python
     docs/                       # Pasta opcional para documentação geral
    

  
