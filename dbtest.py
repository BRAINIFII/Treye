import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "mr5tr4n63",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "Treye_data")
    cursor = connection.cursor()
    
    # cursor.execute('''CREATE TABLE data
    #       (Index_No INT     NOT NULL,
    #        Title           VARCHAR(1000)    NOT NULL,
    #        Link          VARCHAR(100) NOT NULL,
    #        PRICE INT     NOT NULL); ''')
    # print("Database created")

    #cursor.execute("drop table mobile")
    
    cursor.execute("drop table data")
    print("Data Deleted")

    # numrows = int(cursor.rowcount)
    # print(numrows)

    # cursor.execute("SELECT Index_No FROM data ORDER BY Index_No DESC LIMIT 1")
    # i = cursor.fetchall()
    # print(i[0][0])

    
    # cursor.execute('''insert into data values(1,'erwgerherhera','rgaegearaerag',324324)''')
    # cursor.execute("delete from data where Index_No = 1")
    # cursor.execute("select * from data")
    # a = cursor.fetchall()
    # print(a)
    connection.commit()

except (Exception, psycopg2.DatabaseError) as error :
    print ("Treye Module Error:Error while creating PostgreSQL table", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("Treye:PostgreSQL connection is closed")