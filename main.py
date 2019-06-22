import user
import book
import mode

while (1):
    Usr = user.User()
    Book = book.Book()
    UserMode = mode.UserMode()

    print('\n\n정하대학교 도서관에 오신 걸 환영합니다.')

    print('-----------------사용 안내---------------------')
    print('1: 대출하기, 2: 반납하기, 3: 대출정보 확인하기\n\n')

    menu = int(input("사용하실 용도의 번호를 선택해주세요: "))

    if menu == 1:
        # todo :
        print('대출하기를 선택하였습니다.\n')
        myid = []
        u_data = ''
        codes = []
        flag = 0
        i = -1
        while (True):
            if flag == 0:
                id, u_data = UserMode.login()
                id, code = UserMode.loanBook(id, u_data)
                myid.append(id)
                i += 1
                codes.append(code)

            elif flag:
                id, code = UserMode.loanBook(id, u_data)
                myid.append(id)
                i += 1
                codes.append(code)

            select = input("추가로 대출하시겠습니까? (Y/N) ")

            if select in ['N', 'n']:
                break
            else:
                flag = 1

        for idx in range(i+1):
            print(codes[idx], myid[0])
            UserMode.print_receipt(menu, codes[idx], myid[0])


    elif menu == 2:
        print("반납하기를 선택하였습니다.\n")
        i = -1
        myid = []
        codes = []
        while (True):
            id, code = UserMode.returnBook()
            i += 1
            myid.append(id)
            codes.append(code)

            select = input("추가로 반납하시겠습니까? (Y/N) ")

            if select in ['N', 'n']:
                break

        for idx in range(i+1):
            print(codes[idx], myid[0])
            UserMode.print_receipt(menu, codes[idx], myid[0])

    elif menu == 3:
        # TODO :대출 정보 확인하기
        print("대출 정보 확인하기를 선택하였습니다.\n")
        UserMode.printLoanInfo()


    elif menu == -1:
        while (True):
            Admin = mode.AdminMode()
            print('[시크릿 모드]')
            print('** 관리자 모드 입니다. **')

            print('\n\n-----------------사용 안내---------------------')
            print(
                '1: 학생 정보 추가하기, 2: 학생 정보 조회하기, 3: 학생 정보 모두 보기, 4: 도서 정보 추가하기, 5: 도서 정보 조회하기, 6: 도서 정보 모두 보기 q: 나가기 \n\n')

            adminMenu = input("\n사용하실 용도의 번호를 선택해주세요: ")

            if adminMenu == '1':
                print('학생 정보 추가하기를 선택하였습니다.')

                id = input("학번을 입력해주세요: ")

                Admin.registerUsr(id)

            elif adminMenu == '2':
                print("학생 정보 조회하기를 선택하였습니다.")
                id = input("학번을 입력해주세요: ")
                Admin.showUsr(id)

            elif adminMenu == '3':
                Admin.showAllUsr()

            elif adminMenu == '4':
                print('도서 정보 추가하기를 선택하였습니다.')
                Bname, publisher, writer, code = Admin.askBookInfo()
                Admin.registerBook(Bname, publisher, writer, code)

            elif adminMenu == '5':
                code = input('도서 코드를 입력해주세요: ')
                Admin.showBook(code)

            elif adminMenu == '6':
                Admin.showAllBook()

            elif adminMenu == 'q':
                print('관리자 모드를 나갑니다. ')
                break

            else:
                print("번호를 잘 못 입력하였습니다.")
