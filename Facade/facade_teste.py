       ---Cenário--- 
Um sistema de cinema que combina
múltiplos subsistemas, como seleção
de filmes, assentos e pagamentos.

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
