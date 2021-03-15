######   BOOKS AVAILABLE IN STORE   ######
course_books=[
        [1,'  PAK-STUDY','           MUHAMMAD SAMEER ',70],
        [2,'  ISLAMIC-STUDY','       NAHYAL AMJAD    ',70],
        [3,'  COMMAND-ENGLISH','     NOUSHEEN FARRUKH',70],
        [4,'  COMPUTER-SCIENCE','    MUHAMMAD HASSAN ',70],
        [5,'  CALCULUS','            MUHAMMAD KHALID ',70],
        [6,'  ITC','                 MUZAFFER IQBAL  ',70],
        [7,'  ECA','                 AZHAR YASIN     ',70],
        [8,'  PHYSICS','             FAIZAN SHBBIR   ',70],
        [9,'  PYTHON FOR BEGINNER',' YASIR JAMAL     ',70],
        [10,' STATISTICS','          MUHAMMAD MASOUD ',70]
        ];
        
#for books in(course_books):
    #print(books) 
books_comic=[
        [1,"  DOCTOR-STRANGE","     JON HOPKINS   ",70],
	[2,"  SPIDERMAN","          GEORGE ORWELL ",70],
	[3,"  GHOST-IN-SHELL","     KEVIN ROY     ",70],
	[4,"  PUNISHER","           SAM FISHER    ",70],
	[5,"  WOLVERINE","          PETERSON RAND ",70],
	[6,"  THE-DARK-KNIGHT","    KEVIN HERTZ   ",70],
	[7,"  BLACK-PANTHER","      PETERSON LOGAN",70],
	[8,"  INCREDIBLE-HULK","    HARRY STYLES  ",70],
	[9,"  FANTASTIC-FOUR","     JOSEPH HELLER ",70],
	[10," GHOST-RIDER","        ROSE TAYLOR   ",70]
        ];
#print(books_comics[9][1])
books_novel=[
        [1,"THE-OLD-MAN-&-THE-SEA"," JAMES JOYCE    ",70],
	[2,"GOODBYE-MR.CHIPS","      JAMES HILTON   ",70],		 						
	[3,"ULYSSES-HUMAN-FATE","    JAMES JOYCE    ",70],											
	[4,"BATTLE-CRY-OF-FREEDOM"," ALDOUS HUXLEY  ",70],									
	[5,"DARKNESS-AT-NOON","      ARTHUR KOESTLER",70],
	[6,"THE-DEVIL-IN-THE-CITY"," MALCOLM LOWRY  ",70],										
	[7,"BATTLEFIELD-EARTH","     AYN RAND       ",70],									
	[8,"MISSION-EARTH-2050","    RON HUBBARD    ",70],										
	[9,"THE-ABRAHAM-LINCOLN","   HARPER LEE     ",70],	
	[10,"BRAVE-NEW-WORLD-1778"," SCOTT JAMES    ",70]
        ];
#print(books_comics)
	
books_history=[
        [1," HIROSHIMA-REDEMPTION","    JOHN HERSEY    ",70],
	[2," THE-HISTORIES-OF-WAR","    HERODOTUS      ",70],
	[3," THE-RISE-AND-FALL","       DAVID JOY      ",70],
	[4," BATTLE-OF-FREEDOM","       JAMES M.CARVER ",70],
	[5," GUNS,GERMS-AND-STEEL","    JARED DIAMOND  ",70],						
	[6," TEAM-OF-RIVALS-ALCHEMY","  DAVID ROY      ",70],										
	[7," THE-GUNS-OF-AUGUST","      BARBARA TUCHMAN",70],							
	[8," THE-DIARY-OF-YOUNG-GIRL"," DAVID ROY      ",70],							
	[9," A-DISTANT-MIRROR","        BARBARA TUCHMAN",70],
	[10,"A-SHORT-HISTORY-OF-WWII"," DEE BROWN      ",70]
        ];
######   BOOKS AVAILABLE IN STORE   ######[
available_books=[
        ["PAK-STUDY","MUHAMMAD SAMEER",70],
        ["ISLAMIC-STUDY","NAHYAL AMJAD",70],
        ["ENGLISH","NOUSHEEN FARRUKH",70],
        ["COMPUTER","MUHAMMAD HASSAN",70],
        ["CALCULUS","MUHAMMAD KHALID",70],
        ["ITC","MUZAFFER IQBAL",70],
        ["ECA","AZHAR YASIN",70],
        ["PHYSICS","FAIZAN SHBBIR",70],
        ["PYTHON","YASIR JAMAL",70],
        ["STATISTICS","MUHAMMAD MASOUD",70],
        ["DOCTOR-STRANGE","JON HOPKINS",70],
	["SPIDERMAN","GEORGE ORWELL",70],
	["GHOST-IN-SHELL","KEVIN ROY",70],
	["PUNISHER","SAM FISHER",70],
	["WOLVERINE","PETERSON RAND",70],
	["DARK-KNIGHT","KEVIN HERTZ",70],
	["BLACK-PANTHER","PETERSON LOGAN",70],
	["INCREDIBLE-HULK","HARRY STYLES",70],
	["FANTASTIC-FOUR"," JOSEPH HELLER",70],
	["GHOST-RIDER","ROSE TAYLOR",70],
        ["THE-OLD-MAN-&-THE-SEA","JAMES JOYCE",70],
	["GOODBYE-MR.CHIPS","JAMES HILTON",70],		 						
	["ULYSSES-HUMAN-FATE","JAMES JOYCE",70],											
	["BATTLE-CRY-OF-FREEDOM","ALDOUS HUXLEY",70],									
	["DARKNESS-AT-NOON","ARTHUR KOESTLER",70],
	["THE-DEVIL-IN-THE-CITY","MALCOLM LOWRY",70],										
	["BATTLEFIELD-EARTH","AYN RAND",70],									
	["MISSION-EARTH-2050","RON HUBBARD",70],										
	["THE-ABRAHAM-LINCOLN","HARPER LEE",70],	
	["BRAVE-NEW-WORLD-1778","SCOTT JAMES",70],
        ["HIROSHIMA-REDEMPTION","JOHN HERSEY",70],
	["WAR-HISTORIES","HERODOTUS",70],
	["RISE-FALL","DAVID JOY ",70],
	["BATTLE-OF-FREEDOM","JAMES M.CARVER",70],
	["GUNS-AND-STEEL","JARED DIAMOND",70],						
	["TEAM-ALCHEMY","DAVID ROY",70],										
	["GUNS-OF-AUGUST","BARBARA TUCHMAN",70],							
	["YOUNG-GIRL","DAVID ROY",70],							
	["DISTANT-MIRROR","BARBARA TUCHMAN",70],
	["HISTORY-WWII","DEE BROWN",70]
        ];
#print(len(available_books))

#to store all the avilable books in computer memory
books_file=open("E:/available_books.txt",'w')
for ele in available_books:
    books_file.write(str(ele)+'\n')
books_file.close()
         #def cls
         #def course_book():
         #def comic_book():
         #def history_books():
         #def novel_books():
         #def books_collection():
         #def search_books():
         #def reg_new_book(): 
         ####################### def main_menu(): main function  
         
#####search element in 2D list:-
#z=input("Search auther name: ")
#if z in available_books:
#for a in range (len(available_books)):
#   for b in range(3):
#      if available_books[a][b]==z:
#         print("Auther found \n ")
#         print("Book name:           Auther name:            Price: ")
#         for k in available_books[a]:
#             print(k,end="               ")
#      print("\n")
#         break
#print("Auther not found ")
       


import os
def cls():          #clear screan
    os.system('cls')
def main_menu():
    cls()
    print("                         BOOKSTORE                   ")
    print("   1.Display the books collection: ")
    print("   2.Search required book: ")
    print("   3.Enter your credit card number to complete the transection: ")
    print("   4.Regester new books: \n \n ")

 
    print("      Slect the options from the main menu: ")
    print("      Press 0 to exit from the main menu:")
    try:
        a=int(input("Select an option: "))
        if(a==1):
            books_collection()
        elif(a==2):
            search_books()
        elif(a==3):
            bill_of_b()
        elif(a==4):
            reg_new_book()
        elif(a==0):
            exit()
        else:
            print("Select option from given menu..... ")
            main_menu()
        #order_book()
    except:
        print("Went somthing wrong....")
        input("press enter to return to main menu")
        main_menu()
#books collection
def books_collection():
    cls()
    print("""     1.COURSE BOOKS \n     2.COMIC BOOKS \n     3.NOVEL BOOKS \n     4.HISTORY BOOKS""")
    print(" \n     press 0 to return to main menu: ")
    try:
        b=int(input("Select option: ")) 
        if(b==1):
           course_book()
        elif(b==2):
            comic_book()
        elif(b==3):
            novel_books()
        elif(b==4):
            history_books()
        elif(b==0):
            main_menu() 
        else:
            print("select option from the main menu.....")
            books_collection()
        order_book()
    except:
        print("Went somthing wrong.....")
        input("Press enter to return to collection menu")
        books_collection()
#course books
def course_book():
    print("                   COURSE BOOKS")
    print("No.      Auther name:              Book name:            price:\n")
    # multiple temporary values                            #version 2. using indexes 
    for no,auther,books,price in(course_books):            #for i in course_books:
        print(no,"    ",auther,"    ",books,"    ",price)  #    print(i[0],i[1],i[2],i[3])
    try:
        b1=int(input("Enter book number(TO PURCHASE BOOK): "))
        if(b1>10 or b1<=0):
            print("Select option from given.....")
            course_book()
        else:
            i=b1-1
            while(b1>i):
                for c_books in(course_books[i]):
                    a=open("E:/purchse_book.txt",'a')
                    a.write(str(c_books)+"\n \n")
                    a.close() 
                    print(c_books,end="          ")
                i+=1
                break
    except ValueError:
        print("went somthing wrong......")
        input("press enter to return to books collection")
        books_collection()
    
#comic books()
def comic_book():
    print("                 COMIC BOOKS")
    print("No.     Auther name:             Book name:          Price:\n")
    for no,auther,book,price in(books_comic):
        print(no,"   ",auther,"    ",book,"    ",price)
    try:    
        b2=int(input("Enter book number(TO PURCHASE BOOK): "))
        if(b2<=0 or b2>10):
            print("Select option from given options.....")
            comic_book()
        else:
            i=b2-1
            while(b2>i):
                for co_books in (books_comic[i]):
                    a=open("E:/purchse_book.txt",'a')
                    a.write(str(co_books)+"\n \n")
                    a.close() 
                    print(co_books,end="           ")
                i+=1
                break
    except:
        print("Went something wrong......")
        a=input("Press enter to return to books collection")
        books_collection()
#novel books()
def novel_books():
    print("                   NOVEL BOOKS")
    print("No.   Auther name:                Book name:          Price:\n")
    for no,auther,book,price in(books_novel):
        print(no,"   ",auther,"    ",book,"    ",price)
    try:
        b2=int(input("Enter book number(TO PURCHASE BOOK): "))
        if(b2<=0 or b2>10):
            print("Select option from given option....")
            novel_books()
        else:
            i=b2-1
            while(b2>i):
                for n_books in (books_novel[i]):
                    a=open("E:/purchse_book.txt",'a')
                    a.write(str(n_books)+"\n \n")
                    a.close()  
                    print(n_books,end="           ")
                i+=1
                break
    except:
        print("went something wrong....")
        input("press enter ro return to books collection")
        books_collection()
#history books()
def history_books():
    print("                   HISTORY BOOKS")
    print("No.  Auther name:              Book name:         Price:\n")
    for no,auther,books,price in(books_history):
        print(no," ",auther," ",books," ",price)
    try:
        b4=int(input("Enter book number(TO PURCHASE BOOK): "))
        if b4>10 or b4<=0 :
            print("Select option from given....")
            history_books()
        else:
            i=b4-1
            while(b4>i):
                for h_book in books_history[i]:
                    b=open("E:/purchse_book.txt",'a')
                    b.write(str(h_book)+"\n \n")
                    b.close()  
                    print(h_book,end="          ")
                i+=1
                break
    except:
        print("went something wrong....")
        input("Press enter to return to books collection")
        books_collection()
quantity=0
purchase_books=[]
def order_book():
    global quantity
    global purchase_books
    order=input("Do you want to buy this book(yes/no): ")
    if(order=="yes"or order=="no"):
        if(order=="yes"):
        #books quantity
            quantity=int(input("quantity: "))
            purchase_books.append(quantity)
            if(quantity>10):
                print("Out of stock ")

                another_book=input("Do you want yo buy another book(yes/no):")
                if another_book=='yes' or another_book=='no':
                        main_menu()
                else:       
                    main_menu()
            else:   
                print("Books Ordered ")
                another_book=input("Do you want yo buy another book(yes/no):")
                if another_book=='yes' or another_book=='no':
                        main_menu()
                else:
                    main_menu()
        elif(order=="no"):
            print("Thanks for visiting here ")
            another_book=input("Do you want yo buy another book(yes/no):")
            if another_book=='yes' or another_book=='no':
                    main_menu()
            else:
                input("press enter to return to main menu")
                main_menu()
    else:
        print("Enter either yes or no :")
        order_book()

new_book=0
new_books=[]
file=0
#this funtion is for registring new books in shop
def reg_new_book():
    cls()
    global new_book
    global new_books
    global file
    print(" \nYou can add only one book at a time: ")
    print("  1.For registring new books \n  2.To check new books")
    n_books=input("Enter option from given option: ")
    if(n_books=='1'):
        for i in range(1):
            b_n=input("Enter book name: ")
            a_n=input("Enter auther name: ")
            b_p=input("Enter book price: ")
            new_books.append(b_n)
            new_books.append(a_n)
            new_books.append(b_p)
        #reg_new_book()
        a=input("\nPress 0 to return to main menu or 1 for reg menu press any other key for exit :")
        if a=='0':
            main_menu()
        elif(a=='1'):
            reg_new_book()
        
        else:
            exit()
    elif(n_books=='2'):
        print("Book name:          Auther name:           Price:")
        for i in (new_books):
           print(i,end="     ")
        new_book=new_books
        #save file in memory
        file=open("E:/new_books.txt","a")
        file.write(str(new_book))
        file.write (" \n ")
        file.close()
        a=input("\nPress 0 to return to main menu, 1 for reg new book menu and any other key for exit :")
        if a=='0':
            main_menu()
        elif(a=='1'):
            reg_new_book()
        else:
            exit()
    else:
       print("Select option from given menu: ")
       reg_new_book() 
#search function 
def search_books():
    cls()
    print("   1.Search by auther name: \n   2.Search by book name: ")
    print(""   "\n press 0 to return to the main menu"  "")
    c=input("Select option: ")
    if c=='1':
        s_auther_name()
    elif(c=='2'):
        s_book_name()
    elif(c=='0'):
        main_menu()
    else:
        print("Select option from given option....")
        search_books()
def s_auther_name():
    auther_name=input("Search Auther name(in this format\"MUHAMMAD SAMEER\"): ")
    #if auther_name in available_books:
    for i in range (40):
        for j in range(3):
            if available_books[i][j]==auther_name:
                print("Auther found \n ")
                print("Book name:           Auther name:            Price: ")
                for k in available_books[i]:
                    a=open("E:/purchse_book.txt",'a')
                    a.write(str(k)+'\n \n')
                    a.close() 
                    print(k,end="               ")
                print("\n")
                order_book()
                break
                
    
    a=input("Auther not found\n\n  press 1 to return to main menu and press any other key  for search menu : ")
    if a=='1':
        main_menu()
    else:
        search_books()

def s_book_name():
    book_n=input("Search book name(in this formate \"PAK-STUDY\": ")
    #if 'book_n' in available_books:
    for i in range (40):
        for j in range(3):
            if available_books[i][j]==book_n:
                print("Book found \n ")
                print("Book name:           Auther name:            Price: ")
                for k in available_books[i]:
                    a=open("E:/purchse_book.txt",'a')
                    a.write(str(k)+'\n \n')
                    a.close()  
                    print(k,end="               ")
                print("\n")
                order_book()
                break

    
    a=input("Book not found\n\n  press 0 to return to search menu and 1 for main menu  : ")
    if a=='1':
        main_menu()
    else:
        search_books()
    
#bill=0
def bill_of_b():
    sum=0
    for p_books in purchase_books:
        sum+=p_books
    bill=sum*(70)
    if bill==0:
        print("You do not have buy any book yet!")
        input("press enter to return to main menu ")
        main_menu()
    else:
        print("Total bill =",bill)
        credit_card=[]
        c_num=input("Enter your credit card NO (in this formate:123-456-789):")
        j=0
        for i in range(len(c_num)):
            var=c_num[j]
            credit_card.append(var)
            j += 1
        if credit_card[3]=='-' and credit_card[7]=='-':
            print("good ho gya G")

            print("Bill paid ")
            print("Thanks for shopping")
            input("Press enter to return to main menu :")
            main_menu()
        else:
            print("You entered wrong credit card  number: ")
            a=input("Enter 1 to return to bill menu, 0 for main menu and press any key for exit ")
            if a=='1':
                bill_of_b()
            elif a=='0':
                main_menu()
            else:
                exit()
#main_menu()
users={}
status=""
while status!="q":
    status=input("Are you a registred user?y/n?press q to quit:")
    if status=="q":
        exit()
    if status=="n":#creat new login
        create_login=input("Create login name:")
        if create_login in users:#check if login name exist
            print("login name already exist!\n")
        else:
            create_password=input("create password:")
            users[create_login]=create_password
            print("\nAccount created!\n")
    elif status=="y":
        login=input("Enter login name:")
        if login in users:
            passw=input("Enter password:")

             #print
            if login in users and users[login]==passw:#match user name and password
                print("Login saccesfully!\n")
                #main function of our project it controll all other funtion and interprinter start execution from here after login.
                main_menu()
            else:
                print("User does  not exist!\n ")
        else:
            print("Enter wronge login!")
#print(users)
