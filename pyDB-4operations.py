import mysql.connector as c
mydb = c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr"
)

mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE IF NOT EXISTS menu(item_no INT PRIMARY KEY,item_name VARCHAR(20),price INT,restaurant_name VARCHAR(40),location VARCHAR(30))')


item_no = input("Enter the item number: ")
item_name = input("Enter the item name: ")
price = int(input("Enter the price: "))
restaurant_name = input("Enter the restaurant name: ")
location = input("Enter the restaurant place: ")

mycursor.execute('INSERT INTO menu (item_no, item_name, price, restaurant_name, location) VALUES (%s, %s, %s, %s, %s)', (item_no, item_name, price, restaurant_name, location))
print("The new item has been added to the menu")
print("\n")

did = input("Enter the item number to be removed from the menu: ")
mycursor.execute('DELETE FROM menu WHERE item_no = %s', (did,))
print("Item is removed from the menu")
print("\n")

new_price = int(input("Enter the new price: "))
item_no = input("Enter the item number: ")
mycursor.execute('UPDATE menu SET price = %s WHERE item_no = %s', (new_price, item_no))
print("Price of the item is been updated")
print("\n")

print("Available menu:")
mycursor.execute("SELECT * FROM menu")
menu_list = mycursor.fetchall()
for item in menu_list:
    print(item)
print("\n")

mycursor.execute("SELECT * FROM menu ORDER BY item_name ASC")
menu_list_order = mycursor.fetchall()
print("List of the menu-items in the ascending order:")
for item in menu_list_order:
    print(item)
print("\n")

mycursor.execute("SELECT * FROM menu WHERE price BETWEEN 70 AND 90")
required_menu_list = mycursor.fetchall()
print("The items within the range(70/- to 90/-) are:")
for item in required_menu_list:
    print(item)
print("\n")

mycursor.execute('SELECT * FROM menu WHERE location = "Hyderabad"')
areas = mycursor.fetchall()
print("The restaurants details in Hyderabad are as follows:")
for item in areas:
    print(item)
print("\n")
mydb.commit()
