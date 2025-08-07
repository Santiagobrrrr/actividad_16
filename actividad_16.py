class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

list_books = []

def add_books(self):
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
        book_found = False
        for book in list_books:
            if book.title.lower() == book_user.lower():
                list_books.remove(book_user)
                book_found = True
                break
            else:
                print(F"El libro {book.title} no existe\n")

while True:
    print(f"-- MENÚ BIBLIOTECA --")
    print(f"1- Añadir libro")
    print(f"2- Mostrar libros")
    print(f"3- Eliminar libro")
    print(f"4- Salir")

    option_user = input(f"Ingrese la opción a la que desea ir: ")
    match option_user:
        case "1":
            add_books()

        case "2":
            show_books()

        case "3":
            remove_books()

        case "4":
            print("Saliendo del programa...")
            break

        case _:
            print(f"Valor inválido, intente de nuevo.")