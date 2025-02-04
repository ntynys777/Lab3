class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        """Gets a string from user input."""
        self.input_string = input("Enter a string: ")

    def printString(self):
        """Prints the stored string in uppercase."""
        print(self.input_string.upper())

string_manipulator = StringManipulator()
string_manipulator.getString()  
string_manipulator.printString()
