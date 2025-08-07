class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

list_books = []

def add_books():
    try:
        title = input("Ingrese el titulo del libro: ")
        author = input("Ingrese el autor del libro: ")
        year = int(input("Ingrese el año de lanzamiento de libro: "))
    except ValueError:
        print("El valor ingresado es incorrecto\n")
    except Exception as e:
        print(F"Error inesperado: {e} \n")

def show_books():
    if not list_books:
        print("No hay libros registrados aún.\n")
    else:
        i = 0
        print("\nLibros registrados:")
        for book in list_books:
            print(f"{i+1}- Titulo: {book.title} - Autor: {book.author} - Añor de publicación: {book.year}")
    print()

def remove_books():
    if not list_books:
        print("No hay libros registrados.\n")
    else:
        book_user = input("Ingrese el titulo de libro que desea eliminar: ").lower()
        if book_user == book.title.lower():
            list_books.remove(book_user)
        else:
            print("El libro no existe\n")