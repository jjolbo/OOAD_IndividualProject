import pickle
from datetime import date


class DataManager:
    loanList = {}

    def storeRecord(self, id, code, date):
        with open('./loan.data', 'wb') as f:
            self.loanList[code] = [id, date]
            pickle.dump(self.loanList, f)
            print("대출 기록 완료")

    def loadRecord(self, code):
        with open('./loan.data', 'rb') as f:
            data = pickle.load(f)

            if code in data.keys():
                return data[code]

    def loadRecord1(self, id):
        codes = []
        flag = 0
        with open('./loan.data', 'rb') as f:
            data = pickle.load(f)
            for code in data.keys():
                if data[code][0] == id:
                    codes.append(code)
                    flag = 1

            if flag == 0:
                print('대출 정보가 없습니다.')

            return codes

    def delRecord(self, code):
        with open('./loan.data', 'rb') as f:
            data = pickle.load(f)
            if code in data.keys():
                del data[code]

        with open('./loan.data', 'wb') as f:
            pickle.dump(data, f)

    def storeUser(self, usrList):
        with open('./user.data', 'wb') as f:
            # pickle.dump({'20171677': ['이정하', '학사', '소프트웨어학부', '0000']}, f)
            pickle.dump(usrList, f)

        print("유저 정보 기록 완료")

    def loadUser(self, id):

        with open('./user.data', 'rb') as f:
            data = pickle.load(f)
            if id in data.keys():
                u_id = id
                u_data = data[id]
                # print(u_id, u_data)
                return u_id, u_data
            else:
                u_id = None
                u_data = None
                # print(u_id, u_data)
                return u_id, u_data

    def storeBook(self, bookList):
        with open('./book.data', 'wb') as f:
            pickle.dump(bookList, f)

        print("도서 정보 기록 완료")

    def loadBook(self, code):
        with open('./book.data', 'rb') as f:
            data = pickle.load(f)
            if code in data.keys():
                b_code = code
                b_data = data[code]
                return b_code, b_data
            else:
                b_code = None
                b_data = None
                return b_code, b_data

    def loadAllUser(self):
        with open('./user.data', 'rb') as f:
            data = pickle.load(f)

        return data

    def loadAllBook(self):
        with open('./book.data', 'rb') as f:
            data = pickle.load(f)

        return data


# if __name__ == '__main__':
#     from datetime import date
#
#     usrList = {'20171677': ['이정하', '학사', '소프트웨어학부', '0000']}
#     dm = DataManager()
#     bookList = {'20190615': ['객체지향분석및설계', '한빛미디어', '최은미']}
#     dm.storeUser(usrList)
#     dm.storeBook(bookList)
#     today = date.today()
#     return_day = date(today.year, today.month, today.day + 7)
#
#     dm.storeRecord('20171677','20190615',return_day)
#     # dm.storeUser()
