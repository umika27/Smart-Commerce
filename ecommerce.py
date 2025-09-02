# Project Title  : E-commerce
# Version        : 1.0 2024-2025
# Developed By   : Umika Sood
# Last Updated On: 2024-10-15

import mysql.connector
mydb=mysql.connector.connect(host='localhost', user='root', passwd='yourpassword')
csr=mydb.cursor()
try:
    csr.execute('CREATE DATABASE ECOMMERCE')
    print('*'*10+"Welcome"+'*'*10)
except:
    print('*'*10+"Welcome"+'*'*10)
csr.execute("USE ECOMMERCE")






#User Defined Functions:



def CreateTables():
    try:
        csr.execute('CREATE TABLE ADMIN(AdmnId CHAR(5) PRIMARY KEY, Admnname VARCHAR(40), Password VARCHAR(5))')
    except:
        print('')
    try:
        csr.execute('CREATE TABLE USERS(UserId char(5) PRIMARY KEY, Name varchar(40), EmailId varchar(30), MobileNo CHAR(10), Address varchar(80), State varchar(30), Password varchar(5))')
    except:
        print('')
    try:
        csr.execute('CREATE TABLE PRODUCTS(ProductId Char(5) PRIMARY KEY, Pname varchar(30), Description varchar(50), Category varchar(20), Dtype varchar(10), Price float(8,2), Qty int, State varchar(25))')
    except:
        print('')
    try:
        csr.execute('CREATE TABLE ORDERS(OrderId Char(5) PRIMARY KEY, UserId Char(5), ProductIds Varchar(100),TotalCost float, Odate DATE, Ddate DATE)')
    except:
        print('')
    try:
        csr.execute('CREATE TABLE SHOPPINGCART(UserId char(5), ProductId char(5),PPrice float,Qty int, TPrice float, MOP varchar(20))')
    except:
        print("")
    try:
        csr.execute('CREATE TABLE REVIEWS(UserId char(5),ProductId char(5), OrderId char(5), Rating int, Review varchar(80))')
    except:
        print("")
    try:
        csr.execute('CREATE TABLE GRIEVANCES(UserId char(5), OrderId char(5), Tgrieve varchar(20), Sgrieve varchar(90), SolGrieve varchar (40))')
    except:
        print('')
    try:
        csr.execute('Create Table ORDERNO(Ordernum int Default 0)')
    except:
        print('')
    mydb.commit()


#Admin

def AddAdmin():
    result = csr.fetchall()
    AdmnId= int(input('Enter Admin Id: '))
    Admnname=input('Enter Admin Name: ')
    Password=input('Enter Password(5 characters only): ')
    try:
        query="INSERT into ADMIN values (%s, '%s' , '%s' )"%(AdmnId,Admnname,Password)
        csr.execute(query)
        mydb.commit()
    except:
        print('Invalid Input')
def AdmnLogin():
    print("Enter 0 if you don't have an account")
    UAdmnId=input('Enter Admin Id: ')
    if UAdmnId=='0':
        return False
    else:
        UAdmnname=input('Enter Admin Name: ')
        q1="select * from Admin where AdmnId= '%s'"%UAdmnId
        csr.execute(q1)
        d=csr.fetchone()
        ctr=0
        if d is None:
            print('AdmnId does not Exist')
            return False
        else:
            while ctr<2:
                UPassword=input('Enter Password: ')
                if d[2]==UPassword:
                    return True
                else:
                    print('Incorrect Password. Retry!')

                    ctr+=1
            return False
def ShowAdmn():
    csr.execute('Select * from ADMIN')
    mydata=csr.fetchall()
    print("|%6s | %20s | %6s |"%("AdmnId","Admnname", "Password"))
    print('-'*(6+20+6+10))
    for AdmnId,Admnname, Password in mydata:
        print("|%6s | %20s | %6s |"%(AdmnId,Admnname, Password))
    print('-'*(6+20+6+10))

#Users
def RegisterUser():
    Name=input("Enter your Name: ")
    EmailId=input("Enter Email Id: ")
    MobileNo=input("Enter Mobile No.: ")
    Address=input("Enter Address: ")
    State=input("Enter State: ")
    Password=input("Enter Password(5 characters)")
    UserId=Name[0:3]+str(MobileNo)[-3:-1]
    print('*'*10)
    print()
    print('*'*10)
    print("User ID: ", UserId)
    print('*'*10)
    print()
    print()
    q10="INSERT INTO USERS values('%s','%s','%s','%s','%s','%s','%s')" %(UserId, Name, EmailId, MobileNo, Address, State, Password)
    csr.execute(q10)
    mydb.commit()

def LoginUser():
    print("Press Enter If You do not have UserId")
    UId=input("Enter UserId: ")
    if len(UId)==0:
        return False
    else:
        q11="SELECT Password from USERS where UserId= '%s'"%UId
        csr.execute(q11)
        password=csr.fetchone()
        if password is None:
            return False
        else:
            for i in password:
                pswrd=i
            ctr=0
            while ctr<2:
                Upassword=input("Password: ")
                if Upassword==pswrd:
                    return True
                else:
                    ctr+=1
                    print("Retry!")
            return False
def ShowAllUsers():
    try:
        csr.execute('SELECT * from USERS')
        udata=csr.fetchall()
        print("| %6s | %20s | %35s | %11s | %30s | %12s | %8s |" %("UId","Name", "EmailId", "MobileNo", "Address", "State", "Pwrd"))
        print('-' * (6+30+30+12+50+20+6+2))
        for UserId, Name, EmailId, MobileNo, Address, State, Password in udata:
            print("| %6s | %20s | %35s | %11s | %30s | %12s | %8s |" %(str(UserId), str(Name), str(EmailId), str(MobileNo), str(Address), str(State), str(Password)))
        print('-' * (6+30+30+12+50+20+6+2))

    except:
        print("Unexpected Error! Sorry for inconvinience.")
def ShowUsersByState():
    ustate=input("Enter State Name: ")
    try:
        q12= "SELECT * from USERS where State= '%s'"%ustate
        csr.execute(q12)
        udata=csr.fetchall()
        print("| %6s | %20s | %35s | %11s | %30s | %12s | %8s |" %("UId","Name", "EmailId", "MobileNo", "Address", "State", "Pwrd"))
        print('-' * (6+30+30+12+50+20+6+2))
        for UserId, Name, EmailId, MobileNo, Address, State, Password in udata:
            print("| %6s | %20s | %35s | %11s | %30s | %12s | %8s |" %(str(UserId), str(Name), str(EmailId), str(MobileNo), str(Address), str(State), str(Password)))
        print('-' * (6+30+30+12+50+20+6+2))
    except:
        print("Unexpected Error! Sorry for inconvinience.")


#Product

def AddProduct():
    ProductId= input("Enter the Product Id: ")
    Pname= input("Enter the Product name: ")
    Description= input("Enter Product Description: ")
    Category= input("Enter Category of Product: ")
    Dtype= input("Type of Delivery(Long/Instant): ")
    Price=float(input("Enter Price of Product: "))
    Qty= int(input("Enter Quantity of Product: "))
    State=input("Enter State where product was available: ")
    try:
        q2="INSERT INTO PRODUCTS values('%s','%s','%s','%s','%s',%s,%s, '%s')"%(ProductId, Pname, Description, Category, Dtype, Price, Qty, State)
        csr.execute(q2)
        print("Product Added Successfully!")
        mydb.commit()
    except:
        print("Unexpected Error! Sorry for inconvinience.")
def UpdateProduct():
    PId=input('Enter Product Id: ')
    ch= input("What do you Want to Update? (Pname, Description, Category, Dtype, Price,Qty,State): ")
    try:
        if ch.lower() not in ['price', 'qty']:
            nval= input("Enter Updated Value: ")
            q3= "UPDATE PRODUCTS SET %s = '%s' WHERE ProductId= '%s'"%(ch,nval,PId)
        elif ch.upper()=='PRICE':
            nval= float(input("Enter Updated Value: "))
            q3="UPDATE PRODUCTS SET PRICE = %s WHERE ProductId= '%s'"%(nval,PId)
        elif ch.lower()=='qty':
            nval=int(input("Enter Updated Quantity: "))
            q3="UPDATE PRODUCTS SET Qty =%s WHERE ProductId='%s'"%(nval,PId)
        csr.execute(q3)
        print("Product Updated Successfully")
        mydb.commit()
    except:
        print("Unexpected Error! Sorry for inconvinience.")
def DeleteProduct():
    PId=input("Enter the Product Id to be deleted: ")
    try:
        q="Delete from PRODUCTS WHERE ProductId='%s'"%PId
        csr.execute(q)
        print("Deleted Product Successfully")
        mydb.commit()
    except:
        print("Invalid ProductId")
def ShowAllProduct():
    try:
        csr.execute('Select * from PRODUCTS')
        mydata=csr.fetchall()
        print("| %6s | %20s | %40s | %15s | %10s | %8s | %6s | %20s |"%("PId", "Pname", "Description", "Category", "Dtype", "Price", "Qty", "State"))
        print('-'*(6+20+40+15+10+8+6+20+16+8))
        for ProductId, Pname, Description, Category, Dtype, Price, Qty, State in mydata:
            print("| %6s | %20s | %40s | %15s | %10s | %8s | %6s | %20s |"%(ProductId, Pname, Description, Category, Dtype, str(Price), str(Qty), State))
        print('-'*(6+20+40+15+10+8+6+20+16+8))
    except:
        print("Unexpected Error!")
def ViewSelectedProduts():
    opt=input('''Enter Category to choose from:
              A. Category
              B. Price
              C. Location: ''')
    if opt.lower()=='a':
        ucat=input('''Choose a category(Enter Category Name)
                   A.Grocery
                   B.Electronics
                   C.Beauty
                   D.Fashion
                   E.Sports
                   F.Stationary
                   G.Toys
                   H.Books
                   I.Home: ''')
        q13="Select * from PRODUCTS Where CATEGORY= '%s'"%ucat
    elif opt.lower()=='b':
        llimit=float(input("Enter Lower Limit: "))
        ulimit=float(input("Enter Upper Limit: "))
        q13="Select * from PRODUCTS Where Price between %s and %s"%(llimit, ulimit)
    elif opt.lower()=='c':
        ustate=input("Enter State: ")
        q13="Select * from PRODUCTS Where State='%s'" %ustate
    else:
        print("Invalid Option")
    try:
        csr.execute(q13)
        mydata=csr.fetchall()
        print("| %6s | %20s | %40s | %15s | %10s | %8s | %6s | %20s |"%("PId", "Pname", "Description", "Category", "Dtype", "Price", "Qty", "State"))
        print('-'*(6+20+40+15+10+8+6+20+16+8))
        for ProductId, Pname, Description, Category, Dtype, Price, Qty, State in mydata:
            print("| %6s | %20s | %40s | %15s | %10s | %8s | %6s | %20s |"%(ProductId, Pname, Description, Category, Dtype, str(Price), str(Qty), State))
        print('-'*(6+20+40+15+10+8+6+20+16+8))
    except:
        print("Unexpected Error! Sorry for Inconvinience.")
def ProductSort():
    opt=int(input('''Enter the number of your choice:
                     1. Sort from highest to lowest(by price)
                     2. Sort from lowest to highest (by price)
                     3. View Products with Long Delivery
                     4. View Products with Instant Delivery: '''))
    if opt==1:
        q56="SELECT * FROM PRODUCTS ORDER BY Price"
    elif opt==2:
        q56="SELECT * FROM PRODUCTS ORDER BY Price desc"
    elif opt==3:
        q56="SELECT * FROM PRODUCTS where Dtype='Long'"
    elif opt==4:
        q56="SELECT * FROM PRODUCTS where Dtype='Instant'"
    try:
        csr.execute(q56)
        mydata=csr.fetchall()
        print("| %6s | %20s | %40s | %15s | %10s | %8s | %6s | %20s |"%("PId", "Pname", "Description", "Category", "Dtype", "Price", "Qty", "State"))
        print('-'*(6+20+40+15+10+8+6+20+16+8))
        for ProductId, Pname, Description, Category, Dtype, Price, Qty, State in mydata:
            print("| %6s | %20s | %40s | %15s | %10s | %8s | %6s | %20s |"%(ProductId, Pname, Description, Category, Dtype, str(Price), str(Qty), State))
        print('-'*(6+20+40+15+10+8+6+20+16+8))
    except:
        print("Unexpected Error! Sorry for Inconvinience.")
    
def ViewProductReview():
  try:
     ProductId = input("Enter Product ID: ")
     q55="SELECT * FROM REVIEWS WHERE ProductId = '%s'"%ProductId
     csr.execute(q55)
     rev=csr.fetchall()
     print('%6s | %6s | %6s | %3s | %22s |'%('UID', 'PID', 'OID', 'Rt', 'Review'))
     if rev:
        for UserId, ProductId, OrderId, Rating, Review in rev:
            print('%6s | %6s | %6s | %3s | %22s |'%(UserId, ProductId, OrderId, Rating, Review))
     else:
        print("No reviews found.")

  except:
    print("Sorry! we could not find reviews for this product")


# Shopping Cart


def AddShoppingCart():
    UserId=input('Enter User Id: ')
    MOP=input("Enter Method of payment")
    while True:
        try:
            ProductId=input('Enter Product Id: ')
            q35="SELECT Qty,Price from PRODUCTS WHERE ProductId='%s' " % ProductId
            csr.execute(q35)
            pqty=csr.fetchone()
            PPrice=pqty[1]
            print("Available Quantity: ",pqty[0] )
            Qty= int(input("Enter Quantity: "))
            if Qty>pqty[0]:
                print("Not Enough Stock! Add Grievance for same")
                continue
            else:
                TPrice= PPrice*Qty
                print("Total Price: ", TPrice)
                q8="INSERT INTO SHOPPINGCART values('%s','%s',%s,%s,%s,'%s')"%(UserId, ProductId, PPrice, Qty, TPrice,MOP)
                csr.execute(q8)
                mydb.commit()
                opt=input("More?(Y/N): ")
                if opt in ['N','n']:
                    break
        except:
            print("Sorry we could not process that!")
def UpdateShoppingCart():
    UId=input("Enter UserId: ")
    ch=input("What would you like to update(Qty, MOP)")
    if ch=='Qty':
        try:
            PId=input("Enter Product Id: ")
            q36="SELECT Qty,Price from PRODUCTS WHERE ProductId='%s' " % PId
            csr.execute(q36)
            pqty=csr.fetchone()
            print("Available Quantity: ",pqty[0] )
            newval=int(input("Enter updated value: "))
            if newval>pqty[0]:
                print("Not Enough Stock! Add Grievance for same")
            else:
                Nprice=pqty[1]*newval
                print("Updated Price:",Nprice )
                q9="UPDATE SHOPPINGCART SET QTY=%s,TPRICE=%s WHERE ProductId='%s'and UserId='%s'"%(newval, Nprice,PId, UId)
        except:
            print("Unexpected Error!")
    elif ch=='MOP':
        nval=input("Enter updated value: ")
        q9="UPDATE SHOPPINGCART SET MOP= '%s' WHERE UserId= '%s'"%(nval,UId)
    try:
        csr.execute(q9)
        mydb.commit()
    except:
        print("Error!!")
def DeleteShoppingCart():
    try:
        UserId=input("Enter User Id: ")
        while True:
            ProductId=input('Enter Product Id: ')
            q16= "DELETE FROM SHOPPINGCART WHERE ProductId='%s' and UserId='%s'" %(ProductId,UserId)
            csr.execute(q16)
            mydb.commit()
            opt=input("More?(Y/N)")
            if opt in ['N', 'n']:
                break

    except:
        print("Error!!")
def ShowShoppingCart():
    try:
        UserId=input('Enter User Id: ')
        q17="SELECT * FROM SHOPPINGCART WHERE UserId= '%s' "%UserId
        csr.execute(q17)
        scart=csr.fetchall()
        print("| %6s | %6s | %8s | %6s | %12s | %15s |" %("UId", "PId", "PPrice", "Qty", "TPrice","MOP"))
        print('-'* 80)
        for UserId, ProductId, PPrice, Qty, TPrice,MOP in scart:
            print("| %6s | %6s| %8s | %6s | %12s | %15s |" % (UserId, ProductId, str(PPrice), str(Qty), str(TPrice) ,MOP))
        print('-'* 80)
    except:
        print("Error in viewing Shopping Cart!!")

def GenerateBill():
    try:
        UserId = input("Enter your User ID: ")
        q18 = "SELECT SUM(TPrice) FROM SHOPPINGCART WHERE UserId = '%s'"%(UserId)
        csr.execute(q18)
        total = csr.fetchone()
        if total:
            print("Total Bill Amount:", total[0])
        else:
            print("No items in the shopping cart.")
    except:
        print("Error")

#Orders

def Checkout():
    global Orderno
    print("--------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------")
    print("THIS WILL DELETE YOUR SHOPPING CART AND WILL ADD YOUR ITEMS TO YOUR ORDERS")
    print("--------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------")
    try:
        q45='SELECT Ordernum from ORDERNO'
        csr.execute(q45)
        Order=csr.fetchone()
        if Order is None:
            q44='INSERT INTO ORDERNO values(0)'
            csr.execute(q44)
            mydb.commit()
        else:
            q44='UPDATE ORDERNO SET Ordernum= Ordernum+1'
            csr.execute(q44)
            mydb.commit()
        q45='SELECT Ordernum from ORDERNO'
        csr.execute(q45)
        Order=csr.fetchone()
        for i in Order:
            Orderno=i

        UserId=input("Enter UserId : ")
        OrderId='O'+'0'*(4-len(str(Orderno))) + str(Orderno)
        q39="SELECT ProductId, TPrice,Qty from SHOPPINGCART WHERE UserId= '%s'"%(UserId)
        csr.execute(q39)
        products=csr.fetchall()
        ProductIds=''
        TotalCost=0
        for ProductId,Pprice,Qty in products:
            q41="Update PRODUCTS SET Qty= Qty - %s where ProductId= '%s'"%(Qty, ProductId)
            csr.execute(q41)
            ProductIds+=ProductId+ ' '
            TotalCost+=Pprice
        Odate=input("Enter Date of Placing Order in Format(YYYY-MM-DD): ")
        Ddate=input("Enter Date of Delivery in Format(YYYY-MM-DD): ")
        q5="INSERT INTO ORDERS values('%s','%s','%s',%s,'%s','%s')"%(OrderId, UserId,ProductIds, TotalCost, Odate, Ddate)
        csr.execute(q5)
        q40="DELETE FROM SHOPPINGCART WHERE UserId= '%s'"%(UserId)
        csr.execute(q40)
        mydb.commit()
        print("Your Order has been placed!!")
        print()
        print()
        print('*'*12)
        print('Order ID: ', OrderId)
        print('*'*12)
        print()
        print()
    except:
        print("Error occured while placing your order")




def UpdateOrders():
    try:
        OId=input("Enter Order Id: ")
        ch=input("What would you like to update (UserId, Odate,Ddate): ")
        nval=input("Enter Updated Value: ")
        q6="UPDATE ORDERS SET %s ='%s' WHERE OrderId='%s' " %(ch, nval,OId)
        csr.execute(q6)
        mydb.commit()
        print("Updated Successfully")
    except:
        print("Error Updating Order! ")
def DeleteOrders():
    try:
        OId=input("Enter the Order Id to be deleted: ")
        q7="Delete from ORDERS WHERE OrderId= '%s'"%OId
        csr.execute(q7)
        mydb.commit()
    except:
        print("Error")
def ShowAllOrders():
    try:
        csr.execute("Select * from ORDERS")
        mydata=csr.fetchall()
        print("|%8s|%6s|%25s|%12s|%12s|%12s|" % ('OId', 'UId', 'PIds', 'TotalCost', 'Odate', 'Ddate'))
        print('-' * 150)
        for OrderId, UserId,ProductIds, TotalCost, Odate, Ddate in mydata:
            print("|%6s | %6s | %25s | %12s | %12s |%12s|"%(OrderId, UserId,ProductIds, str(TotalCost), str(Odate), str(Ddate)))
        print('-'*150)
    except:
        print("Error")
def ShowSpecificOrders():
    try:
        SUId=input('Enter UserId: ')
        q14="Select * from ORDERS where UserId= '%s'"%SUId
        csr.execute(q14)
        mydata=csr.fetchall()
        print("|%6s | %6s | %25s | %12s | %12s | %12s|"%("OId", "UId","PIds", "TotalCost", "Odate", "Ddate"))
        print('-'*80)
        for OrderId, UserId,ProductIds, TotalCost, Odate, Ddate in mydata:
            print("|%6s | %6s | %25s | %12s | %12s |%12s|"%(OrderId, UserId,ProductIds, str(TotalCost), str(Odate), str(Ddate)))
        print('-'*80)
    except:
        print("Error")


#Reviews

def AddReviews():
    try:
        UserId = input("Enter your User ID: ")
        ProductId = input("Enter Product ID: ")
        OrderId = input("Enter Order ID: ")
        Rating = int(input("Enter Rating (1-5): "))
        Review = input("Enter your review: ")
        q19 = "INSERT INTO REVIEWS (UserId, ProductId, OrderId, Rating, Review) VALUES ('%s', '%s', '%s', %s, '%s')"%(UserId, ProductId, OrderId, Rating, Review)
        csr.execute(q19)
        mydb.commit()
        print("Review added successfully.")
    except:
        print("Error")
#Display options for 1)seeing both Product and User description 2) Seeing only review for specific product 3)Reviews from specificUser 4) Review of Product with specific rating

def DeleteReview():
    try:
        UserId = input("Enter your User ID: ")
        ProductId = input("Enter Product ID to delete review for: ")
        q29 = "DELETE FROM REVIEWS WHERE UserId = '%s' AND ProductId = '%s'"%(UserId, ProductId)
        csr.execute(q29)
        mydb.commit()
        print("Review deleted.")
    except:
        print("Error deleting review")

def ViewReviews():
    try:
        option = input('''Enter A number
                          1) See Product and User description
                          2) Reviews for specific product
                          3) Reviews from specific user
                          4) Reviews with specific rating
                          Choose an option: ''')
        if option == '1':
            q50='SELECT ProductId,Pname,Rating from PRODUCTS NATURAL JOIN REVIEWS'
            csr.execute(q50)
            record1= csr.fetchall()
            q51='SELECT ProductId, UserID, Name, Review from USERS NATURAL JOIN REVIEWS'
            csr.execute(q51)
            record2=csr.fetchall()
            print('%6s | %30s | %6s | %20s | %2s | %22s |'%('UID', 'UserName', 'PID', 'Pname', 'Rt' , 'Review'))
            if record1:
                for i in record1:
                    for j in record2:
                        if i[0]==j[0]:
                            print('%6s | %30s | %6s | %20s | %2s | %22s |'%(j[1],j[2],i[0],i[1],str(i[2]),j[3]))
            else:
                print("No reviews found!")

        elif option == '2':
            ProductId = input("Enter Product ID: ")
            q20="SELECT * FROM REVIEWS WHERE ProductId = '%s'"%ProductId
            csr.execute(q20)
        elif option == '3':
            UserId = input("Enter User ID: ")
            q21= "SELECT * FROM REVIEWS WHERE UserId ='%s'"%UserId
            csr.execute(q21)
        elif option == '4':
            Rating = int(input("Enter Rating: "))
            q22= "SELECT * FROM REVIEWS WHERE Rating = %s"%Rating
            csr.execute(q22)
        else:
            print("Invalid option.")
            print("Error")
        if option != '1':
            reviews = csr.fetchall()
            print('%6s | %6s | %6s | %3s | %22s |'%('UID', 'PID', 'OID', 'Rt', 'Review'))
            if reviews:
                for UserId, ProductId, OrderId, Rating, Review in reviews:
                    print('%6s | %6s | %6s | %3s | %22s |'%(UserId, ProductId, OrderId, Rating, Review))
            else:
                print("No reviews found.")
    except:
        print("Error viewing reviews:")
def UpdateReview():
    try:
        UserId = input("Enter your User ID: ")
        ProductId = input("Enter Product ID to update review for: ")
        Rating = int(input("Enter new Rating (1-5): "))
        Review = input("Enter new review: ")
        q23 = "UPDATE REVIEWS SET Rating = %s, Review = '%s' WHERE UserId = '%s' AND ProductId = '%s'"%(Rating, Review, UserId, ProductId)
        csr.execute(q23)
        mydb.commit()
        print("Review updated.")
    except:
        print("Error")


#Grievences

def AddGrievances():
    try:
        UserId = input("Enter your User ID: ")
        OrderId = input("Enter Order ID: ")
        Tgrieve = input("Enter your grievance title: ")
        Sgrieve = input("Enter your grievance description: ")
        q24 = "INSERT INTO GRIEVANCES (UserId, OrderId, Tgrieve, Sgrieve) VALUES ('%s', '%s', '%s', '%s')"%(UserId, OrderId, Tgrieve, Sgrieve)
        csr.execute(q24 )
        mydb.commit()
        print("Grievance submitted successfully.")
    except:
        print("Error submitting grievance")
def ViewGrievances():
    try:
        option = input('''1) View grievances by User ID
                          2) View grievances by Order ID
                          Choose an option: ''')
        if option == '1':
            UserId=input("Enter User ID: ")
            q25="SELECT * FROM GRIEVANCES WHERE UserId = '%s'"%UserId
            csr.execute(q25)
        elif option == '2':
            OrderId = input("Enter Order ID: ")
            q25="SELECT * FROM GRIEVANCES WHERE OrderId = '%s' " %OrderId
            csr.execute(q25)
        else:
            print("Invalid option.")


        grievances = csr.fetchall()
        if grievances:
            print("| %6s | %6s | %20s | %30s | %30s | " %('UserId', 'OrderId', 'Tgrieve', 'Sgrieve' , 'SolGrieve'))
            print('*'*126)
            for UserId, OrderId, Tgrieve, Sgrieve,SolGrieve in grievances:
                print("| %6s | %6s | %20s | %30s | %30s |"%(UserId, OrderId, Tgrieve, Sgrieve, SolGrieve))
            print('*'*126)
        else:
            print("No grievances found.")
    except:
        print("Error viewing grievances")
def ReplyGrievances():
     try:
        UserId = input("Enter User ID: ")
        OrderId = input("Enter Order ID: ")
        q54="SELECT Tgrieve,Sgrieve from GRIEVANCES WHERE UserId = '%s' AND OrderId = '%s'"%(UserId, OrderId)
        csr.execute(q54)
        gv=csr.fetchall()
        if gv:
          for i,j in gv:
            print('Grievance Title:', i)
            print('Grievance description: ',j)
            Solgrieve = input("Enter Reply to  grievance: ")
            q27 = "UPDATE GRIEVANCES SET SolGrieve = '%s' WHERE UserId = '%s' AND OrderId = '%s'"%(Solgrieve, UserId, OrderId)
            csr.execute(q27)
            mydb.commit()
            print("Grievance updated successfully.")
        else:
          print("No grievances found")
          
     except:
        print("Error updating grievance")

def UpdateGrievances():
    try:
        UserId = input("Enter your User ID: ")
        OrderId = input("Enter Order ID: ")
        Tgrieve = input("Enter updated grievance: ")
        Sgrieve=input("Enter Updted Grievance Description: ")
        q27 = "UPDATE GRIEVANCES SET Tgrieve = '%s',Sgrieve='%s' WHERE UserId = '%s' AND OrderId = '%s'"%(Tgrieve, Sgrieve, UserId, OrderId)
        csr.execute(q27)
        mydb.commit()
        print("Grievance updated successfully.")
    except:
        print("Error updating grievance")
def DeleteGrievances():
    try:
        UserId = input("Enter your User ID: ")
        OrderId = input("Enter Order ID to delete grievance for: ")
        q28 = "DELETE * FROM GRIEVANCES WHERE UserId = '%s' AND OrderId ='%s'"%(UserId, OrderId)
        csr.execute(q28)
        mydb.commit()
        print("Grievance deleted successfully.")
    except:
        print("Error deleting grievance")


#MAIN CODE

print('*'*200)
CreateTables()
while True:
  print("*"*500)
  print("LOGIN PAGE")
  print("*"*500)
  Tlogin=input('''Enter Your Domain For Logging In:
                    A. Admin
                    B. User
                    C. Close the Program (Enter C): ''')
  if Tlogin.lower()=='admin':
        val=AdmnLogin()
        if val:
            Dlogin='admin'
            print('Logged in Successfully!')
        elif not val:
            opt=input("Would You like to Register?(Y/N) ")
            if opt in ['Y','y']:
                AddAdmin()
                print("You Have Registered Successfully")
                Dlogin='admin'
            else:
                break

  elif Tlogin.lower()=='user':
        val= LoginUser()
        if val:
            Dlogin= 'user'
            print('Logged in Successfully!')
        elif not val:
            opt=input("Would You like to Register?(Y/N) ")
            if opt in ['Y','y']:
                RegisterUser()
                print("You Have Registered Successfully")
                Dlogin= 'user'
  elif Tlogin.lower()=='c':
      print("Closing the Program")
      break
  else:
        print('Invalid input. ')
        continue

  while True:
    print()
    print()
    print()
    print()
    print()
    choice= int(input('''Enter the number to choose an Domain(Enter Number):
                               1.Admin and Users
                               2.Products
                               3.Shopping Cart
                               4. Orders
                               5.Reviews
                               6.Grievances
                               7.Return to Login Page: '''))
    print()
    print()
    print()
    print()
    print()

    if choice==1:
            print("*"*500)
            print("ADMIN and USER Page")
            print("*"*500)
            if Dlogin=='admin':
                c1= input('''Choose operation (Enter Alphabet):
                              A.Display All Admin Credentials
                              B.Show All Users
                              C.Show Users by State
                              D.Add Admin:  ''')
                if c1.lower()=='a':
                    ShowAdmn()
                    continue
                elif c1.lower()=='b':
                    ShowAllUsers()
                    continue
                elif c1.lower()=='c':
                    ShowUsersByState()
                    continue
                elif c1.lower()=='d':
                    while True:
                        AddAdmin()
                        m=input("Enter More:(Y/N) ")
                        if m in ['N','n']:
                            break
                    continue
                else:
                    print('Invalid Option')
                    continue
            else:
                print("This option is restricted for Admin.")
                continue
    elif choice==2:
            print("*"*500)
            print("PRODUCT PAGE")
            print("*"*500)
            if Dlogin=='admin':
                c= input('''Choose operation (Enter Alphabet):
                              A. Add Products
                              B. Update Products
                              C. Delete Products
                              D. Show All Products''')
                if c.lower()=='a':
                    while True:
                        AddProduct()
                        m=input("Enter More:(Y/N) ")
                        if m in ['N','n']:
                            break
                    continue
                elif c.lower()=='b':
                    UpdateProduct()
                    continue
                elif c.lower()=='c':
                    DeleteProduct()
                elif c.lower()=='d':
                    ShowAllProduct()
                else:
                    print('Invalid Option')
            else:
                c= input('''Choose operation (Enter Alphabet):
                              A. Show All Products
                              B. View Specific Products
                              C. View reviews for specific order
                              D. View Sorted Products''')
                if c.lower()=='a':
                    ShowAllProduct()
                elif c.lower()=='b':
                    ViewSelectedProduts()
                elif c.lower()=='c':
                    ViewProductReview()
                elif c.lower()=='d':
                    ProductSort()
                else:
                    print('Invalid Option')
    elif choice==4:
            print("*"*500)
            print("ORDERS PAGE")
            print("*"*500)
            if Dlogin=='admin':
                c= input('''Choose operation (Enter Alphabet):
                              A. Show All Orders
                              B. Update Orders
                              C. Show Orders by Specific User:''')
                if c.lower()=='a':
                    ShowAllOrders()
                elif c.lower()=='b':
                    UpdateOrders()
                elif c.lower()=='c':
                    ShowSpecificOrders()
                else:
                    print('Invalid Option')
            else:
                c= input('''Choose operation (Enter Alphabet):
                              A. Checkout
                              B. Delete Orders
                              C. View Orders by Specific User: ''')
                if c.lower()=='a':
                    Checkout()
                elif c.lower()=='b':
                    DeleteOrders()
                elif c.lower()=='c':
                    ShowSpecificOrders()
                else:
                    print('Invalid Option')
    elif choice==3:
            print("*"*500)
            print("SHOPPING CART")
            print("*"*500)
            if Dlogin=='admin':
                c= input('''Choose operation (Enter Alphabet):
                              A. Show Shopping Cart: ''')
                if c.lower()=='a':
                    ShowShoppingCart()
                else:
                    print('Invalid Option')
            else:
                c= input('''Choose operation(Enter Alphabet):
                              A. Add products to Shopping cart
                              B. Update the Shopping Cart
                              C. Delete from Shopping Cart
                              D.Show the Shopping Cart
                              E.Generate Bill: ''')
                if c.lower()=='a':
                    AddShoppingCart()
                elif c.lower()=='b':
                    UpdateShoppingCart()
                elif c.lower()=='c':
                    DeleteShoppingCart()
                elif c.lower()=='d':
                    ShowShoppingCart()
                elif c.lower()=='e':
                    GenerateBill()
                else:
                    print('Invalid Option')

    elif choice==5:
            print("*"*500)
            print("REVIEWS")
            print("*"*500)
            if Dlogin=='admin':
                c= input('''Choose operation:
                              A. View Reviews: ''')
                if c.lower()=='a':
                    ViewReviews()
                else:
                    print('Invalid Option')
            else:
                c= input('''Choose operation (Enter Alphabet):
                              A. Add Reviews
                              B. Update Reviews
                              C. Delete Reviews: ''')
                if c.lower()=='a':
                    AddReviews()
                elif c.lower()=='b':
                    UpdateReview()
                elif c.lower()=='c':
                    DeleteReview()
                else:
                    print('Invalid Option')
    elif choice==6:
            print("*"*500)
            print("GRIEVANCES")
            print("*"*500)
            if Dlogin=='admin':
                c= input('''Choose operation (Enter Alphabet):
                              A. View Grievances:
                              B. Reply Grievances''')
                if c.lower()=='a':
                    ViewGrievances()
                elif c.lower()=='b':
                    ReplyGrievances()
                else:
                    print('Invalid Option')
            else:
                c= input('''Choose operation (Enter Alphabet):
                              A. Add Grievances
                              B. Update Grievances
                              C. Delete Grievances
                              D. View Grievances:  ''')
                if c.lower()=='a':
                    AddGrievances()
                elif c.lower()=='b':
                    UpdateGrievances()
                elif c.lower()=='c':
                    DeleteGrievances()
                elif c.lower()=='d':
                    ViewGrievances()
                else:
                    print('Invalid Option')
    elif choice==7:
        break
