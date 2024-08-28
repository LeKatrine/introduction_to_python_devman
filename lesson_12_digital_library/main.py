def get_shelfs_book(num_of_books):
    for num in range(num_of_books):
        shelf = input("На какую книжную полку добавить книгу? ")
        book_name = input("Название книги: ").strip()
        author = input("Автор книги: ").strip()      
        book_format = {"name" : book_name, "authors" : author}
        shelf_format = "Shelf_{} : {}\n".format(shelf, book_format)
        with open("Library.txt", "a") as lib:
            lib.write(f"{shelf_format}")
    return "Книги добавлены"


def read_file_library():
    with open("Library.txt", "rt") as lib:
        for n, line in enumerate(lib, start=1):
            print(f"{n}:", line.strip())
            
# def read_file_library():
#     with open("Library.txt", "r") as lib:
#         for line in lib:
#             print(line.strip())


def main():
    num_of_books = int(input("Сколько книг вам нужно добавить? "))
    print(get_shelfs_book(num_of_books))
    read_file_library()
    
if __name__ == "__main__":
	main()