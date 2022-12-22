class Publisher:
    def __init__(self,publisher_name):
        self.publisher_name = publisher_name

class Book(Publisher):
    def __init__(self,publisher_name,title,author):
        Publisher.__init__(self,publisher_name)
        self.title = title
        self.author = author

class Python(Book):
    def __init__(self,publisher_name,title,author,price,no_of_pages):
        Book.__init__(self,publisher_name,title,author)
        self.price = price
        self.no_of_pages = no_of_pages


book1 = Python("DC","superman","stan lee",500,1000)

print(vars(book1))