# 3.在python中输入:

    import cx_Oracle
    没有报错的话说明驱动安装成功。
# 4.数据库连接操作：

    conn = cx_Oracle.connect('xzt/xzt@localhost/testdb')#这里的顺序是用户名/密码@oracleserver的ip地址/数据库名字
        cur = conn.cursor()
        sql = "SELECT * FROM DUAL"
        cur.execute(sql)
        cur.close()
        conn.commit()
        conn.close()
# 5.数据库查询：
    import cx_Oracle  

    conn = cx_Oracle.connect('xzt/xzt@localhost/testdb')    
    cursor = conn.cursor ()  

    cursor.execute ("SELECT * FROM STUDENT_TB")  
    rows = cursor.fetchall() #得到所有数据集 
    for row in rows:  
        print("%d, %s, %s, %s" % (row[0], row[1], row[2], row[3]))#python3以上版本中print()要加括号用了

    print("Number of rows returned: %d" % cursor.rowcount)  

    cursor.execute ("SELECT * FROM STUDENT_TB")  
    while (True):  
        row = cursor.fetchone() #逐行得到数据集
        if row == None:  
            break  
        print("%d, %s, %s, %s" % (row[0], row[1], row[2], row[3])) 

    print("Number of rows returned: %d" % cursor.rowcount)

    cursor.close ()  
    conn.close () 
# 6.数据库插入：
    import cx_Oracle  

    conn = cx_Oracle.connect('xzp/xzp@localhost/testdb')    
    cursor = conn.cursor()  

    cursor.execute ("CREATE TABLE INSERTTEST(ID INT, C1 VARCHAR(50), C2 VARCHAR(50), C3 VARCHAR(50))")  

    cursor.execute ("INSERT INTO INSERTTEST (ID, COL1, COL2, COL3)VALUES(1213412, 'asdfa', 'ewewe', 'sfjgsfg')")  
    cursor.execute ("INSERT INTO INSERTTEST (ID, COL1, COL2, COL3)VALUES(12341, 'ashdfh', 'shhsdfh', 'sghs')")  
    cursor.execute ("INSERT INTO INSERTTEST (ID, COL1, COL2, COL3)VALUES(123451235, 'werwerw', 'asdfaf', 'awew')")  
    conn.commit() #这里一定要commit才行，要不然数据是不会插入的 

    cursor.close()  
    conn.close()
