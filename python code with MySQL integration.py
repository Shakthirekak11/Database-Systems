#--------------------------------------------FUNCTIONS-------------------------------------------------------------------
def book_details():
    print("\nBOOK DETAILS")
    print("a. To display in ascending order")
    print("b. To display in descending order")
    print("c. To display in the order as stored\n")
    
    ch4 = input("Enter the choice: ")
    ch4 = ch4.lower()

    if ch4 in ('a', 'b', 'c'):
        sql_query = """
            SELECT bd.ISBN, bd.Book_title, bd.Language, bd.Genre, bd.Publisher, bd.Edition, bd.Price, 
                   bad.Author, bi.Book_ID, bi.Copies, bi.Condition, bi.Status
            FROM Book_details bd
            JOIN Book_author_details bad ON bd.ISBN = bad.ISBN
            JOIN BookInventory bi ON bad.Book_ID = bi.Book_ID
        """

        if ch4 == 'a':
            sql_query += " ORDER BY bd.Book_title ASC"
        elif ch4 == 'b':
            sql_query += " ORDER BY bd.Book_title DESC"

        mycursor.execute(sql_query)
        result = mycursor.fetchall()

        if result:
            print("Book details:")
            for row in result:
                print("ISBN:", row[0])
                print("Title:", row[1])
                print("Language:", row[2])
                print("Genre:", row[3])
                print("Publisher:", row[4])
                print("Edition:", row[5])
                print("Price:", row[6])
                print("Author:", row[7])
                print("Book ID:", row[8])
                print("Copies:", row[9])
                print("Condition:", row[10])
                print("Status:", row[11])
                print(" ")
        else:
            print("No details to display")
    else:
        print("Invalid choice")


def member_details():
    print("\nMEMBER DETAILS")
    print("a. To display in ascending order")
    print("b. To display in descending order")
    print("c. To display in the order as stored\n")

    ch4 = input("Enter the choice: ")
    ch4 = ch4.lower()

    if ch4 in ('a', 'b', 'c'):
        query = """
            SELECT md.Member_ID, md.SSN, md.Member_name, md.Gender, md.DOB, md.Address, md.Payment_Status,
                   md.Join_Date, md.Status, md.Renew_Joined, md.Amount, me.Email_ID, mpn.Phone_no
            FROM Membership_details md
            LEFT JOIN Member_Email me ON md.Member_ID = me.Member_ID
            LEFT JOIN Member_Phone_no mpn ON md.Member_ID = mpn.Member_ID
        """
        
        if ch4 == 'a':
            query += " ORDER BY md.Member_name ASC"
        elif ch4 == 'b':
            query += " ORDER BY md.Member_name DESC"

        mycursor.execute(query)
        result = mycursor.fetchall()

        if result:
            print("Member details:")
            for row in result:
                print("Member ID:", row[0])
                print("SSN:", row[1])
                print("Name:", row[2])
                print("Gender:", row[3])
                print("DOB:", row[4])
                print("Address:", row[5])
                print("Payment Status:", row[6])
                print("Join Date:", row[7])
                print("Status:", row[8])
                print("Renew Joined:", row[9])
                print("Amount:", row[10])
                print("Email:", row[11])
                print("Phone Number:", row[12])
                print(" ")
        else:
            print("No details to display")
    else:
        print("Invalid choice")


def staff_details():
    print("\nSTAFF DETAILS")
    print("a. To display in ascending order")
    print("b. To display in descending order")
    print("c. To display in the order as stored\n")

    ch4 = input("Enter the choice: ")
    ch4 = ch4.lower()

    if ch4 in ('a', 'b', 'c'):
        query = """
            SELECT s.Staff_ID, s.Staff_Name, s.Address, s.Gender, s.Join_date, s.Salary, s.Position,
                   se.Email_ID, spn.Phone_no
            FROM Staff s
            LEFT JOIN Staff_Email se ON s.Staff_ID = se.Staff_ID
            LEFT JOIN Staff_Phone_no spn ON s.Staff_ID = spn.Staff_ID
        """
        
        if ch4 == 'a':
            query += " ORDER BY s.Staff_Name ASC"
        elif ch4 == 'b':
            query += " ORDER BY s.Staff_Name DESC"

        mycursor.execute(query)
        result = mycursor.fetchall()

        if result:
            print("Staff details:")
            for row in result:
                print("Staff ID:", row[0])
                print("Name:", row[1])
                print("Address:", row[2])
                print("Gender:", row[3])
                print("Join Date:", row[4])
                print("Salary:", row[5])
                print("Position:", row[6])
                print("Email:", row[7])
                print("Phone Number:", row[8])
                print(" ")
        else:
            print("No details to display")
    else:
        print("Invalid choice")

def book_add():
    global bookID 
    mycursor.execute("INSERT INTO Book_details VALUES(%s,'%s','%s','%s','%s',%s,%s)"%(ISBN,bookTitle,language,genre,publisher,edition,price))
    mydb.commit()
    mycursor.execute("INSERT INTO BookInventory VALUES(%s,%s,'%s','%s')"%(bookID,copies,condition,status))
    mydb.commit()
    for i in authorNames:
        mycursor.execute("INSERT INTO Book_author_details VALUES(%s,%s,'%s')"%(bookID,ISBN,i))
    mydb.commit()
    bookID+=1
    print("Book added")

def book_deact(Bid): 
    mycursor.execute("UPDATE BookInventory SET `Condition`='Condemned' WHERE Book_ID=(%s)"%(Bid,))
    mycursor.execute("UPDATE BookInventory SET `Status`='Unavailable' WHERE Book_ID=(%s)"%(Bid,))
    mydb.commit()
    print("Book deactivated")

def member_add(): 
    global memberID
    mycursor.execute("INSERT INTO Membership_details VALUES(%s,%s,'%s','%s','%s','%s','%s',CURRENT_DATE(),'%s','%s',%s)"%(memberID,SSN,memberName,gender,dob,address,paymentStatus,status,'Joined',amount))
    mycursor.execute("INSERT INTO Member_details VALUES(%s,%s,'%s','%s','%s','%s',CURRENT_DATE())"%(memberID,SSN,memberName,address,gender,dob))
    for i in email:
        mycursor.execute("INSERT INTO Member_Email VALUES(%s,'%s')"%(memberID,i))
    for j in phoneno:
        mycursor.execute("INSERT INTO Member_Phone_no VALUES(%s,%s)"%(memberID,j))
    mydb.commit()
    memberID+=1
    print("Member added")

def staff_add():
    global staffID
    mycursor.execute("INSERT INTO Staff VALUES(%s,'%s','%s','%s',CURRENT_DATE(),%s,'%s')"%(staffID,staffName,address,gender,salary,position))
    for i in email:
        mycursor.execute("INSERT INTO Staff_Email VALUES(%s,'%s')"%(staffID,i))
    for j in phoneno:
        mycursor.execute("INSERT INTO Staff_Phone_no VALUES(%s,%s)"%(staffID,j))
    mydb.commit()
    staffID+=1
    print("Staff added")

def book_del(bid): 
    mycursor.execute("SELECT ISBN FROM Book_author_details WHERE Book_ID = %s", (bid,))
    isbn_result = mycursor.fetchone()
    
    if isbn_result:
        isbn = isbn_result[0]
        mycursor.fetchall()

        mycursor.execute("DELETE FROM Book_author_details WHERE Book_ID = %s", (bid,))
        mycursor.execute("DELETE FROM BookInventory WHERE Book_ID = %s", (bid,))
        mycursor.execute("DELETE FROM Book_details WHERE ISBN = %s", (isbn,))
        mydb.commit()
        print("Book deleted")
    else:
        print("Book with the provided Book_ID not found")

def mem_del(mid):

    mycursor.execute("SELECT * FROM Member_details WHERE Member_ID = %s", (mid,))
    member_result = mycursor.fetchone()
    
    if member_result:
        mycursor.fetchall()
        
        mycursor.execute("DELETE FROM Member_Email WHERE Member_ID = %s", (mid,))
        mydb.commit()
        mycursor.execute("DELETE FROM Member_Phone_no WHERE Member_ID = %s", (mid,))

        mycursor.execute("DELETE FROM Member_details WHERE Member_ID = %s", (mid,))

        mycursor.execute("DELETE FROM Membership_details WHERE Member_ID = %s", (mid,))

        mydb.commit()
        print("Member deleted")
    else:
        print("Member with the provided Member_ID not found")

def member_cancel(Mn,reason): 
    mycursor.execute("UPDATE Membership_details SET Status='Inactive' WHERE Member_ID=(%s)"%(Mn,))
    mycursor.execute("UPDATE Membership_details SET Renew_Joined=('%s') WHERE Member_ID=(%s)"%(reason,Mn))
    if (reason=='Not renewed'):
        mycursor.execute("UPDATE Membership_details SET Payment_status='Unsuccessful' WHERE Member_ID=(%s)"%(Mn,))
        mycursor.execute("UPDATE Membership_details SET Amount=499 WHERE Member_ID=(%s)"%(Mn,))
    if (reason=='Cancelled'):
        mycursor.execute("UPDATE Membership_details SET Amount=NULL WHERE Member_ID=(%s)"%(Mn,))
        
    mydb.commit()
    print("Subscription cancelled")

def search():
    print("\na.Search for a book")
    print("b.Search for a member ")
    print("c.Search for a staff\n")
    
    ch4 = input("Enter the choice: ")
    ch4 = ch4.lower()

    if ch4 == 'a':
        bid = int(input("Enter the book id: "))
        mycursor.execute("SELECT bd.ISBN, bd.Book_title, bd.Language, bd.Genre, bd.Publisher, bd.Edition, bd.Price, bad.Author, bi.Copies, bi.Condition, bi.Status FROM Book_details bd JOIN Book_author_details bad ON bd.ISBN = bad.ISBN JOIN BookInventory bi ON bad.Book_ID = bi.Book_ID WHERE bi.Book_ID = %s", (bid,))
        result = mycursor.fetchall()
        if result:
            print("Book details:")
            for row in result:
                print("ISBN:", row[0])
                print("Title:", row[1])
                print("Language:", row[2])
                print("Genre:", row[3])
                print("Publisher:", row[4])
                print("Edition:", row[5])
                print("Price:", row[6])
                print("Author:", row[7])
                print("Copies:", row[8])
                print("Condition:", row[9])
                print("Status:", row[10])
        else:
            print("Book not found.")

    elif ch4 == 'b':
        mid = int(input("Enter the member id: "))
        mycursor.execute("SELECT md.Member_ID, md.SSN, md.Member_name, md.Gender, md.DOB, md.Address, md.Payment_Status, md.Join_Date, md.Status, md.Renew_Joined, md.Amount, me.Email_ID, mpn.Phone_no FROM Membership_details md LEFT JOIN Member_Email me ON md.Member_ID = me.Member_ID LEFT JOIN Member_Phone_no mpn ON md.Member_ID = mpn.Member_ID WHERE md.Member_ID = %s", (mid,))
        result = mycursor.fetchall()
        if result:
            print("Member details:")
            for row in result:
                print("Member ID:", row[0])
                print("SSN:", row[1])
                print("Name:", row[2])
                print("Gender:", row[3])
                print("DOB:", row[4])
                print("Address:", row[5])
                print("Payment Status:", row[6])
                print("Join Date:", row[7])
                print("Status:", row[8])
                print("Renew Joined:", row[9])
                print("Amount:", row[10])
                print("Email ID:", row[11])
                print("Phone number:", row[12])
        else:
            print("Member not found.")

    elif ch4 == 'c':
        sid = int(input("Enter the staff id: "))
        mycursor.execute("SELECT s.Staff_ID, s.Staff_Name, s.Address, s.Gender, s.Join_date, s.Salary, s.Position, se.Email_ID, spn.Phone_no FROM Staff s LEFT JOIN Staff_Email se ON s.Staff_ID = se.Staff_ID LEFT JOIN Staff_Phone_no spn ON s.Staff_ID = spn.Staff_ID WHERE s.Staff_ID = %s", (sid,))
        result = mycursor.fetchall()
        if result:
            print("Staff details:")
            for row in result:
                print("Staff ID:", row[0])
                print("Name:", row[1])
                print("Address:", row[2])
                print("Gender:", row[3])
                print("Join Date:", row[4])
                print("Salary:", row[5])
                print("Position:", row[6])
                print("Email ID:", row[7])
                print("Phone number:", row[8])
        else:
            print("Staff not found.")
    else:
        print("Invalid choice")

def modify_mem():
    mid=int(input("Enter the member id of the member to be modified:"))
    print("\na.Address")
    print("b.Contact")
    print("c.Email\n")

    ch4=input("Enter the choice:")
    ch4 = ch4.lower()

    if ch4=='a':
        add=input("Enter the new address:")
        mycursor.execute("UPDATE Membership_details SET Address=('%s') WHERE Member_ID=(%s)"%(add,mid))
        mycursor.execute("UPDATE Member_details SET Address=('%s') WHERE Member_ID=(%s)"%(add,mid))
        mydb.commit()
        print("Address has been updated")

    elif ch4=='b':
        mycursor.execute("DELETE FROM Member_phone_no WHERE Member_ID=(%s)"%(mid,))
        mydb.commit()
        phoneno=input("Enter the phone numbers seperated by commas(,):")
        phoneno = [no.strip() for no in phoneno.split(",")]
        for i in phoneno:
            mycursor.execute("INSERT INTO Member_Phone_no VALUES(%s,%s)"%(i,mid))
        mydb.commit()
        print("Contact number has been updated")

    elif ch4=='c':
        mycursor.execute("DELETE FROM Member_Email WHERE Member_ID=(%s)"%(mid,))
        mydb.commit()
        email=input("Enter the emails seperated by commas(,):")
        email = [mail.strip() for mail in email.split(",")]
        for j in email:
            mycursor.execute("INSERT INTO Member_Email VALUES(%s,'%s')"%(mid,j))
        mydb.commit()
        print("Email has been updated")

def modify_staff():
    sid=int(input("Enter the staff id of the staff to be modified:"))
    print("\na.Address")
    print("b.Contact")
    print("c.Email\n")

    ch4=input("Enter the choice:")
    ch4 = ch4.lower()

    if ch4=='a':
        add=input("Enter the new address:")
        mycursor.execute("UPDATE Staff SET Address=('%s') WHERE Staff_ID=(%s)"%(add,sid))
        mydb.commit()
        print("Address has been updated")

    elif ch4=='b':
        mycursor.execute("DELETE FROM Staff_phone_no WHERE Staff_ID=(%s)"%(sid,))
        mydb.commit()
        phoneno=input("Enter the phone numbers seperated by commas(,):")
        phoneno = [no.strip() for no in phoneno.split(",")]
        for i in phoneno:
            mycursor.execute("INSERT INTO Staff_Phone_no VALUES(%s,%s)"%(sid,i))
        mydb.commit()
        print("Contact number has been updated")

    elif ch4=='c':
        mycursor.execute("DELETE FROM Staff_Email WHERE Staff_ID=(%s)"%(sid,))
        mydb.commit()
        email=input("Enter the emails seperated by commas(,):")
        email = [mail.strip() for mail in email.split(",")]
        for j in email:
            mycursor.execute("INSERT INTO Staff_Email VALUES(%s,'%s')"%(sid,j))
        mydb.commit()
        print("Email has been updated")

def renew_mem():
    mid=int(input("Enter the member id to be renewed:"))
    mycursor.execute("UPDATE Membership_details SET Status='Active' WHERE Member_ID=(%s)"%(mid,))
    mycursor.execute("UPDATE Membership_details SET Renew_Joined='Renewed' WHERE Member_ID=(%s)"%(mid,))
    mycursor.execute("UPDATE Membership_details SET Payment_status='Successful' WHERE Member_ID=(%s)"%(mid,))
    mycursor.execute("UPDATE Membership_details SET Amount=499 WHERE Member_ID=(%s)"%(mid,))
    mydb.commit()
    print("Membership has been renewed")

def staff_del():
    sid=int(input("Enter the staff id of the staff to be deleted:"))
    mycursor.execute("DELETE FROM Staff_Email WHERE Staff_ID=(%s)"%(sid,))
    mydb.commit()
    mycursor.execute("DELETE FROM Staff_Phone_no WHERE Staff_ID=(%s)"%(sid,))
    mydb.commit()
    mycursor.execute("DELETE FROM Staff WHERE Staff_ID=(%s)"%(sid,))
    mydb.commit()
    print("Staff has been deleted")

def book_borrow():
    global borrowID
    bid = int(input("Enter the book id of the book:"))
    mycursor.execute("SELECT status FROM BookInventory WHERE Book_ID = %s" % bid)
    result = mycursor.fetchone()
    if result and result[0] == 'Checked Out':
        print("Sorry, book is unavailable at the moment")
    else:
        mid = int(input("Enter the member id of the member:"))
        mycursor.execute("SELECT Member_ID FROM member_details WHERE Member_ID = %s" % mid)
        member_exists = mycursor.fetchone()
        if not member_exists:
            print("Invalid member ID. Please enter a valid member ID.")
            return
        sid = int(input("Enter the staff id of the staff issuing the book:"))
        rdate = input("Enter the return date:")
        mycursor.execute("INSERT INTO Book_borrow VALUES (%s, %s, %s, CURRENT_DATE(), '%s')" % (borrowID, mid, bid, rdate))
        mycursor.execute("UPDATE BookInventory SET Status = 'Checked Out' WHERE Book_Id = %s" % bid)
        mycursor.execute("INSERT INTO Issues VALUES (%s, %s)" % (sid, bid))
        mydb.commit()
        print("Book borrowed successfully with the borrow id:", borrowID)
        borrowID += 1

def book_return():
    global returnID
    from datetime import date
    current_date = date.today()
    boid = int(input("Enter the borrow id: "))
    sid = int(input("Enter the staff id: "))

    mycursor.execute("SELECT Member_ID, Book_ID, Return_date FROM Book_borrow WHERE Borrow_ID = %s", (boid,))
    result = mycursor.fetchone()
    rdate=result[2]
    mid=result[0]
    bid=result[1]

    if current_date > rdate:
        days = (current_date - rdate).days
        fine = days * 2
        mycursor.execute("INSERT INTO Book_return (Return_ID, Borrow_ID, Member_ID, Book_ID, Staff_ID, Return_date, Returned_date, Fine) VALUES (%s, %s, %s, %s, %s, %s, CURRENT_DATE(), %s)", (returnID, boid, mid, bid, sid, rdate, fine))
        mydb.commit()
        mycursor.execute("INSERT INTO Fine_Overdue VALUES (%s, %s, %s, %s, CURRENT_DATE(), %s, '%s')", (fineID, boid, returnID, rdate, fine, 'Unpaid'))
        mycursor.execute("UPDATE BookInventory SET Status='Available' WHERE Book_ID = %s", (bid,))
        mydb.commit()
        print("Book returned successfully with fine.")
    elif current_date <= rdate:
        mycursor.execute("INSERT INTO Book_return (Return_ID, Borrow_ID, Member_ID, Book_ID, Staff_ID, Return_date, Returned_date, Fine) VALUES (%s, %s, %s, %s, %s, %s, CURRENT_DATE(), %s)", (returnID, boid, mid, bid, sid, rdate, 0))
        mycursor.execute("UPDATE BookInventory SET Status='Available' WHERE Book_ID = %s", (bid,))
        mydb.commit()
        print("Book returned successfully with no fines.")
        returnID += 1
    else:
        print("No record found for borrow ID:", boid)

def fine_pay():
    fid=int(input("Enter the fine id:"))
    mycursor.execute("UPDATE Fine_Overdue SET Amount=0 and Payment_status='Paid';")

def trans_details():
    print("\na.Borrow details")
    print("b.Return details")
    print("c.Fine details\n")

    ch4=input("Enter the choice:")
    ch4 = ch4.lower()

    if (ch4=='a'):
        mycursor.execute("SELECT * FROM Book_borrow;")
        result = mycursor.fetchall()
        if result:
            for row in result:
                print(" | ".join(str(col) for col in row))
        else:
            print("No details to display")
        mydb.commit()
    elif (ch4=='b'):
        mycursor.execute("SELECT * FROM Book_return;")
        result = mycursor.fetchall()
        if result:
            for row in result:
                print(" | ".join(str(col) for col in row))
        else:
            print("No details to display")
        mydb.commit()
    elif (ch4=='c'):
        mycursor.execute("SELECT * FROM Fine_Overdue;")
        result = mycursor.fetchall()
        if result:
            for row in result:
                print(" | ".join(str(col) for col in row))
        else:
            print("No details to display")
        mydb.commit()
    else:
        print("Invalid choice")

#-------------------------------------------MAIN PROGRAM-----------------------------------------------------------------

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sample123",
    auth_plugin='caching_sha2_password'
)
mycursor=mydb.cursor()

database_name = "Library"
mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))

mycursor.execute("USE {}".format(database_name))


create_table_query="""
CREATE TABLE IF NOT EXISTS Book_details (
    ISBN VARCHAR(20) PRIMARY KEY,
    Book_title VARCHAR(255) NOT NULL,
    Language VARCHAR(50),
    Genre VARCHAR(50),
    Publisher VARCHAR(100),
    Edition VARCHAR(50),
    Price DECIMAL(10, 2)
);
"""    # -----------------------------------------------------------------------Book_details
mycursor.execute(create_table_query)
mydb.commit()

create_table_query = """
CREATE TABLE IF NOT EXISTS BookInventory (
    Book_ID INT PRIMARY KEY,
    Copies INT NOT NULL DEFAULT 1,
    `Condition` VARCHAR(50) DEFAULT 'Active',
    `Status` VARCHAR(50) DEFAULT 'Available'
);
"""     #------------------------------------------------------------------BookInventory
mycursor.execute(create_table_query)
mydb.commit()

create_trigger_condition = """
CREATE TRIGGER IF NOT EXISTS check_condition BEFORE INSERT ON BookInventory
FOR EACH ROW
BEGIN
    IF NEW.Condition NOT IN ('Active', 'Condemned') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Condition must be either Active or Condemned ';
    END IF;
END;
"""

mycursor.execute(create_trigger_condition)
mydb.commit()

create_trigger_status = """
CREATE TRIGGER IF NOT EXISTS check_status BEFORE INSERT ON BookInventory
FOR EACH ROW
BEGIN
    IF NEW.status NOT IN ('Available','Checked Out','Unavailable') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'status must be either Available or Checked Out or Unavailable';
    END IF;
END;
"""

mycursor.execute(create_trigger_status)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Book_author_details (
    Book_ID INT,
    ISBN VARCHAR(20),
    Author VARCHAR(50),
    PRIMARY KEY (Book_ID,ISBN, Author),
    FOREIGN KEY(Book_ID) REFERENCES BookInventory(Book_ID),
    FOREIGN KEY (ISBN) REFERENCES Book_details(ISBN)
);
"""   #----------------------------------------------------------------------Book_author_details
mycursor.execute(create_table_query)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Staff (
    Staff_ID INT PRIMARY KEY,
    Staff_Name VARCHAR(50) NOT NULL,
    Address VARCHAR(50),
    Gender VARCHAR(10) NOT NULL,
    Join_date DATE,
    Salary DECIMAL(10,2),
    Position VARCHAR(50)
);
"""    #-----------------------------------------------------------------------------------Staff
mycursor.execute(create_table_query)
mydb.commit()


create_trigger_gender = """
CREATE TRIGGER IF NOT EXISTS check_gender BEFORE INSERT ON Staff
FOR EACH ROW
BEGIN
    IF NEW.Gender NOT IN ('M', 'F', 'O') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Gender must be either M, F, or O';
    END IF;
END;
"""

mycursor.execute(create_trigger_gender)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Staff_Email (
    Staff_ID INT,
    Email_ID VARCHAR(50),
    PRIMARY KEY(Staff_ID,Email_ID),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);
"""  #-----------------------------------------------------------------------------------Staff_Email
mycursor.execute(create_table_query)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Staff_Phone_no (
    Staff_ID INT,
    Phone_no BIGINT,
    PRIMARY KEY(Staff_ID,Phone_no),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);
"""  #-----------------------------------------------------------------------------------Staff_Phone_no
mycursor.execute(create_table_query)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Issues (
    Staff_ID INT,
    Book_ID INT,
    PRIMARY KEY(Staff_ID,Book_ID),
    FOREIGN KEY(Staff_ID) REFERENCES Staff(Staff_ID),
    FOREIGN KEY(Book_ID) REFERENCES BookInventory(Book_ID)
);
"""  #-----------------------------------------------------------------------------------Issues
mycursor.execute(create_table_query)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Membership_details (
    Member_ID INT PRIMARY KEY,
    SSN INT,
    Member_name VARCHAR(50),
    Gender VARCHAR(10) NOT NULL,
    DOB DATE,
    Address VARCHAR(100),
    Payment_Status VARCHAR(20),
    Join_Date DATE,
    Status VARCHAR(20),
    Renew_Joined VARCHAR(20) DEFAULT NULL,
    Amount DECIMAL(10,2) DEFAULT NULL
);
"""  #-----------------------------------------------------------------------------------Membership_details
mycursor.execute(create_table_query)
mydb.commit()

create_trigger_gender_1 = """
CREATE TRIGGER IF NOT EXISTS check_gender_1 BEFORE INSERT ON Membership_details
FOR EACH ROW
BEGIN
    IF NEW.Gender NOT IN ('M', 'F', 'O') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Gender must be either M, F, or O';
    END IF;
END;
"""

mycursor.execute(create_trigger_gender_1)
mydb.commit()

create_trigger_renew_joined = """
CREATE TRIGGER IF NOT EXISTS check_renew_joined BEFORE INSERT ON Membership_details
FOR EACH ROW
BEGIN
    IF NEW.Renew_Joined NOT IN ('Joined','Renewed','Not renewed','Cancelled') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Gender must be either Joined or Renewed or Not renewed or Cancelled';
    END IF;
END;
"""

mycursor.execute(create_trigger_renew_joined)
mydb.commit()

create_trigger_status_1 = """
CREATE TRIGGER IF NOT EXISTS check_status_1 BEFORE INSERT ON Membership_details
FOR EACH ROW
BEGIN
    IF NEW.status NOT IN ('Active','Inactive') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'status must be either Active or Inactive';
    END IF;
END;
"""

mycursor.execute(create_trigger_status_1)
mydb.commit()

create_table_query = """
CREATE TABLE IF NOT EXISTS Member_details (
    Member_ID INT PRIMARY KEY,
    SSN INT,
    Member_name VARCHAR(255) NOT NULL,
    Address VARCHAR(255),
    Gender VARCHAR(10) NOT NULL,
    DOB DATE,
    Join_date DATE,
    FOREIGN KEY (Member_ID) REFERENCES Membership_details(Member_ID)
);
"""  #-----------------------------------------------------------------------------------Member_details
mycursor.execute(create_table_query)
mydb.commit()

create_trigger_gender_2 = """
CREATE TRIGGER IF NOT EXISTS check_gender_2 BEFORE INSERT ON Member_details
FOR EACH ROW
BEGIN
    IF NEW.Gender NOT IN ('M', 'F', 'O') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Gender must be either M, F, or O';
    END IF;
END;
"""
mycursor.execute(create_trigger_gender_2)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Member_Email (
    Member_ID INT,
    Email_ID VARCHAR(50),
    PRIMARY KEY(Member_ID,Email_ID),
    FOREIGN KEY (Member_ID) REFERENCES Membership_details(Member_ID)
);
"""  #-----------------------------------------------------------------------------------Member_Email
mycursor.execute(create_table_query)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Member_Phone_no (
    Member_ID INT,
    Phone_no BIGINT,
    PRIMARY KEY(Member_ID,Phone_no), 
    FOREIGN KEY (Member_ID) REFERENCES Membership_details(Member_ID)
);
"""  #-----------------------------------------------------------------------------------Member_Phone_no
mycursor.execute(create_table_query)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Book_borrow (
    Borrow_ID INT PRIMARY KEY,
    Member_ID INT,
    Book_ID INT,
    Borrow_date DATE,
    Return_date DATE,
    FOREIGN KEY (Member_ID) REFERENCES Member_details(Member_ID),
    FOREIGN KEY (Book_ID) REFERENCES BookInventory(Book_ID)
);
"""  #-----------------------------------------------------------------------------------Book_borrow
mycursor.execute(create_table_query)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Book_Return (
    Return_ID INT PRIMARY KEY,
    Borrow_ID INT,
    Member_ID INT,
    Book_ID INT,
    Staff_ID INT,
    Return_Date DATE,
    Returned_Date DATE,
    Fine DECIMAL(10,2),
    FOREIGN KEY (Borrow_ID) REFERENCES Book_borrow(Borrow_ID),
    FOREIGN KEY(Member_ID) REFERENCES Member_details(Member_ID),
    FOREIGN KEY(Book_ID) REFERENCES BookInventory(Book_ID),
    FOREIGN KEY (Staff_ID) REFERENCES Staff(Staff_ID)
);
"""  #-----------------------------------------------------------------------------------Book_return
mycursor.execute(create_table_query)
mydb.commit()

create_table_query="""
CREATE TABLE IF NOT EXISTS Fine_Overdue (
    Fine_ID INT PRIMARY KEY,
    Borrow_ID INT,
    Return_ID INT,
    Book_ID INT,
    Date DATE,
    Amount DECIMAL(10,2),
    Payment_Status VARCHAR(20) NOT NULL DEFAULT 'Unpaid',
    FOREIGN KEY (Borrow_ID) REFERENCES Book_borrow(Borrow_ID),
    FOREIGN KEY (Return_ID) REFERENCES Book_return(Return_ID),
    FOREIGN KEY(Book_ID) REFERENCES BookInventory(Book_ID)
);
"""  #-----------------------------------------------------------------------------------Fine_overdue
mycursor.execute(create_table_query)
mydb.commit()

create_trigger_payment_status = """
CREATE TRIGGER IF NOT EXISTS check_payment_status BEFORE INSERT ON Fine_Overdue
FOR EACH ROW
BEGIN
    IF NEW.Payment_Status NOT IN ('Completed','Incomplete') THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Payment_Status must be either Completed or Incomplete';
    END IF;
END;
"""
mycursor.execute(create_trigger_payment_status)
mydb.commit()

mydb.commit()
print("Required database and tables have been created.")

mycursor.execute("SELECT * FROM BookInventory;")
row_count1 = mycursor.fetchall()
if not row_count1:
    bookID=10001
else:
    max_id1=max(row[0] for row in row_count1) 
    bookID=max_id1+1

mycursor.execute("SELECT * FROM Staff;")
row_count2 = mycursor.fetchall()
if not row_count2:
    staffID=20001
else:
    max_id2=max(row[0] for row in row_count2) 
    staffID=max_id2+1

mycursor.execute("SELECT * FROM Membership_details;")
row_count3 = mycursor.fetchall()
if not row_count3:
    memberID=30001
else:
    max_id3=max(row[0] for row in row_count3) 
    memberID=max_id3+1

mycursor.execute("SELECT * FROM Book_borrow;")
row_count4 = mycursor.fetchall()
if not row_count4:
    borrowID=40001
else:
    max_id4=max(row[0] for row in row_count4) 
    borrowID=max_id4+1

mycursor.execute("SELECT * FROM Book_return;")
row_count5 = mycursor.fetchall()
if not row_count5:
    returnID=50001
else:
    max_id5=max(row[0] for row in row_count5) 
    returnID=max_id5+1

mycursor.execute("SELECT * FROM Fine_Overdue;")
row_count6 = mycursor.fetchall()
if not row_count6:
    fineID=60001
else:
    max_id6=max(row[0] for row in row_count6) 
    fineID=max_id6+1


while True:
    print("\n---LIBRARY MENU---")
    print("1.Book details")
    print("2.Member details")
    print("3.Staff details")
    print("4.Book addition")
    print("5.Book deletion")
    print("6.Book deactivation")
    print("7.Member addition")
    print("8.Modify member details")
    print("9.Member deletion")
    print("10.Member cancellation")
    print("11.Renew Membership")
    print("12.Staff addition")
    print("13.Modify staff details")
    print("14.Staff deletion")
    print("15.Borrow book")
    print("16.Return book")
    print("17.Fine payment")
    print("18.Search")
    print("19.transaction details")
    print("0.Exit\n")

    ch=int(input("Enter the choice:"))

    if (ch==1):
        book_details()

    elif (ch==4 or ch==7 or ch==12):
        if (ch==4):
            while True:
                ISBN=int(input("Enter the ISBN:"))
                bookTitle=input("Enter the book title:")
                authorNames=input("Enter the author names seperated by commas(,):")
                authorNames = [name.strip() for name in authorNames.split(",")]
                publisher=input("Enter the publisher's name:")
                edition=int(input("Enter the edition year:"))
                price=float(input("Enter the price:"))
                genre=input("Enter the genre:")
                language=input("Enter the language:")
                copies=int(input("Enter the number of copies present:"))
                condition=input("Enter whether Active/Condemned:")
                status=input("Enter the status as Available/Checked Out:")
                book_add()
                rec=input("Enter more records?(y/n):")
                rec=rec.lower()
                if rec=='y':
                    continue
                else:
                    break
        if (ch==7):
            while True:
                SSN=int(input("Enter the SSN:"))
                memberName=input("Enter the member name:")
                gender=input("Enter the gender as (M-male, F-female,O-others):")
                address=input("Enter the address:")
                dob=input("Enter the date of birth:")
                phoneno=input("Enter the phone numbers seperated by commas(,):")
                phoneno = [no.strip() for no in phoneno.split(",")]
                email=input("Enter the emails seperated by commas(,):")
                email = [mail.strip() for mail in email.split(",")]
                paymentStatus=input("Enter the payment status as(Successful/Unsuccessful):")
                status=input("Enter the status as (Active/Inactive):")
                amount=float(input("Enter the amount:"))
                member_add()
                rec=input("Enter more records?(y/n):")
                rec=rec.lower()
                if rec=='y':
                    continue
                else:
                    break
        elif (ch==12):
            while True:
                staffName=input("Enter the staff name:")
                gender=input("Enter the gender as (M-male, F-female, O-others):")
                address=input("Enter the address:")
                phoneno=input("Enter the phone numbers seperated by commas(,):")
                phoneno = [no.strip() for no in phoneno.split(",")]
                email=input("Enter the emails seperated by commas(,):")
                email = [mail.strip() for mail in email.split(",")]
                salary=float(input("Enter the salary:"))
                position=input("Enter the position:")
                staff_add()
                rec=input("Enter more records?(y/n):")
                rec=rec.lower()
                if rec=='y':
                    continue
                else:
                    break

    elif (ch==5 or ch==9):
        if (ch==5):
            bid=int(input("Enter the book ID of the book to be deleted:"))
            book_del(bid)

        elif (ch==9):
            mid=int(input("Enter the member ID of the member to be deleted:"))
            mem_del(mid)
    
    elif (ch==6):
        Bid=int(input("Enter the book Id of the book to be deactivated:"))
        book_deact(Bid)

    elif (ch==2):
        member_details()

    elif (ch==3):
        staff_details()

    elif (ch==10):
        Mid=int(input("Enter the member ID of the member to be cancelled:"))
        reason=input("Enter the reason for cancellation:")
        member_cancel(Mid, reason)
    
    elif (ch==18):
        search()

    elif (ch==8):
        modify_mem()

    elif (ch==13):
        modify_staff()

    elif (ch==11):
        renew_mem()

    elif (ch==14):
        staff_del()

    elif (ch==15):
        book_borrow()

    elif (ch==0):
        break

    elif (ch==17):
        fine_pay()

    elif (ch==16):
        book_return()
    
    elif (ch==19):
        trans_details()

    else:
        print("Invalid choice")
            
mydb.close()
