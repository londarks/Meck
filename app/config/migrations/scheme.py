import psycopg2

con = psycopg2.connect(host='127.0.0.1',dbname='metronic_db' ,user='postgres',password='3167582')
cur = con.cursor()

#con.autocommit = True
  
# Creating a cursor object
#cursor = con.cursor()
  
# query to create a database 
# sql = ''' CREATE database Metronic_DB ''';
# cursor.execute(sql)

#CREATE TABELA
# sql = 'create table usuarios (id serial primary key, username varchar(100), email varchar(100), password varchar(100), space serial, create_date serial, acess serial )'
# cur.execute(sql)
# con.commit()


#CREATE
#await db.execute(f"INSERT INTO {data['STRG']} VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", dados)
dados = ('londarks','admin@gmail.com','aaee2e0160833193f4be0cca47d42246dc31887f185730cd7803e9f6b5cbc7bb',50,1658715855,3)
query =  """ INSERT INTO usuarios (username, email, password,space,create_date,acess) VALUES (%s,%s,%s,%s,%s,%s)"""
cur.execute(query, dados)
con.commit()


#UPDATE
# query = """Update usuarios set ovos = 10 where name ='londarks'"""
# cur.execute(query)
# con.commit()

#DELET
# query = """delete from usuarios where name ='Meck'"""
# cur.execute(query)
# con.commit()


# cur.execute('select * from usuarios')
# recset = cur.fetchall()
# for rec in recset:
#     print (rec)
# con.close()


#READ
# cur.execute('select * from usuarios')
# recset = cur.fetchall()
# for rec in recset:
#     print (rec)
# con.close()


con.close()