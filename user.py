class User:
    def __init__(self):
        self.usrList = {'20171677': ['이정하', '학사', '소프트웨어학부', '0000']}

    def setName(self, id, name):
        self.usrList[id][0] = name

    def getName(self, id):
        if id == self.getID(id):
            return self.usrList[id][0]

    def setID(self, id):
        self.usrList[id] = []

    def getID(self, id):
        if id in self.usrList.keys():
            return id
        else:
            return False

    def addUser(self, id, name, degree, dept):
        self.usrList[id] = [name, degree, dept, '0000']
        return self.usrList
        pass

    def setDegree(self, id, degree):
        self.usrList[id][2] = degree

    def getDegree(self, id, degree):
        if degree in self.usrList[id]:
            return degree

    def setDept(self, id, dept):
        self.usrList[id][1] = dept

    def getDept(self, id, dept):
        if dept in self.usrList[id]:
            return dept
