import mysql.connector

# ********************************************

# connection = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "mydatabase" 
# )

# cursor = connection.cursor()

#  mycursor.execute("CREATE DATABASE mydatabase")

# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), adress VARCHAR(255))")

# ********************************************


# ******************** Def ************************

# Single insert

# def insertProduct():
#     while True:
#         name = input("Name: ")
#         price = float(input("Price: "))
#         image = input("Image: ")
#         description = input("Description: ")

#         connection = mysql.connector.connect(
#             host = "localhost",
#             user = "root",
#             password = "",
#             database = "mydatabase" 
#         )

#         cursor = connection.cursor()

#         insert_sql = "INSERT INTO products(Name, Price, Image, Description) VALUES (%s, %s, %s, %s)"
#         values = (name, price, image, description)
#         cursor.execute(insert_sql,values)

#         try:
#             connection.commit()
#             print(f"{ cursor.rowcount } Added")
#             print(f"ID of the last added: {cursor.lastrowid}")
#         except mysql.connector.Error as err:
#             print("Error",err)
#         finally:
#             connection.close()
#             print("Database Connection Closed")
#             result = input("Do you wanna continue? (y/n): ")
#             if result == 'n':
#                 break


# List insert

def insertProducts(List):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mydatabase" 
    )

    cursor = connection.cursor()

    insert_sql = "INSERT INTO products(Name, Price, Image, Description) VALUES (%s, %s, %s, %s)"
    values = List
    cursor.executemany(insert_sql,values)

    
    try:
        connection.commit()
        print(f"{ cursor.rowcount } Added")
        print(f"ID of the last added: { cursor.lastrowid }")
    except mysql.connector.Error as err:
        print("Error",err)
    finally:
        connection.close()
        print("Database Connection Closed")
        
def getProducts():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mydatabase" 
    )

    cursor = connection.cursor()

    getProductsInfo()
    
    cursor.execute("Select * From products Where Price > 500 and name LIKE '%iphone%' ")

    try:
        result = cursor.fetchall()
        for i in result:
            print(f"Name: {i[1]} Price: {i[2]}")
    except mysql.connector.Error as err:
        print("Error", err)
    finally:
        connection.close()
        print("Closed")

def getProductsInfo():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "mydatabase" 
    )

    cursor = connection.cursor()

    # cursor.execute("Select COUNT(*) from products")
    # cursor.execute("Select AVG(Price) from products")
    # cursor.execute("Select SUM(Price) from products")
    cursor.execute("Select Name from products where Price = (Select MAX(Price) from products)")
 
    product_count = cursor.fetchone()
    print(f"Result: {product_count[0]}")


# ********************** Main ****************************

# insertProduct()

# List = []
# while True:
#     name = input("Name: ")
#     price = float(input("Price: "))
#     image = input("Image: ")
#     description = input("Description: ")

#     List.append((name, price, image, description))
#     result = input("Do you wanna continue? (y/n): ")
#     if result == 'n':
#         print(List)
#         insertProducts(List)
#         break

getProducts()