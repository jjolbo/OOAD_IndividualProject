import user
import book
import dataManager
from datetime import date

class Mode:
    def select_mode(self):
        pass


class AdminMode(Mode):
    book = book.Book()
    usr = user.User()
    dataManager = dataManager.DataManager()

    def askUsrInfo(self):
        name = input("이름을 입력해주세요: ")
        dept = input("학과를 입력해주세요: ")
        degree = input("학위를 입력해주세요: ")

        return name, dept, degree

    def askBookInfo(self):
        Bname = input("도서명을 입력해주세요: ")
        publisher = input('출판사명을 입력해주세요: ')
        writer = input('저자명을 입력해주세요: ')
        code = input('도서 코드를 입력해주세요: ')

        return Bname, publisher, writer, code


    def registerUsr(self, id):
        u_id, u_data = self.dataManager.loadUser(id)

        if u_id is None:
            name, degree, dept = self.askUsrInfo()
            data = self.usr.addUser(id, name, degree, dept)
            self.dataManager.storeUser(data)
        else:
            print(u_id, ' 사용자는 이미 등록되어있습니다.')

    def showUsr(self, id):
        u_id, u_data = self.dataManager.loadUser(id)

        if u_id is None:
            print(id, '학번은 없습니다.\n\n')
        else:
            print('[학생정보]')
            print('학번: ', u_id)
            print('이름: ',u_data[0])
            print('학과: ', u_data[1])
            print('학위: ', u_data[2])
            print('임시 비밀번호: ', u_data[3])

    def showAllUsr(self):
        dic = self.dataManager.loadAllUser()

        print('[학생정보]')
        cnt = 0
        for data in dic:
            cnt += 1
            print(cnt,'.')
            print('학번: ', data)
            print('이름: ', dic[data][0])
            print('학과: ', dic[data][1])
            print('학위: ', dic[data][2])
            print('임시 비밀번호: ', dic[data][3])

    def registerBook(self, name, publisher, writer, code):
        b_code, b_data = self.dataManager.loadBook(code)

        if b_code is None:
            data = self.book.addBook(code, name, publisher, writer)
            self.dataManager.storeBook(data)
        else:
            print(code, ' 도서는 이미 등록되어있습니다.')

    def showBook(self, code):
        b_code, b_data = self.dataManager.loadBook(code)

        if b_code is None:
            print(code, '도서는 없습니다.\n\n')
        else:
            print('[도서정보]')
            print('도서번호: ', b_code)
            print('도서명: ', b_data[0])
            print('출판사: ', b_data[1])
            print('저자: ', b_data[2])

    def showAllBook(self):
        dic = self.dataManager.loadAllBook()

        print('[도서정보]')
        cnt = 0
        for data in dic:
            cnt += 1
            print(cnt, '.')
            print('도서번호: ', data)
            print('도서명: ', dic[data][0])
            print('출판사: ', dic[data][1])
            print('저자: ', dic[data][2])


class UserMode(Mode):
    Book = book.Book()
    Usr = user.User()
    dataManager = dataManager.DataManager()

    def login(self):
        id = input('학번을 입력해주세요: ')
        u_id, u_data = self.dataManager.loadUser(id)

        if u_id is None:
            print('위 아이디는 존재하지 않습니다.')

        else:
            while (True):
                pw = input('비밀번호를 입력해주세요: ')
                if pw == u_data[3]:
                    break
                else:
                    print('비밀번호가 일치하지 않습니다.')

        return u_id, u_data

    def scanBook(self):
        code = input('대출할 도서를 스캔해주세요: ')
        b_code, b_data = self.dataManager.loadBook(code)

        if b_code is None:
            print('해당 도서를 찾을 수 없습니다.')

        return b_code, b_data


    def loanBook(self, id, u_data):
        code, b_data = self.scanBook()

        if code != None:
            book_name = b_data[0]
            book_writer = b_data[2]
            book_publisher = b_data[1]

            # todo : store the info between user and book.
            today = date.today()
            return_day = date(today.year, today.month, today.day + 7)

            self.dataManager.storeRecord(id, code, return_day)

            print(u_data[0], '님의 대출 기록은 ... ')
            print('책 이름: ', book_name, '저자명: ', book_writer, '출판사명: ', book_publisher)

        return id, code

    def returnBook(self):
        code = input('반납할 도서를 스캔해주세요: ')
        id = ''
        b_code, b_data = self.dataManager.loadBook(code)

        if b_code is None:
            print('해당 도서를 찾을 수 없습니다.')

        else:
            # todo : store the info between user and book.
            id = self.dataManager.loadRecord(code)[0]
            book_name = b_data[0]
            book_writer = b_data[2]
            book_publisher = b_data[1]
            print(id, '님의 남은 책은 ... ')
            print('책 이름: ', book_name, '저자명: ', book_writer, '출판사명: ', book_publisher)

            self.dataManager.delRecord(code)

        return id, code

    def printLoanInfo(self):
        # todo
        id = input('학번을 입력해주세요: ')
        u_id, u_data = self.dataManager.loadUser(id)

        if u_id is None:
            print('위 아이디는 존재하지 않습니다.')

        else:
            codes = self.dataManager.loadRecord1(u_id)
            for i in codes:
                time = self.dataManager.loadRecord(i)[1]
                b_code, b_data = self.dataManager.loadBook(i)

                print('[대출정보]')
                print('도서명: ', b_data[0], end='\t\t')
                print('출판사: ', b_data[1], end ='\t\t')
                print('반납일:' ,time)



    def print_receipt(self, mode, code, id):
        today = date.today()
        return_day = date(today.year, today.month, today.day + 7)

        if mode == 1:
            print('\n\n----대출 확인증 ----')
        else:
            print('\n\n----반납 확인증 ----')

        u_id, u_data = self.dataManager.loadUser(id)
        print('사용자명: ', u_data[0])
        print('도서번호: ', code)
        b_code, b_data = self.dataManager.loadBook(code)
        print('도서명 : ', b_data[0])
        print()

        if mode == 1:
            print('대출일: ', today)
            print('반납예정일: ', return_day)
        else:
            print('반납일: ', today)
