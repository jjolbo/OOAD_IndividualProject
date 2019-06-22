class Book:
    def __init__(self):
        self.bookList = {'20190615': ['객체지향분석및설계', '한빛미디어', '최은미']}

    def addBook(self, code, name, publisher, writer):
        self.bookList[code] = [name, publisher, writer]

        return self.bookList

    def setName(self, code, name):
        self.bookList[code][0] = name

    def getName(self, code):
        if code == self.getCode(code):
            return self.bookList[code][0]

    def setPublisher(self, code, publisher):
        self.bookList[code][1] = publisher

    def getPublisher(self, code):
        if code == self.getCode(code):
            return self.bookList[code][1]

    def setWriter(self, code, writer):
        self.bookList[code][2] = writer

    def getWriter(self, code):
        if code == self.getCode(code):
            return self.bookList[code][2]

    def setCode(self, code):
        self.bookList[code] = []

    def getCode(self, code):
        if code in self.bookList.keys():
            return code
        else:
            return False

