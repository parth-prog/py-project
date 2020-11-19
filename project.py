# Importing modules used in the project
from tkinter import *
import tkinter.messagebox as tkmsg
import tkinter.ttk as table
import mysql.connector as sql

# Establishing connection to mysql and creating cursor for executing queries
mycon = sql.connect(host="localhost", user="root", passwd="12345", database="darkgamingserver")
cursor = mycon.cursor()

# If database doesn't exist then it will be created
cursor.execute("create database if not exists darkgamingserver")

# If table doesn't exist then it will be created
cursor.execute("create table if not exists record (sno int(1) primary key , firstname varchar(15) not null , \
 lastname varchar(15) not null , ign varchar(20), phoneno varchar(10) not null , emailid varchar(30) , \
  gender varchar(1) , system varchar(11) not null)")

root = Tk()
root.geometry("1365x729")
root.title("Dark Gaming")


# Creating a home page(first GUI window) using a homepage_main() function
def homepage_main():
    intro = "Hello \n Hope you are well set \n So , let's begin"
    frame_1 = Frame(root, borderwidth=4, relief=SUNKEN, bg="black")
    frame_1.pack(side=TOP, fill=X, anchor="n")
    label1 = Label(frame_1, text=intro, font="System 35 bold", bg="black", fg="red")
    label1.pack(side=TOP, anchor="nw")

    frame_2 = Frame(root, bg="black")
    frame_2.pack(side=RIGHT, anchor="ne", fill=Y)

    # User will be able to choose between Admin or User access through below choose_access() function
    def choose_access():
        root.destroy()
        root1 = Tk()
        root1.geometry("1365x729")
        root1.title("Choose Access")
        frame_4 = Frame(root1, bg="black")
        frame_4.pack(fill=X)
        label3 = Label(frame_4, text="Want to get which Access ?", font="System 50 bold", fg="blue", relief=SUNKEN)
        label3.pack()

        frame_5 = Frame(root1, bg="blue")
        frame_5.pack(side=LEFT, fill=Y)
        label4 = Label(frame_5, text="""Please choose USER ACCESS
         if you wish to add your record 
        & want to get your 
        System as preferred by you .""", font="comicsans 30 bold", relief=SOLID)
        label4.pack(side=LEFT, anchor="nw")

        # If user click "USER ACCESS" button , user_access() function gets executed
        def user_access():
            root2 = Tk()
            root2.geometry("1365x729")
            root2.title("User Access")

            label6 = Label(root2, text="Please fill out the form below", font="comicsans 40 bold", bg="black",
                           fg="orange")
            label6.pack(fill=X)

            # For firstname
            label7 = Label(root2, text="Firstname", font="comicsans 20 bold", bg="yellow")
            label7.place(rely=0.2)
            firstnamevalue = StringVar()
            firstnameentry = Entry(root2, textvariable=firstnamevalue, font="comicsans 20 bold")
            firstnameentry.place(relx=0.12, rely=0.2)

            # For lastname
            label8 = Label(root2, text="Lastname", font="comicsans 20 bold", bg="yellow")
            label8.place(relx=0.4, rely=0.2)
            lastnamevalue = StringVar()
            lastnameentry = Entry(root2, textvariable=lastnamevalue, font="comicsans 20 bold")
            lastnameentry.place(relx=0.52, rely=0.2)

            # For ign(in game name)
            label9 = Label(root2, text="IGN(In Game Name)", font="comicsans 20 bold", bg="yellow")
            label9.place(rely=0.35)
            ignvalue = StringVar()
            ignentry = Entry(root2, textvariable=ignvalue, font="comicsans 20 bold")
            ignentry.place(relx=0.22, rely=0.35)

            # For Phoneno.
            label10 = Label(root2, text="Phoneno.", font="comicsans 20 bold", bg="yellow")
            label10.place(relx=0.5, rely=0.35)
            phonenovalue = StringVar()
            phonenoentry = Entry(root2, textvariable=phonenovalue, font="comicsans 20 bold")
            phonenoentry.place(relx=0.62, rely=0.35)

            # For EmailID
            label11 = Label(root2, text="Email ID", font="comicsans 20 bold", bg="yellow")
            label11.place(rely=0.5)
            emailidvalue = StringVar()
            emailidentry = Entry(root2, textvariable=emailidvalue, font="comicsans 20 bold")
            emailidentry.place(relx=0.12, rely=0.5)

            # For Gender
            label12 = Label(root2, text="Gender", font="comicsans 20 bold", bg="yellow")
            label12.place(relx=0.4, rely=0.5)
            gendervalue = StringVar()
            genderentry = Entry(root2, textvariable=gendervalue, font="comicsans 20 bold")
            genderentry.place(relx=0.5, rely=0.5)

            # For System
            label13 = Label(root2, text="System", font="comicsans 20 bold", bg="yellow")
            label13.place(rely=0.65)
            systemvalue = StringVar()
            systementry = Entry(root2, textvariable=systemvalue, font="comicsans 20 bold")
            systementry.place(relx=0.12, rely=0.65)

            # For filling information
            label14 = Label(root2, text="""1.) Firstname & Lastname couldn't be greater than 15 characters
            2.) IGN couldn't be greater than 20 characters
            3.) Phoneno. couldn't be greater than 10 characters
            4.) Email ID couldn't be greater than 30 characters
            5.) Gender should be either 'M'(male), 'F'(female),'O'(other)
            6.) System should be either 'PC','XBOX','PLAYSTATION'
            7.) Null values accepted only in IGN,Email ID,Gender""", font="System 10 bold")
            label14.place(relx=0.6, rely=0.6)

            # Getting values entered by user & inserting it into database or table record
            def gettingvalues():
                f = firstnameentry.get().upper()
                l = lastnameentry.get().upper()
                i = ignentry.get().upper()
                p = phonenoentry.get()
                e = emailidentry.get()
                g = genderentry.get().upper()
                s = systementry.get().upper()

                try:
                    if f == "" or l == "":
                        tkmsg.showerror("Blank", "You didn't entered anything in Firstname or Lastname or both")
                        root2.destroy()
                    elif p == "" or s == "":
                        tkmsg.showerror("Blank", "You didn't entered anything in Phoneno. or System or both")
                        root2.destroy()
                    elif g != "" and g not in ['M', 'F', 'O']:
                        tkmsg.showerror("Gender entry", "You didn't entered as mentioned")
                        root2.destroy()
                    elif s not in ['PC', 'XBOX', 'PLAYSTATION']:
                        tkmsg.showerror("System entry", "You didn't entered as mentioned")
                        root2.destroy()
                    else:
                        cursor.execute("select * from record")
                        cursor.fetchall()
                        count = cursor.rowcount

                        cursor.execute("insert into record values({},'{}','{}','{}','{}','{}','{}','{}')"
                                       .format(count+1, f, l, i, p, e, g, s))
                        tkmsg.showinfo("Record info", "Record added successfully")
                        root2.destroy()
                        mycon.commit()
                except:
                    tkmsg.showerror("ERROR", "Please read the instructions carefully and then TRY AGAIN")
                    root2.destroy()

            button4 = Button(root2, text="Submit", font="comicsans 30 bold", bg="red", command=gettingvalues)
            button4.place(relx=0.4, rely=0.8)
            root2.mainloop()

        button2 = Button(frame_5, text="USER ACCESS", font="comicsans 30 bold", bg="red", command=user_access)
        button2.place(relx=0.3, rely=0.5)

        frame_6 = Frame(root1, bg="purple")
        frame_6.pack(side=RIGHT, fill=Y)
        label5 = Label(frame_6, text="""Please choose ADMIN ACCESS
        if you wish to add ,
        delete ,
        display record/records .""", font="comicsans 30 bold", relief=SOLID)
        label5.pack()

        # To take a valid password for Admin access
        def admin_access_authentication():
            root3 = Tk()
            root3.title("Admin access authentication")
            root3.geometry("800x400")
            label15 = Label(root3, text="Please enter password", font="comicsans 20 bold")
            label15.place(rely=0.3)
            passvalue = StringVar()
            passentry = Entry(root3, textvariable=passvalue, font="comicsans 20 bold", show="*")
            passentry.place(relx=0.4, rely=0.3)

            # If entered password is correct then "if" statement gets executed otherwise "else" in below function
            def admin_access():
                if passentry.get() == "12345":
                    tkmsg.showinfo("Status", "Access Granted")
                    root3.destroy()
                    root1.destroy()
                    root4 = Tk()
                    root4.geometry("1365x729")
                    root4.title("Admin Access")

                    admin_intro = "Hi Admin \n What would you like to do ?"
                    label16 = Label(root4, text=admin_intro, font="System 35 bold", bg="black", fg="orange")
                    label16.pack(fill=X)

                    button6 = Button(root4, text="Add record", font="comicsans 30 bold", bg="red", command=user_access)
                    button6.place(rely=0.3)

                    label17 = Label(root4, text="Move furhter \n down for more", font="comicsans 30 bold", bg="orange")
                    label17.place(relx=0.2, rely=0.42)

                    # To delete a record
                    def delete_record():
                        root7 = Tk()
                        root7.geometry("500x300")
                        root7.title("Delete record")
                        label18 = Label(root7, text="Please enter Serial no.(Sno)\n of the record you want to delete",
                                        font="comicsans 20 bold")
                        label18.pack()
                        snovalue2 = StringVar()
                        snoentry2 = Entry(root7, textvariable=snovalue2, font="comicsans 20 bold")
                        snoentry2.pack()

                        # To get the value entered and then work accordingly in deletion
                        def get_sno2():
                            entered_sno2 = snoentry2.get()
                            if entered_sno2.isdigit():
                                cursor.execute("select * from record where sno={}".format(entered_sno2,))
                                data = cursor.fetchone()
                                if data is None:
                                    tkmsg.showinfo("Record info", "No such record found")
                                    root7.destroy()
                                else:
                                    cursor.execute("delete from record where sno={}".format(entered_sno2,))
                                    cursor.execute("update record set sno=sno-1 where sno>{}".format(entered_sno2,))
                                    mycon.commit()
                                    tkmsg.showinfo("Record info", "Record successfully deleted")
                                    root7.destroy()
                            else:
                                tkmsg.showerror("Type error", "Please enter only a number...TRY AGAIN")
                                root7.destroy()

                        button10 = Button(root7, text="Submit", font="comicsans 30 bold", bg="red", command=get_sno2)
                        button10.pack()
                        root7.mainloop()

                    button7 = Button(root4, text="Delete record", font="comicsans 30 bold", bg="red",
                                     command=delete_record)
                    button7.place(relx=0.45, rely=0.55)

                    # To display all the records
                    def display_record():
                        root8 = Tk()
                        root8.geometry("1365x729")
                        root8.title("Dark Gaming record")
                        cursor.execute("select * from record")
                        data = cursor.fetchall()
                        count = cursor.rowcount
                        tab = table.Treeview(root8, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height=count)
                        tab.pack()
                        tab.heading(1, text="Sno")
                        tab.heading(2, text="Firstname")
                        tab.heading(3, text="Lastname")
                        tab.heading(4, text="IGN")
                        tab.heading(5, text="Phoneno")
                        tab.heading(6, text="Email ID")
                        tab.heading(7, text="Gender")
                        tab.heading(8, text="System")

                        tab.column(1, width=40, anchor="s")
                        tab.column(2, anchor="s")
                        tab.column(3, anchor="s")
                        tab.column(4, anchor="s")
                        tab.column(5, anchor="s")
                        tab.column(6, anchor="s")
                        tab.column(7, width=50, anchor="s")
                        tab.column(8, anchor="s")

                        for i in data:
                            tab.insert("", "end", values=i)

                        # For closing the displaying records window and moving back to Admin Access window
                        def back():
                            root8.destroy()

                        button11 = Button(root8, text="BACK", font="comicsans 30 bold", bg="red", command=back)
                        button11.place(relx=0.8, rely=0.8)
                        root8.mainloop()

                    button8 = Button(root4, text="Display record", font="comicsans 30 bold", bg="red",
                                     command=display_record)
                    button8.place(relx=0.67, rely=0.68)

                    # To close the Admin Access window
                    def exit():
                        root4.destroy()

                    button9 = Button(root4, text="Exit", font="comicsans 30 bold", bg="red", command=exit)
                    button9.place(relx=0.9, rely=0.82)
                    root4.mainloop()
                else:
                    tkmsg.showinfo("Status", "Access Denied")
                    root3.destroy()

            button5 = Button(root3, text="Submit", font="comicsans 30 bold", bg="red", command=admin_access)
            button5.place(relx=0.4, rely=0.5)
            root3.mainloop()

        button3 = Button(frame_6, text="ADMIN ACCESS", bg="red", font="comicsans 30 bold",
                         command=admin_access_authentication)
        button3.place(relx=0.2, rely=0.5)
        root1.mainloop()

    button1 = Button(frame_2, text="Click here to continue", font="comicsans 20 bold", bg="red", command=choose_access)
    button1.pack(side=RIGHT)


# Inserting image(Darkgaming logo) on the homepage
frame_3 = Frame(root, bg="black")
frame_3.pack(side=BOTTOM, fill=X)
ph = PhotoImage(file="DARKGAMING.png")
label2 = Label(frame_3, image=ph)
label2.pack(side=BOTTOM)

homepage_main()

root.mainloop()
