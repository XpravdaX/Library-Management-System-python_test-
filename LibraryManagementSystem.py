import datetime

class Book:
    def __init__(self, title, author, isbn, publication_year, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.copies = copies
        self.available_copies = copies

    def __str__(self):
        return f"{self.title} автор {self.author} (ISBN: {self.isbn})"

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_borrowed = []

    def __str__(self):
        return f"{self.name} (ID: {self.member_id})"

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга добавлена: {book}")

    def add_member(self, member):
        self.members.append(member)
        print(f"Читатель добавлен: {member}")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member:
            print("Читатель не найден.")
            return

        if not book:
            print("Книга не найдена.")
            return

        if book.available_copies > 0:
            book.available_copies -= 1
            member.books_borrowed.append(book)
            transaction = {
                "type": "выдача",
                "member": member,
                "book": book,
                "date": datetime.datetime.now()
            }
            self.transactions.append(transaction)
            print(f"{member.name} взял книгу {book.title}")
        else:
            print("Извините, эта книга недоступна.")

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if not member:
            print("Читатель не найден.")
            return

        if not book:
            print("Книга не найдена.")
            return

        if book in member.books_borrowed:
            book.available_copies += 1
            member.books_borrowed.remove(book)
            transaction = {
                "type": "возврат",
                "member": member,
                "book": book,
                "date": datetime.datetime.now()
            }
            self.transactions.append(transaction)
            print(f"{member.name} вернул книгу {book.title}")
        else:
            print(f"{member.name} не брал эту книгу.")

    def display_available_books(self):
        print("Доступные книги:")
        for book in self.books:
            if book.available_copies > 0:
                print(f"{book} - Доступно экземпляров: {book.available_copies}")

    def display_member_books(self, member_id):
        member = self.find_member(member_id)
        if member:
            print(f"Книги, взятые читателем {member.name}:")
            for book in member.books_borrowed:
                print(book)
        else:
            print("Читатель не найден.")

# Пример использования
library = Library()

# Добавление книг
book1 = Book("Война и мир", "Лев Толстой", "9785170880805", 1869, 5)
book2 = Book("Преступление и наказание", "Фёдор Достоевский", "9785171147426", 1866, 3)
book3 = Book("Мастер и Маргарита", "Михаил Булгаков", "9785170878895", 1967, 4)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Добавление читателей
member1 = Member("Иван Петров", "M001")
member2 = Member("Анна Сидорова", "M002")

library.add_member(member1)
library.add_member(member2)

# Выдача и возврат книг
library.borrow_book("M001", "9785170880805")
library.borrow_book("M002", "9785171147426")
library.return_book("M001", "9785170880805")

# Отображение доступных книг и книг, взятых читателем
library.display_available_books()
library.display_member_books("M002")
