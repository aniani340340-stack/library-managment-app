
while True:
    print("1. Add Book")
    print("2. Search Book")
    print("3. Show All Books")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book Data")
    print("7. Exit")
    option=int(input("Enter your option: "))
    if option==1:
        print("You have selected option 1")
        while True:
            try:
                BookId=int(input("Enter Book Id: "))
                break
            except ValueError:
                print("please write the valid value")
                continue
        id_exist_boolean=False
        try:
            with open("booksdata.csv") as file:
                for line in file:
                    line=line.strip()
                    book_list=line.split(",")
                    if int(book_list[0])==BookId:
                        id_exist_boolean=True
                        print(f"Book with id {BookId} already exists. Please enter a unique Book Id.")
                        break
        except FileNotFoundError:
            pass
        if id_exist_boolean:
            continue
        else:    

            while True:
                try:
                    quantity=int(input("Enter Quantity: "))
                    break
                except ValueError:
                    print("please write the valid value")
                    continue    

            BookName=input("Enter Book Name: ")
            Author=input("Enter Author Name: ")
    
            with open("booksdata.csv","a") as file:
                file.write(f"{BookId},{BookName},{Author},{quantity}"+"\n")
                print("Book added successfully")
    elif option==2:
        while True:
            try:
                BookId=int(input("please type the book id you want to search:"))
                break
            except ValueError:
                print("please write the correct input")
                continue
        with open("booksdata.csv") as file:
            book_list=[]
            book_found=False
            for line in file:
                line=line.strip()
                book_list=line.split(",")
                if int(book_list[0])==BookId:
                    print(f"Book_id:{book_list[0]}\nBook_name:{book_list[1]}\nAuthor:{book_list[2]}\nQuantity:{book_list[3]}\n")
                    book_found=True
            if book_found==False:
                print(f"Book with id {BookId} is not found")      
    elif option==3:
        with open("booksdata.csv") as file:
            for line in file:
                search_list=[]
                line=line.strip()
                show_list=line.split(",")
                print(f"Book_id:{show_list[0]}\nBook_name:{show_list[1]}\nAuthor:{show_list[2]}\nQuantity:{show_list[3]}\n")
    elif option==4:
        with open("booksdata.csv") as file:
            with open("temparorydata.csv","w") as file1:
                id=input("please write the id of which you have issue the book")
                issuebook_list=[]
                bookissue_boolean=False
                for line in file:
                    line=line.strip()
                    issuebook_list=line.split(",")
                    if issuebook_list[0]==id:
                        bookissue_boolean=True
                        if int(issuebook_list[3])==0:
                            print("Sorry, this book is currently not available for issue.")
                        
                            file1.write(line+"\n")
                            continue
                        else:
                            issuebook_list[3]=int(issuebook_list[3])
                            issuebook_list[3]-=1
                            file1.write(f"{issuebook_list[0]},{issuebook_list[1]},{issuebook_list[2]},{issuebook_list[3]}\n")
                    else:
                        file1.write(line+"\n")
        with open ("temparorydata.csv") as file:
            with open ("booksdata.csv","w") as file1:
                for line in file:
                    file1.write(line)  
        if bookissue_boolean==False:
            print(f"Book with id {id} is not found")      
        else:
            print("Book issued successfully")                                             
    elif option==5:
        with open("booksdata.csv") as file:
            with open("temparorydata.csv","w") as file1:
                id=input("please write the id of which you have issue the book")
                book_found=False
                returnbook_list=[]
                for line in file:
                    line=line.strip()
                    returnbook_list=line.split(",")
                    if returnbook_list[0]==id:
                        book_found=True
                        returnbook_list[3]=int(returnbook_list[3])
                        returnbook_list[3]+=1
                        file1.write(f"{returnbook_list[0]},{returnbook_list[1]},{returnbook_list[2]},{returnbook_list[3]}\n ")
                    else:
                        file1.write(line+"\n")
        with open ("temparorydata.csv") as file:
            with open ("booksdata.csv","w") as file1:
                for line in file:
                    file1.write(line)                                        
        if book_found==False:
            print(f"Book with id {id} is not found")            
        else:
            print("Book returned successfully")                           
    elif option==6:
        with open("booksdata.csv") as file:
            with open("temparorydata.csv","w") as file1:
                id=input("please write the id of which you have delete the book data")
                delete_boolean=False
                delete_list=[]
                for line in file:
                    line=line.strip()
                    deletebook_list=line.split(",")
                    if deletebook_list[0]==id:
                        delete_boolean=True
                        continue
                    else:
                        file1.write(line+"\n")
        with open ("temparorydata.csv") as file:
            with open ("booksdata.csv","w") as file1:
                for line in file:
                    file1.write(line)
        if delete_boolean==False:
            print(f"Book with id {id} is not found")
        else:
            print("Book data deleted successfully")
    elif option==7:
        print("Thank you for using the library management system")
        break
    else:
        print("Please select the valid option")    
        continue