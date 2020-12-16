import psycopg2

#Connecting to database
conn = psycopg2.connect(database="test_aut",user="sundarb",password="P7BrSBgxVfuYz4ZB",host="localhost",port=5433)
print("Database connected Successfully")

#Create a table
cur = conn.cursor();
# cur.execute('''CREATE TABLE STUDENT 
#     (ADMISSION INT PRIMARY KEY NOT NULL,
#     NAME TEXT NOT NULL,
#     AGE INT NOT NULL,
#     COURSE CHAR(50),
#     DEPARTMENT CHAR(50));''')
# print('Table created successfully')
# # conn.commit()
# # conn.close()

# # Inserting data to database
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (34550,'sundarb',18,'CS','ICT')");
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3419, 'Abel', 17, 'Computer Science', 'ICT')");
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')");
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')");
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')");
# print('Data inserted Successfully')

# Reteriving data
# cur.execute("SELECT admission, name, age, course, department from STUDENT")
# rows = cur.fetchall();
# for row in rows:
#     print("ADMISSION =", row[0])
#     print("NAME =", row[1])
#     print("AGE =", row[2])
#     print("COURSE =", row[3])
#     print("DEPARTMENT =", row[4], "\n")
# print('Operation successfull')

cur.execute("SELECT * from test_de")
rows1 = cur.fetchall()
for row in rows1:
    print("ITEM ID:", row[1])
    print("ITEM Desc:", row[2])
    print("ITEM Locator:", row[3])
    


conn.commit()
conn.close()

