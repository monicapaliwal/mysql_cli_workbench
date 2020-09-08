import mysql.connector

def connecToDB(dbname,passwrd):
    user='root'
    host='localhost'
    password=passwrd
    database=dbname

    conn=mysql.connector.connect(user=user,password=password,host=host,database=database)
    return conn

def SelectFromTable(conn,tablename,attribute):
    if len(attribute)==0:
        query="select * from "+tablename
    else:
        query="select "
        for i in range(len(attribute)):
            if i<(len(attribute)-1):
                query+=attribute[i]
                query+=','
            else:
                query+=attribute[i]
        query+=' from '+tablename

    cursr=conn.cursor()
    cursr.execute(query)
    result=cursr.fetchall()
    for i in result:
        print(i)

def Showdatabase(conn):
    query="show databases"
    cursr=conn.cursor()
    cursr.execute(query)
    result=cursr.fetchall()
    for i in result:
        print(i)

def Showtables(conn):
    query="show tables"
    cursr=conn.cursor()
    cursr.execute(query)
    result=cursr.fetchall()
    for i in result:
        print(i)

def DescribeTable(tablename):
    query="describe "+tablename
    cursr=conn.cursor()
    cursr.execute(query)
    result=cursr.fetchall()
    for i in result:
        print(i)

def DeleteFromTable(tablename,where,op):
    op= " "+op+" "
    list=[k+"='"+v+"'" for k,v in where.items()]
    op=op.join(list)
    print(op)
    query="delete from "+tablename+" where "+op
    print(query)
    cursr=conn.cursor()
    cursr.execute(query)
    print("The requirement is deleted!!")
    conn.commit()

def UpdateTable(tablename,where,op,setvalue):
    op= " "+op+" "
    list=[k+"='"+v+"'" for k,v in where.items()]
    op=op.join(list)
    print(op)

    list=[]
    set=" , "
    list=[k+"='"+v+"'" for k,v in setvalue.items()]
    set=set.join(list)
    query="update "+tablename+" set "+set+" where "+op
    print(query)
    cursr=conn.cursor()
    cursr.execute(query)
    print("The requirement is updated!!")
    conn.commit()

def InsertIntoTable(tablename,valuelist):
    query="Insert into "+tablename+" values ("
    for i in range(len(valuelist)):
        if i<(len(valuelist)-1):
            query+=valuelist[i]
            query+=','
        else:
            query+=valuelist[i]
    query+=")"
    print(query)
    cursr=conn.cursor()
    cursr.execute(query)
    print("The requirement is updated!!")
    conn.commit()


conn=connecToDB('library','1234')
Showdatabase(conn)

db=input("The above databases are present.Select the one that belongs to you:")
conn=connecToDB(db,'1234')

print("\nThe database contains the following tables:")
Showtables(conn)

table=input("Choose a table:")
DescribeTable(table)

ch=int(input("\nWhat do you wanna do?\n1)Insert value into some table:\n2)Select values from table:\n3)Delete from table:\n4)Update from table:\nMake a choice:"))


if ch==1:
    value=list()
    print("\nEnter the attributes uh want to enter:")
    while True:
        i=input()
        if i=='':
            break
        value.append(i)

    InsertIntoTable(table,value)
    SelectFromTable(conn,table,[])
if ch==2:
    attr=list()
    print("\nEnter the attributes uh want to print:")
    while True:
        i=input()
        if i=='':
            break
        attr.append(i)

    SelectFromTable(conn,table,attr)

if ch==3:
    where={}
    while True:
        i=input("Enter the entity name:")
        if i=='':
            break
        j=input("What value does it hold?")
        where.update({i:j})

    DeleteFromTable(table,where,'and')
    SelectFromTable(conn,table,[])

if ch==4:
    setvalue={}
    while True:
        i=input("Enter the set entity name:")
        if i=='':
            break
        j=input("What value does it hold?")
        setvalue.update({i:j})

    print("Enter the new values in order: ")
    where={}
    while True:
        i=input("Enter the entity name:")
        if i=='':
            break
        j=input("What value does it hold?")
        where.update({i:j})
    print("Enter the new values in order: ")


    UpdateTable(table,where,'and',setvalue)
    SelectFromTable(conn,table,[])
