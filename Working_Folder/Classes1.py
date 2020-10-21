# Class that declares library instance details
class Library():
    # Variables to be identical when instanced
    listOfClients = []
    listOfEmployees = []
    listOfBooks = []
	
    # Variables to be defined when instanced
    def __init__(self, libraryOwner=None, libraryCoowner=None, libraryName=None):
        # If the libraryOwner isn't populated, then use the default value
        if libraryOwner is None:
            self.libraryOwner = "Dylan Scott"
        else:
            self.libraryOwner = libraryOwner
        
        # If the libraryCoowner isn't populated, then use the default value
        if libraryCoowner is None:
            self.libraryCoowner = ""
        else:
            self.libraryCoowner = libraryCoowner
        
        # If the libraryName isn't populated, then use the default value
        if libraryName is None:
            self.libraryName = "Durham Books!"
        else:
            self.libraryName = libraryName
	
    # __str__ function: returns the below string when the object itself is passed into the 'print' function
    def __str__(self):
        return "This is the 'BookPublisher' class"
    
    # __repr__ function: returns the below string when the object itself is passed is called by itself
    def __repr__(self):
        return "BookPublisher()"
    
    # Prints the owner(s) of the Library
    def printTheOwners(self):
        if self.libraryCoowner == "":
            print("The owner of '" + self.libraryName + "' is " + self.libraryOwner + ".")
        else:
            print("The owners of '" + self.libraryName + "' are " + self.libraryOwner + " and " + self.libraryCoowner + ".")
    
    # Print out a list of all clients of the library
    def generateListOfClient(self):
        print("List of all clients:")
        clientList = list(dict.fromkeys(self.listOfClients))
        for client in clientList:
            print("  " + client.fullName)
    
    # Print out a list of all employees of the library
    def generateListOfEmployees(self):
        print("List of all employees:")
        employeeList = list(dict.fromkeys(self.listOfEmployees))
        for employee in employeeList:
            print("  " + employee.fullName)
    
    # Print out a list of all books in the library
    def generateListOfBooks(self):
        print("List of all books:")
        bookList = list(dict.fromkeys(self.listOfBooks))
        for book in bookList:
            print("  " + book.title)

# Create Library object
Library = Library()
print("The library object is called 'Library'.")

# Class that declares client instance details
class AddClient():
    # Variables to be identical when instanced
    previouslyCheckedOutBooks = []
    activelyCheckedOutBooksList = []

    # Variables to be defined when instanced
    def __init__(self, firstName, surname, age, gender, address):
        self.__firstName = firstName
        self.surname = surname
        self.age = age
        self.gender = gender
        self.address = address
        self.fullName = self.__firstName + " " + self.surname
        Library.listOfClients.append(self);

    # __str__ function: returns the below string when the object itself is passed into the 'print' function
    def __str__(self):
        return "This is the 'AddClient' class"

    # __repr__ function: returns the below string when the object itself is passed is called by itself
    def __repr__(self):
        return "AddClient()"
    
    # Prints the clients name
    def printName(self):
        print("The client is called " + self.fullName + ".")
    
    # Prints the number of books checked out by the client
    def printPreviouslyCheckedOutVolume(self):
        if len(self.previouslyCheckedOutBooks) == 1:
            print("The client has checked out " + str(len(self.previouslyCheckedOutBooks)) + " book in the past.")
        else:
            print("The client has checked out " + str(len(self.previouslyCheckedOutBooks)) + " books in the past.")
    
    # Prints the names of the books currently checked out by the client
    def printActivelyCheckedOut(self):
        print(self.fullName + "currently has these books checked out:")
        for ind, book in enumerate(self.activelyCheckedOutBooksList):
            print("  Book " + str(ind + 1) + ": " + book.title)

    # Prints the clients age
    def printAge(self):
        if self.gender == "male":
            print("He is " + str(self.age) + " years old.")
        elif self.gender == "female":
            print("She is " + str(self.age) + " years old.")
        else:
            print("They are " + str(self.age) + " years old.")
    
    # Add book to clients checked out list
    def checkOutBook(self, newBook):
        self.activelyCheckedOutBooksList.append(newBook)
        print("'" + newBook.title + "' has been added to " + self.fullName + "'s checked out list.")

    # Remove book from clients checked out list and adds to their historic list
    def checkBookBackIn(self, newBook):
        self.activelyCheckedOutBooksList.remove(newBook)
        print("'" + newBook.title + "' has been removed from " + self.fullName + "'s checked out list.")
        self.previouslyCheckedOutBooks.append(newBook)
        print("'" + newBook.title + "' has been added to " + self.fullName + "'s historic checked out list.")

# Class that declares employee instance details
class AddEmployee(AddClient):
    # Variables to be identical when instanced
    previouslyCheckedOutBooks = []
    activelyCheckedOutBooksList = []

    # Variables to be defined when instanced
    def __init__(self, firstName, surname, age, gender, address, employeeLevel):
        super().__init__(firstName, surname, age, gender, address)
        self.employeeLevel = employeeLevel
        Library.listOfEmployees.append(self);

    # __str__ function: returns the below string when the object itself is passed into the 'print' function
    def __str__(self):
        return "This is the 'AddEmployee' class"
    
    # __repr__ function: returns the below string when the object itself is passed is called by itself
    def __repr__(self):
        return "AddEmployee()"
    
    # Prints the employees name
    def printName(self):
        print("The employee is called " + self.fullName + ".")
    
    # Promotes the employees to the next level
    def promoteEmployee(self):
        self.employeeLevel = self.employeeLevel + 1
        print("The employee has been promoted from level " + str(self.employeeLevel - 1) + " to level " + str(self.employeeLevel) + ".")

# Class that declares books
class BookSales():
    # Variables to be identical when instanced
    cutOfProfit = 0.6

    # Variables to be defined when instanced
    def __init__(self, sales, price):
        self.sales = sales
        self.price = price
        self.gross = self.price * self.cutOfProfit
        self.profit = self.gross * self.sales
    
    def __str__(self):
        return "This is the 'BookSales' class"
    
    def __repr__(self):
        return "BookSales()"

# Class that declares book instance details
class NewBook():
    # Variables to be defined when instanced
    def __init__(self, title, pageNum, genre, sales, price):
        self.title = title
        self.pageNum = pageNum
        self.genre = genre
        self.__salesDetails = BookSales(sales, price)
        self.__profit = self.__salesDetails.profit
        Library.listOfBooks.append(self);


    # __str__ function: returns the below string when the object itself is passed into the 'print' function
    def __str__(self):
        return "This is the 'NewBook' class"

    # __repr__ function: returns the below string when the object itself is passed is called by itself
    def __repr__(self):
        return "NewBook()"

    # Print the title and genre of book
    def printBookDetails(self):
        print("The title of this book is '" + self.title, "', and is of the genre '" + self.genre + "'.")

    # Prints the length of the book
    def printBookLength(self):
        if self.pageNum < 100:
            print("This is a short book, only " + str(self.pageNum) + " pages.")
        elif self.pageNum <= 300:
            print("This is a moderately long book, " + str(self.pageNum) + " pages.")
        else:
            print("This is a LONG book, a whooping " + str(self.pageNum) + " pages!")

# Create some clients
alex = AddClient("Alex", "Billson", 23, "male", "1 First Street")
bill = AddClient("Bill", "Charles", 53, "male", "2 Second Street")
chris = AddClient("Chris", "Downs", 35, "male", "3 Third Street")
dylan = AddClient("Dylan", "Everton", 19, "male", "4 Fourth Street")

# Create some employees
eve = AddEmployee("Eve", "Fry", 41, "female", "5 Fifth Street", 10)
freya = AddEmployee("Freya", "Greggs", 20, "female", "6 Sixth Street", 9)
georgia = AddEmployee("Georgia", "Holmes", 30, "female", "7 Seventh Street", 9)
hanna = AddEmployee("Hanna", "Ivory", 34, "female", "8 Eighth Street", 8)

# Create some books
hobbit = NewBook("The Hobbit", 200, "Fantasy", 1000000, 12)
fellowship = NewBook("The Fellowship", 534, "Fantasy", 836200, 12)
twoTowers = NewBook("The Two Towers", 496, "Fantasy", 648300, 12)
returnKing = NewBook("The Return", 817, "Fantasy", 884600, 12)

# Clients check out some books
alex.checkOutBook(hobbit)
bill.checkOutBook(fellowship)
chris.checkOutBook(twoTowers)
dylan.checkOutBook(returnKing)

# Employees check out some books
eve.checkOutBook(hobbit)
freya.checkOutBook(hobbit)
georgia.checkOutBook(hobbit)
hanna.checkOutBook(hobbit)
eve.checkOutBook(fellowship)
freya.checkOutBook(fellowship)
georgia.checkOutBook(fellowship)
hanna.checkOutBook(fellowship)

# Employees check in some books
eve.checkBookBackIn(hobbit)
freya.checkBookBackIn(hobbit)
georgia.checkBookBackIn(hobbit)
hanna.checkBookBackIn(hobbit)

# List all clients, employees, and books in Library object
Library.generateListOfClient()
Library.generateListOfEmployees()
Library.generateListOfBooks()

# Call one method from each class
Library.printTheOwners()
alex.printPreviouslyCheckedOutVolume()
eve.promoteEmployee()
hobbit.printBookLength()