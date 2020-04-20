
#abstract class
class Taggable(object):
    def tag(self):
        pass
class Book(Taggable):
    code_of_book = 1
    def __init__(self, author, title):
        try:
            if len(str(title)) == 0 or len(str(author)) == 0:
                raise ValueError
            else:
                self.__title = title
                self.__author = author
                self.__code = Book.code_of_book
                Book.code_of_book += 1
        except ValueError:
                if len(str(title)) ==0:
                    self.__title = "Unknown"
                    self.__author = author
                    self.__code = Book.code_of_book
                if len(str(author)) ==0:
                    self.__title = title
                    self.__author = "Unknown"
                    self.__code = Book.code_of_book
                if len(str(author)) ==0 and len(str(title)) ==0:
                    self.__title = "Unknown"
                    self.__author = "Unknown"
                    self.__code = Book.code_of_book
    def __str__(self):
        return "[{0}] {1} '{2}'".format(self.code, self.author, self.title)
    def tag(self):
        return [word for word in str(self.__title).split() if str(word)[0].isupper()]
    @property
    def author(self):
        return self.__author
    @property
    def title(self):
        return self.__title
    @property
    def code(self):
        return self.__code
class Library(object):
    def __init__(self, adress, number):
        self.__books = list()
        self.__adress = adress
        self._number = number
    def __iadd__(self, book):
        self.__books.append(book)
        return self
    def __iter__(self):
        return iter(self.__books)

if __name__ =="__main__":
    lib = Library(1, "51 Some str., NY’")
    lib += Book("Leo Tolstoi", "War and Peace")
    lib += Book("Charles Dickens", "David Copperfield")
    lib += Book("", "")
    for book in lib:
#вывод в виде: [1] L.Tolstoi ‘War and Peace’
        print(book)
# вывод в виде: [‘War’, ‘Peace’]
        print(book.tag())