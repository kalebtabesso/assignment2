from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    year: int
    price: float

    def discounted_price(self, discount: float) -> float:
        return self.price * (1 - discount)

# Example usage
if __name__ == "__main__":
    book = Book(title="1984", author="George Orwell", year=1949, price=20.0)
    print(f"Original price of '{book.title}' by {book.author}: ${book.price}")
    discount = 0.1  # 10% discount
    print(f"Discounted price: ${book.discounted_price(discount)}")
