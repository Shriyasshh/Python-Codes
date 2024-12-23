class Library:
    shelf=[]
    def __init__(self,book):
        self.book=book

    def Addbook(self):
        Library.shelf.append(self.book)
        # print(f"Book '{self.book}'added to library succssfully ")

    def __len__(self):
        return len(Library.shelf)
    
a=Library("python")
a.Addbook()
b=Library("java")
b.Addbook()

print(len(b))
print(Library.shelf)  
c=Library("C++")
c.Addbook()
print(Library.shelf)


#or

class Library1:
    def __init__(self):
        self.NoBook=0
        self.Books=[]

    def Add(self,book):
        self.Books.append(book)
        self.NoBook=len(self.Books)
        
    def show(self):
        print(f"Library has {self.NoBook} books")
        print(self.Books)

    
a=Library1()
a.Add("python")
a.Add("python1")
a.Add("python2")
a.Add("python3")
a.show()

b =Library1()
b.Add("Java")
b.show()
C=Library1()
C.show()