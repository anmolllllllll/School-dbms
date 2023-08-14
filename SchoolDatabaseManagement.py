import mysql.connector
print("___________________________________WELCOME___________________________________")
loginfo={1118 : 10062002, 2342 : 21072002}
c=0
print("Please log in to continue")
chance=1
num=1
while 5>=chance>=1:
    if num==1:
        username=int(input("ENTER YOUR USERNAME: "))
        passwd=int(input("ENTER YOUR PASSWORD: "))
        for name in loginfo:
            if name==username:
                if loginfo[name]==passwd:
                    chance=0
                    print("")
                    print("")
                    print("Successfully Logged In")
                    rep=1
                    while rep>0:
            
                        def createdatabase():
                            try:
                                db=mysql.connector.connect(user='root',password='mysql',host='localhost')
                                cursor=db.cursor()
                                cursor.execute("create database mysql;")
                                
                            except:
                                print("Database already exist")
                                selection()
                        def selection():
                            db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                            cursor = db.cursor()
                            print('-----------------------------------\nWELCOME TO SCHOOL MANAGEMENT SYSTEM\n-----------------------------------')
                            print("1.STUDENT MANAGEMENT")
                            print("2.EMPLOYEE MANAGEMENT")
                            print("3.FEE MANAGEMENT")
                            print("4.EXAM MANAGEMENT")
                            ch=int(input("\nEnter ur choice (1-4) : "))
                            if ch==1:
                                print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
                                print('a.NEW ADMISSION')
                                print('b.UPDATE STUDENT DETAILS')
                                print('c.ISSUE TC')
                                c=input("Enter ur choice (a-c) : ")
                                print('\nInitially the details are..\n')
                                display1()
                                if c=='a':
                                    insert1()
                                    print('\nModified details are..\n')
                                    display1()
                                elif c=='b':
                                    update1()
                                    print('\nModified details are..\n')
                                    display1()
                                elif c=='c':
                                    delete1()
                                    print('\nModified details are..\n')
                                    display1()
                                else:
                                    print('Enter correct choice...!!')
                            elif ch==2:
                                print('WELCOME TO EMPLOYEE MANAGEMENT SYSTEM')
                                print('a.NEW EMPLOYEE')
                                print('b.UPDATE STAFF DETAILS')
                                print('c.DELETE EMPLOYEE')
                                c=input("Enter ur choice : ")
                                
                                if c=='a':
                                    insert2()

                                    print('\nModified details are..\n')
                                    display2()
                                elif c=='b':
                                    update2()
                                    print('\nModified details are..\n')
                                    display2()
                                elif c=='c':
                                    delete2()
                                    print('\nModified details are..\n')
                                    display2()
                                else:
                                    print('Enter correct choice...!!')
                            
                            elif ch==3:
                                print('WELCOME TO FEE MANAGEMENT SYSTEM')
                                print('a.NEW FEE')
                                print('b.UPDATE FEE')
                                print('c.EXEMPT FEE')
                                c=input("Enter ur choice : ")
                            
                                if c=='a':
                                    insert3()
                                elif c=='b':
                                    update3()
                                elif c=='c':
                                    delete3()
                                else:
                                    print('Enter correct choice...!!')
                            
                            elif ch==4:
                                print('WELCOME TO EXAM MANAGEMENT SYSTEM')
                                print('a.EXAM DETAILS')
                                print('b.UPDATE DETAILS ')
                                print('c.DELETE DETAILS')
                                c=input("Enter ur choice : ")
                            
                                if c=='a':
                                    insert4()
                                elif c=='b':
                                    update4()
                                elif c=='c':
                                    delete4()
                                else:
                                    print('Enter correct choice...!!')
                            else:
                                print('Enter correct choice...!!')
                            
                        def insert1():
                            sname=input("Enter Student Name : ")
                            admno=int(input("Enter Admission No : "))
                            admnos=str(admno)
                            dob=input("Enter Date of Birth(yyyy-mm-dd): ")
                            cls=input("Enter class for admission: ")
                            cty=input("Enter City : ")
                            db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                            cursor = db.cursor()
                            z="create table student(sname char(50),admno int,dob char(20),cls varchar(5),cty char(10));"
                            sql="INSERT INTO student VALUES ("+"'"+sname+"'"+","+admnos+","+"'"+dob+"'"+","+cls+","+"'"+cty+"'"+");"
                            try:
                                cursor.execute(z) 
                                cursor.execute(sql)
                                db.commit()
                            except:
                                db.rollback()
                                db.close()
                        #insert()
                        def display1():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM student"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    sname = c[0]
                                    admno= c[1]
                                    dob=c[2]
                                    cls=c[3]
                                    cty=c[4]
                                    print ("(sname="+sname+",admno="+admno+",dob="+dob+",cls="+cls+",cty="+cty+")")
                            except:
                                print ("Error: unable to fetch data")
                                db.close()
                        def update1():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM student"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    sname = c[0]
                                    admno= c[1]
                                    dob=c[2]
                                    cls=c[3]
                                    cty=c[4]
                            except:
                                print ("Error: unable to fetch data")
                                
                            try:
                                tempst=int(input("Enter Admission No : "))
                                temp=input("Enter new class : ")
                                sql = "Update student set cls="+temp+"where admno="+str(tempst)+";"
                                cursor.execute(sql)
                                sql1= "SELECT * FROM student"
                                cursor.execute(sql1)
                                db.commit()
                            except Exception as e:
                                print (e)

                                db.close()
                        def delete1():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM student"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    sname = c[0]
                                    admno= c[1]
                                    dob=c[2]
                                    cls=c[3]
                                    cty=c[4]
                            except:
                                print ("Error: unable to fetch data")
                                temp=int(input("\nEnter adm no to be deleted : "))
                            try:
                                sql = "delete from student where admno="+str(temp)
                                ans=input("Are you sure you want to delete the record(y/n) : ")
                                if ans=='y' or ans=='Y':
                                    cursor.execute(sql)
                                    db.commit()
                            except Exception as e:
                                print (e)
                                db.close()
                        def insert2():
                            ename=input("Enter Employee Name : ")
                            empno=int(input("Enter Employee No : "))
                            job=input("Enter Designation: ")
                            hiredate=input("Enter date of joining: ")
                            db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                            cursor = db.cursor()
                            z="create table emp(ename char(20),empno int,job char(50),hiredate date)"
                            sql="INSERT INTO emp VALUES("+ename+","+empno+","+job+","+hiredate+")"
                            try:
                                try:
                                    cursor.execute(sql)
                                    db.commit()
                                except:
                                    cursor.execute(z) 
                                    cursor.execute(sql)
                                    db.commit()
                            except:
                                db.rollback()
                                db.close()
                        def display2():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM emp"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    ename = c[0]
                                    empno= c[1]

                                job=c[2]
                                hiredate=c[3]
                                print ("(empno="+str(empno)+",ame="+ename+",job="+job+",hiredate="+str(hiredate)+")")
                            except:
                                print ("Error: unable to fetch data")
                                db.close()
                        def update2():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM emp"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    ename = c[0]
                                    empno= c[1]
                                    job=c[2]
                                    hiredate=c[3]
                            except:
                                print ("Error: unable to fetch data")
                                print()
                                tempst=int(input("Enter Employee No : "))
                                temp=input("Enter new designation : ")
                            try:
                                sql = "Update emp set job="+temp+"where empno="+"'"+str(tempst)+"'"
                                cursor.execute(sql)
                                db.commit()
                            except Exception as e:
                                print (e)
                                db.close()
                        def delete2():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM emp"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    ename = c[0]
                                    empno= c[1]
                                    job=c[2]
                                    hiredate=c[3]
                            except:
                                print ("Error: unable to fetch data")
                                temp=int(input("\nEnter emp no to be deleted : "))
                            try:
                                sql = "delete from emp where empno="+"'"+str(temp)+"'"
                                ans=input("Are you sure you want to delete the record(y/n) : ")
                                if ans=='y' or ans=='Y':
                                    cursor.execute(sql)

                                    db.commit()
                            except Exception as e:
                                print (e)
                                db.close()
                        def insert3():
                            admno=int(input("Enter adm no: "))
                            fee=float(input("Enter fee amount : "))
                            month=input("Enter Month: ")
                            db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                            cursor = db.cursor()
                            z="create table fee(admo int, fee int, month char(15));"
                            sql="INSERT INTO fee VALUES ("+str(admo)+","+str(fee)+","+month+")"
                            try:
                                cursor.execute(z)
                                cursor.execute(sql)
                                db.commit()
                            except:
                                db.rollback()
                                db.close()
                        def display3():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM fee"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    admno= c[0]
                                    fee=c[1]
                                    month=c[2]
                                    print ("(admno="+admo+",fee="+fee+",month="+month+")")
                            except:
                                print ("Error: unable to fetch data")
                                db.close()
                        def update3():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM fee"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    admno= c[0]
                                    fee=c[1]
                                    month=c[2]
                            except:
                                print ("Error: unable to fetch data")
                                print()
                                tempst=int(input("Enter Admission No : "))
                                temp=input("Enter new class : ")
                            try:
                                sql = "Update fee set month="+str(temp)+"where admno="+str(tempst)
                                cursor.execute(sql)

                                db.commit()
                            except Exception as e:
                                print (e)
                                db.close()
                        def delete3():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM fee"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    admno= c[0]
                                    fee=c[1]
                                    month=c[2]
                            except:
                                print ("Error: unable to fetch data")
                                temp=int(input("\nEnter adm no to be deleted : "))
                            try:
                                sql = "delete from student where admno="+str(temp)
                                ans=input("Are you sure you want to delete the record(y/n) : ")
                                if ans=='y' or ans=='Y':
                                    cursor.execute(sql)
                                    db.commit()
                            except Exception as e:
                                print (e)
                                db.close()
                        def insert4():
                            sname=input("Enter Student Name : ")
                            admno=int(input("Enter Admission No : "))
                            per=float(input("Enter percentage : "))
                            res=input("Enter result: ")
                            db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                            cursor = db.cursor()
                            z="create table exam(sname char(20),admno int,per int,res char(50));"
                            sql="INSERT INTO exam VALUES("+sname+","+admno+","+per+","+res+");"
                            try:
                                cursor.execute(z)
                                cursor.execute(sql)
                                db.commit()
                            except:
                                db.rollback()
                                db.close()
                        def display4():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM exam"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    sname = c[0]

                                    admno= c[1]
                                    dob=c[2]
                                    cls=c[3]
                                    cty=c[4]
                                    print(sname,admno,per,res)
                            except:
                                print ("Error: unable to fetch data")
                                db.close()
                        def update4():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM exam"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    sname = c[0]
                                    admno= c[1]
                                    dob=c[2]
                                    cls=c[3]
                                    cty=c[4]
                            except:
                                print ("Error: unable to fetch data")
                                print()
                                tempst=int(input("Enter Admission No : "))
                                temp=input("Enter new result : ")
                            try:
                                sql = "Update student set res="+temp+"where admno="+str(tempst) 
                                cursor.execute(sql)
                                db.commit()
                            except Exception as e:
                                print (e)
                                db.close()
                        def delete4():
                            try:
                                db = mysql.connector.connect(user='root', password='mysql', host='localhost',database='mysql')
                                cursor = db.cursor()
                                sql = "SELECT * FROM exam"
                                cursor.execute(sql)
                                results = cursor.fetchall()
                                for c in results:
                                    sname = c[0]
                                    admno= c[1]
                                    dob=c[2]
                                    cls=c[3]
                                    cty=c[4]
                            except:
                                print ("Error: unable to fetch data")

                                temp=int(input("\nEnter adm no to be deleted : "))
                            try:
                                sql = "delete from exam where admno="+str(temp)
                                ans=input("Are you sure you want to delete the record(y/n) : ")
                                if ans=='y' or ans=='Y':
                                    cursor.execute(sql)
                                    db.commit()
                            except Exception as e:
                                print (e)
                                db.close()
                        createdatabase()
                        selection()
                        ask=input("Do you want to run the program again ?(y/n)")
                        if ask=='y'or ask='Y':
                            rep=1
                        else:
                            rep=0
