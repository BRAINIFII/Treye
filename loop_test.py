from tkinter import *
import psycopg2
import time

root = Tk()

l = Listbox(root)

# auto Entry
try:
    connection = psycopg2.connect(user = "postgres",
                                password = "mr5tr4n63",
                                host = "127.0.0.1",
                                port = "5432",
                                database = "Treye_data")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM data")
    connection.commit()
    numrows = int(cursor.rowcount)
    for x in range(0,numrows):
        row = cursor.fetchone()
        print (row[1])
        l.insert(END, row[1])
        time.sleep(1)
    connection.commit()

except (Exception, psycopg2.DatabaseError) as error :
    print ("Treye Module Error:Error while creating PostgreSQL table", error)



l.pack()

root.mainloop()