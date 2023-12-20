import mysql.connector
import mysql

#database connection
db=mysql.connector.connect(user="root",host="localhost",passwd="root123",auth_plugin="mysql_native_password",database="expense") 
mycursor=db.cursor()
main_sql="SET SQL_SAFE_UPDATES=0" 
mycursor.execute(main_sql) 
db.commit() 

#decorator for the function
def dec(func):
    def wrapee():
        print("-------------------------------") 
        func() 
        print("---------------------")
        print("*********************")
    return wrapee

@dec
def add_user():
    cursor=db.cursor()
    a=input("reason for buying:") 
    b=input("price:")
    c=input("product name:") 
    e=input("gateway (online/offline): ") 
    f=input("from where: ")
    #using r strip to remove the space when given 
    reason_for_buying=a.rstrip()
    price=b.rstrip()
    product_name=c.rstrip() 
    method=e.rstrip() 
    venue=f.rstrip()
    sql="INSERT INTO tech_expense(reason_for_buying,price,product_name,method,venue) VALUES(%s,%s,%s,%s,%s)"
    data=(reason_for_buying,price,product_name,method,venue)
    cursor.execute(sql,data)
    db.commit()
    print(cursor.rowcount ,"added successfully! :)")  

def database_():
    sql_select_Query = "SELECT * FROM tech_expense"
    cursor = db.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    
    
    for row in records:
        print("Total number of rows in table: ", cursor.rowcount,"\n")
        print("reason for buying = ", row[0], )
        print("price = ", row[1])
        print("product_name = ", row[2])
        print("method = ", row[3])
        print("venue= ",row[4])


def search_():
    mycursor = db.cursor()

    sql = "SELECT * FROM tech_expense WHERE product_name = %s"
    req=input("product name to be searched: ")
    adr = (req,)

    mycursor.execute(sql, adr)

    myresult = mycursor.fetchall()

    for row in myresult:
        print("reason for buying = ", row[0], )
        print("price = ", row[1])
        print("product_name = ", row[2])
        print("method = ", row[3])
        print("venue= ",row[4])


while True:
    try:
        print('''
                  menu 
                  1) to add product
                  2) show the list of products
                  3)  to search for a product from database 
                  4) exit..
        ''')
        ch=int(input("enter your choice:"))
        #1st code 
        if ch==1:    
          req=input("enter yes to add input:") 
          add_input = req.rstrip() 
          if add_input == "yes":
              add_user() 
              continue
          if add_input =="no":
              print("thank you") 
              break
          else:
              print("enter a valid input!") 
              continue 
        #2nd code 
        if ch==2:
            print("the records are:","\n")
            database_()
        if ch==3:
            search_()
        if ch==4:
            break  
    except EOFError:
        print("our server is quiet busy , pleease try again later :( ") 