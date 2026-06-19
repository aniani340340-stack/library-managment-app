import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Anishop@1212",
    database='library_db'
)
print("database connection is done!")

while True:
    print("1. Add Book")
    print("2. Search Book")
    print("3. Show All Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book Data")
    print("7. Exit")
    try:
        option = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    if option==1:
        print("You have selected option 1")
        while True:
            try:
                BookId=int(input("Enter Book Id: "))
                break
            except ValueError:
                print("please write the valid value")
                continue
        # id_exist_boolean=False
        # try:
        #     with open("booksdata.csv") as file:
        #         for line in file:
        #             line=line.strip()
        #             book_list=line.split(",")
        #             if int(book_list[0])==BookId:
        #                 id_exist_boolean=True
        #                 print(f"Book with id {BookId} already exists. Please enter a unique Book Id.")
        #                 break
        # except FileNotFoundError:
        #     pass
        # if id_exist_boolean:
        #     continue
        # else:    

        while True:
            try:
                quantity=int(input("Enter Quantity: "))
                break
            except ValueError:
                print("please write the valid value")
                continue    

        BookName=input("Enter Book Name: ")
        Author=input("Enter Author Name: ")
    
            # with open("booksdata.csv","a") as file:
            #     file.write(f"{BookId},{BookName},{Author},{quantity}"+"\n")
            #     print("Book added successfully")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "SELECT * FROM books WHERE BookID=%s",
            (BookId,)
        )   

        book = my_cursor.fetchone()
        print(book)

        if book:
            print("Book ID already exists!")
        else:    
            books_query="insert into books(BookID,BookName,Author,Quantity) values (%s,%s,%s,%s)"
            book_values=(BookId,BookName,Author,quantity) 
            
            my_cursor.execute(books_query,book_values)
            print("book add sucessfully")
            conn.commit()   
    elif option==2:
        while True:
            try:
                BookId=int(input("please type the book id you want to search:"))
                break
            except ValueError:
                print("please write the correct input")
                continue
        # with open("booksdata.csv") as file:
        #     book_list=[]
        #     book_found=False
        #     for line in file:
        #         line=line.strip()
        #         book_list=line.split(",")
        #         if int(book_list[0])==BookId:
        #             print(f"Book_id:{book_list[0]}\nBook_name:{book_list[1]}\nAuthor:{book_list[2]}\nQuantity:{book_list[3]}\n")
        #             book_found=True
        #     if book_found==False:
        #         print(f"Book with id {BookId} is not found")
        sql_query="select* From books where BookId=%s"
        my_cursor=conn.cursor()
        my_cursor.execute(sql_query,(BookId,))
        book = my_cursor.fetchone()
        if book:
            print(f"BookId:{book[0]}")
            print(f"BookName:{book[1]}")
            print(f"Author:{book[2]}")
            print(f"Quantity:{book[3]}")
        else: 
            print("Book not found")   
        

    elif option==3:
        # with open("booksdata.csv") as file:
        #     for line in file:
        #         search_list=[]
        #         line=line.strip()
        #         show_list=line.split(",")
        #         print(f"Book_id:{show_list[0]}\nBook_name:{show_list[1]}\nAuthor:{show_list[2]}\nQuantity:{show_list[3]}\n")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from books")
        books=my_cursor.fetchall()
        for book in books:

            print(f"BookId:{book[0]}")
            print(f"BookName:{book[1]}")
            print(f"Author:{book[2]}")
            print(f"Quantity:{book[3]}")
            print("-"*30)            
    elif option==4:
        # with open("booksdata.csv") as file:
        #     with open("temparorydata.csv","w") as file1:
        #         id=input("please write the id of which you have issue the book")
        #         issuebook_list=[]
        #         bookissue_boolean=False
        #         for line in file:
        #             line=line.strip()
        #             issuebook_list=line.split(",")
        #             if issuebook_list[0]==id:
        #                 bookissue_boolean=True
        #                 if int(issuebook_list[3])==0:
        #                     print("Sorry, this book is currently not available for issue.")
                        
        #                     file1.write(line+"\n")
        #                     continue
        #                 else:
        #                     issuebook_list[3]=int(issuebook_list[3])
        #                     issuebook_list[3]-=1
        #                     file1.write(f"{issuebook_list[0]},{issuebook_list[1]},{issuebook_list[2]},{issuebook_list[3]}\n")
        #             else:
        #                 file1.write(line+"\n")
        # with open ("temparorydata.csv") as file:
        #     with open ("booksdata.csv","w") as file1:
        #         for line in file:
        #             file1.write(line)  
        # if bookissue_boolean==False:
        #     print(f"Book with id {id} is not found")      
        # else:
        #     print("Book issued successfully")    
        while True:
            try:       
                book_id=int(input("please write the id of book you want to issue:"))
                break
            except ValueError:
                print("please write the correct option")
                continue
        my_cursor=conn.cursor()
        my_cursor.execute("select Quantity from books where BookId=%s",(book_id,))
        book=my_cursor.fetchone()
        if book is None:
            print("no book is found")
        elif book[0]==0:
            print("quantity is zero")
        else:    
            my_cursor.execute("update books set quantity=quantity-1 where BookId=%s ",(book_id,))
            print("Issue done sucesfully")
            conn.commit()  
            # my_cursor.execute("select Quantity from books where BookId=%s",(id,))
            # book=my_cursor.fetchone
            print(f"remaning quantity:{book[0]-1}")                                 
    elif option==5:
        # with open("booksdata.csv") as file:
        #     with open("temparorydata.csv","w") as file1:
        #         id=input("please write the id of which you have issue the book")
        #         book_found=False
        #         returnbook_list=[]
        #         for line in file:
        #             line=line.strip()
        #             returnbook_list=line.split(",")
        #             if returnbook_list[0]==id:
        #                 book_found=True
        #                 returnbook_list[3]=int(returnbook_list[3])
        #                 returnbook_list[3]+=1
        #                 file1.write(f"{returnbook_list[0]},{returnbook_list[1]},{returnbook_list[2]},{returnbook_list[3]}\n ")
        #             else:
        #                 file1.write(line+"\n")
        # with open ("temparorydata.csv") as file:
        #     with open ("booksdata.csv","w") as file1:
        #         for line in file:
        #             file1.write(line)                                        
        # if book_found==False:
        #     print(f"Book with id {id} is not found")            
        # else:
        #     print("Book returned successfully")
        while True:
            try:       
                book_id=int(input("please write the id of book you want to issue:"))
                break
            except ValueError:
                print("please write the correct option")
                continue   
        my_cursor=conn.cursor()
        my_cursor.execute("select * from books where BookId=%s",(book_id,))
        book=my_cursor.fetchone()
        if book is None:
            print("no book found")
        else:    
            my_cursor.execute("update books set quantity=quantity+1 where BookId=%s ",(book_id,))
            print("book return sucessfully")
            conn.commit()
                                         
    elif option==6:
        # with open("booksdata.csv") as file:
        #     with open("temparorydata.csv","w") as file1:
        #         id=input("please write the id of which you have delete the book data")
        #         delete_boolean=False
        #         delete_list=[]
        #         for line in file:
        #             line=line.strip()
        #             deletebook_list=line.split(",")
        #             if deletebook_list[0]==id:
        #                 delete_boolean=True
        #                 continue
        #             else:
        #                 file1.write(line+"\n")
        # with open ("temparorydata.csv") as file:
        #     with open ("booksdata.csv","w") as file1:
        #         for line in file:
        #             file1.write(line)
        # if delete_boolean==False:
        #     print(f"Book with id {id} is not found")
        # else:
        #     print("Book data deleted successfully")
        while True:
            try:       
                BookId=int(input("please write the id of book you want to issue:"))
                break
            except ValueError:
                print("please write the correct option")
                continue
        my_cursor=conn.cursor()
        my_cursor.execute("delete from books where BookId=%s",(BookId,))
        if my_cursor.rowcount > 0:
            print("Book deleted")
        else:
            print("Book not found") 
        conn.commit()   
    elif option==7:
        print("Thank you for using the library management system")
        conn.close()
        break
    else:
        print("Please select the valid option")    
        continue