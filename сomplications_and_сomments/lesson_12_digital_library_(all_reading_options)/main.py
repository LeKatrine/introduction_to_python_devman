def get_shelfs_book(number):
    for index in range(number):
        shelf = input("На какую книжную полку добавить книгу? ")
        book_name = input("Название книги: ").strip()
        author = input("Автор книги: ").strip()      
        book_format = {"name" : book_name, "authors" : author}
        shelf_format = "Shelf_{} : {}\n".format(shelf, book_format)
        with open("Library.txt", "a") as lib:
            lib.write(f"{shelf_format}")
    return print("Книги добавлены")
        
number_of_books = int(input("Сколько книг вам нужно добавить? "))


def read_file_library():
    with open("Library.txt", "r") as lib:
        for string in lib:
            print(string.strip())
            
        print("Другой способ")
        lib.seek(0)
        line = lib.readline().strip()
        while line:
            print(line)
            line = lib.readline().strip()

        print("Другой способ")
        lib.seek(0)
        for х in lib:
            х = lib.readline().strip()
            print(х)

def main():
    get_shelfs_book(number_of_books)
    read_file_library()
    
if __name__ == '__main__':
	main()