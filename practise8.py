class Book:
    def __init__(self, title: str, author: str, price: float, quantity: float):
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

    def apply_discount(self, discount_percentage):
        self.price = self.price * (1 - discount_percentage / 100)
        return self.price

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
        else:
            print('No available book.')

    def __str__(self):
        return f"Title: '{self.title}', Author: '{self.author}', Price: '{self.price}', Quanity: '{self.quantity}'"


class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def search(self, query):
        for book in self.books:
            if book.title == query or book.author == query:
                return book

    def calculate_total_price(self, book: Book):
        total_price = 0
        for book in self.books:
            total_price += book.price * book.quantity
            return total_price


book1 = Book("Mein Kampf", "Austian artist", 1488, 7)
book2 = Book("1984", "George Orwell", 11, 9)
book3 = Book("Бомжі Донбасу", "Oleksiy Chupa", 300, 43)

print(book2)

bookstore = BookStore()
bookstore.add_book(book1)
bookstore.add_book(book2)
bookstore.add_book(book3)

print(bookstore.calculate_total_price(book1))
print(bookstore.search("Бомжі Донбасу"))
print(book2.apply_discount(20))
book1.sell(6)
print(book1)