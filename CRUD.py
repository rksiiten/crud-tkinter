import tkinter, pymysql                                     #import tkinter and pymysql to access their function
from tkinter.ttk import *                                   #import for ttk function
from tkinter import *                                       #import all from tkinter
from tkinter import messagebox                              #separate import of messagebox

root=Tk()                                                   #create widget
root.title("Student Data")                                  #title of widget show on top
root.geometry("800x600")                                    #size of widget
root.configure(bg='maroon')                                 #set widget background color

stnumL = Label(root, text="Student Number :",fg="white",bg="maroon")        #student number label
stnumL.place(x=190, y=60)                                                   #student number label location in widget
lnameL = Label(root, text="Last Name :",fg="white",bg="maroon")             #last name label
lnameL.place(x=190, y=90)                                                   #last name label location in widget
fnameL = Label(root, text="First Name :",fg="white",bg="maroon")            #first name label
fnameL.place(x=190, y=120)                                                  #first name label location in widget
mnameL = Label(root, text="Middle Name :",fg="white",bg="maroon")           #middle name name label
mnameL.place(x=190, y=150)                                                  #middle name label location in widget
bdayL = Label(root, text="Birthday :",fg="white",bg="maroon")               #birthday label
bdayL.place(x=190, y=180)                                                   #birthday label location in widget
ageL = Label(root, text="Age :",fg="white",bg="maroon")                     #age label
ageL.place(x=190, y=210)                                                    #age label location in widget
addressL = Label(root, text="Address :",fg="white",bg="maroon")             #address label
addressL.place(x=190, y=240)                                                #address label location in widget
idL = Label(root, text="id :",fg="white",bg="maroon")                       #id label
idL.place(x=190, y=350)                                                     #id label location in widget

stnumEntry = Entry(root)                                                    #student number entry
stnumEntry.place(x=350, y=60)                                               #student number entry location in widget
lnameEntry = Entry(root)                                                    #last name entry
lnameEntry.place(x=350, y=90)                                               #last name entry location in widget
fnameEntry = Entry(root)                                                    #first name entry
fnameEntry.place(x=350, y=120)                                              #first name entry location in widget
mnameEntry = Entry(root)                                                    #middle name entry
mnameEntry.place(x=350, y=150)                                              #middle name entry location in widget
bdayEntry = Entry(root)                                                     #birthday entry
bdayEntry.place(x=350, y=180)                                               #birthday entry location in widget
bdayEntry.insert(10, "yyyy/mm/dd")                                          #age entry
ageEntry = Entry(root)                                                      #age entry location in widget
ageEntry.place(x=350, y=210)                                                #address entry
addressEntry = Entry(root)                                                  #address entry location in widget
addressEntry.place(x=350, y=240)                                            #id entry
idEntry = Entry(root)                                                       #id entry location in widget
idEntry.place(x=350, y=350)

def add():                        #create a function for the button
    #set variables
    stnum = stnumEntry.get();     #student number variable
    lname = lnameEntry.get();     #last name variable
    fname = fnameEntry.get();     #first name variable
    mname = mnameEntry.get();     #middle name variable
    bday = bdayEntry.get();       #birthday variable
    age = ageEntry.get()          #age variable
    address = addressEntry.get()  #address variable
    # Connect to database
    guicon = pymysql.connect("localhost","root","","guistudent")
    # Create cursor object
    cursor = guicon.cursor()
    # Prepare SQL query to INSERT INTO tblstudent - table in guistudent
    sql = """INSERT INTO tblstudent(StudentNo, Lastname, Firstname, Middlename, Birthday, age, address) 
            VALUES ('%s','%s','%s','%s','%s','%s','%s')""" \
            % (stnum, lname, fname, mname, bday, age, address)
    # Execute SQL query
    cursor.execute(sql)
    # Commit changes
    guicon.commit()
    # Message box show in pop up; display the result
    msg = messagebox.showinfo("STUDENT INFO:","\nStudent Number\t:"+stnum +"\nLast Name\t:"+lname +"\nFirst Name\t:"+fname +"\nMiddle Name\t:"+mname +"\nBirthday\t\t:"+bday +"\nAge\t\t:"+age +"\nAddress\t\t:"+address)
    # Close database
    guicon.close()
    
    # Clear textboxes
    stnumEntry.delete(0, END)   # Clear textbox for stnumEntry
    lnameEntry.delete(0, END)   # Clear textbox for lnameEntry
    fnameEntry.delete(0, END)   # Clear textbox for fnameEntry
    mnameEntry.delete(0, END)   # Clear textbox for mnameEntry
    bdayEntry.delete(0, END)    # Clear textbox for bdayEntry
    ageEntry.delete(0, END)     # Clear textbox for ageEntry
    addressEntry.delete(0, END) # Clear textbox for addressEntry

def delete():                       #create a function for the button
    id = idEntry.get()              #id variable
    # Connect to database
    guicon = pymysql.connect("localhost","root","","guistudent")
    # Create cursor object
    cursor = guicon.cursor()
    # Prepare SQL query to DELETE FROM tblstudent - table in guistudent
    sql = """DELETE FROM tblstudent
            WHERE id=%s""" \
            % (id)
    # Execute SQL query
    cursor.execute(sql)
    # Commit changes
    guicon.commit()
    # Close database
    guicon.close()
    # Message box show in pop up; display "Student Deleted"
    messagebox.showinfo("Info","Student Deleted")
    # Clear textbox of id
    idEntry.delete(0, END)
    
def update():                     #create a function for the button
    #set variables
    id = idEntry.get();           #id variable
    stnum = stnumEntry.get();     #student number variable
    lname = lnameEntry.get();     #last name variable
    fname = fnameEntry.get();     #first name variable
    mname = mnameEntry.get();     #middle name variable
    bday = bdayEntry.get();       #birthday variable
    age = ageEntry.get()          #age variable
    address = addressEntry.get()  #address variable
    # Connect to database
    guicon = pymysql.connect("localhost","root","","guistudent")
    # Create cursor object
    cursor = guicon.cursor()
    # Prepare SQL query to UPDATE tblstudent - table in guistudent
    sql = """UPDATE tblstudent SET
        StudentNo = '%s',
        Lastname = '%s',
        Firstname = '%s',
        Middlename = '%s',
        Birthday = '%s',
        age = '%s',
        address = '%s'
        WHERE id = %s""" % (stnum,lname,fname,mname,bday,age,address,id)
    # Execute SQL query
    cursor.execute(sql)
    # Commit changes
    guicon.commit()
    # Close database
    guicon.close()
    # Message box show in pop up; display "Student Updated"
    messagebox.showinfo("Info","Student Updated")
    # Clear textbox of id
    idEntry.delete(0, END)
    
def read():                                 #create a function for the button
    student = Tk()                          #create widget
    student.title("Registered Students")    #widget title
    student.geometry("800x600")             #widget size
    
    # Connect to database
    guicon = pymysql.connect("localhost","root","","guistudent")
    # Create cursor object
    cursor = guicon.cursor()
    # Prepare SQL query to SELECT FROM tblstudent - table in student
    sql = "SELECT * FROM tblstudent"
    #execute SQL command
    cursor.execute(sql) 
    #fetch all the rows in a list of lists
    result = cursor.fetchall() 
    #disconnect from server
    guicon.close()
    
    idL = Label(student, text="id",width=5,height=2,bg="blue").grid(row=1, column=1)                    #id label and location in widget student
    stnumL = Label(student, text="Student Number",width=15,height=2,bg="blue").grid(row=1, column=2)    #student number label and location in widget student
    lnameL = Label(student, text="Last Name",width=15,height=2,bg="blue").grid(row=1, column=3)         #last name label and location in widget student
    fnameL = Label(student, text="First Name",width=15,height=2,bg="blue").grid(row=1, column=4)        #first name label and location in widget student
    mnameL = Label(student, text="Middle Name",width=15,height=2,bg="blue").grid(row=1, column=5)       #middle name label and location in widget student
    bdayL = Label(student, text="Birthday",width=15,height=2,bg="blue").grid(row=1, column=6)           #birthday label and location in widget student
    ageL = Label(student, text="Age",width=10,height=2,bg="blue").grid(row=1, column=7)                 #age label and location in widget student
    addressL = Label(student, text="Address",width=20,height=2,bg="blue").grid(row=1, column=8)         #address label and location in widget student
    
    for index, x in enumerate(result):                      # Create a loop to access result
        num = 0                                             # this is for the variable for column
        for y in x:                                         # nested loop to access the x in result
            readL = Label(student, text=y)                  # read Label in student widget
            readL.grid(row=index+2, column=num+1)           # read Label position in widget as grid
            num+=1                                          # increment num to make a table
    
addB=Button(root,text="ADD STUDENT",width=10,height=1,command=add).place(x=350, y=290)
deleteB=Button(root,text="Delete",width=10,height=1,command=delete).place(x=350, y=380)
updateB=Button(root,text="Update",width=10,height=1,command=update).place(x=350, y=430)
readB=Button(root,text="Show All",width=10,height=1,command=read).place(x=350, y=480)



root.mainloop()