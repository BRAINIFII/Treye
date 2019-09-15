from sqlite3 import *

database="Databases\data.db"
c = connect(database)
curval = c.cursor()
#curval.execute("DROP TABLE IF EXISTS Links")
#curval.execute("CREATE TABLE Links(Index_No number(3),Title varchar(1000),Link varchar(20),Price number(10))")
#curval.execute(" INSERT INTO Links VALUES(1,'Test1','esfesfsiofjsof',3242342)")
#curval.execute("INSERT INTO Links VALUES(2,'Test2','weWEwgrgzgegx',5646456)")
##curval.execute("INSERT INTO Links VALUES(3,'Test3','etshsehhtrsht',42542542)")
# curval.execute("select count(Index_No) from Links")
# a = curval.fetchall()
# curval.execute("select Title,Link from Links")
# c = curval.fetchall()
# print(pd.read_sql_query("select * from Links",c),"\n\n")
# #b = a[0]
