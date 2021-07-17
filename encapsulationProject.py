# a protector class
class Protector:
    # initializes the protector class
    def __init__(self):
        self.proctedVal = 0
        pass

    # gets the protected variable from the class

    def getProtectedVal(self):
        return 'Procted variable: {}'.format(self.proctedVal)

    # sets the protected variable from the class

    def setProtectedVal(self, proctedVal):
        self.proctedVal = proctedVal

    # increments the protected variable from the class

    def incrementProtectedVal(self):
        self.proctedVal += 1


# Entry point for the app
if __name__ == '__main__':
    # instance of the class
    protector = Protector()
    # gets the protected variable
    print(protector.getProtectedVal())

    # sets the protected variable
    protector.setProtectedVal(1)
    # gets the protected variable
    print(protector.getProtectedVal())

    # increments the protected variable
    protector.incrementProtectedVal()
    # gets the protected variable
    print(protector.getProtectedVal())
