from tkinter import ttk
#import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
from PIL import Image, ImageTk
import sqlite3
Profile = {1:""}


def add_customer():
    name = entryName.get()
    phone = entryPhoneNumber.get()
    more = entryMoreInfo.get()
    # create connection
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    # Insert data
    cur.execute("INSERT INTO custom ('name', 'phone', 'moreinfo') values (?,?,?)", (name, phone, more))
    # Commit connection
    conn.commit()
    conn.close()
    # Refresh instantané
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    select = cur.execute("SELECT*FROM custom order by id desc")
    select = list(select)
    tree.insert('', END, values=select[0])
    conn.close()

    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    select = cur.execute("SELECT*FROM custom order by id desc")
    select = list(select)
    id = select[0][0]
    filename = entryPhoto.get()
    im = Image.open(filename)
    rgb_im = im.convert('RGB')
    rgb_im.save(("images/profil_" + str(id)+ "." + "jpg"))
    conn.close()


def delete_customer():
    idSelect = tree.item(tree.selection())['values'][0]
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    delete = cur.execute("delete from custom where id = {}".format(idSelect))
    conn.commit()
    tree.delete(tree.selection())

def sortByName():
    # clear the treeview
    for x in tree.get_children():
        tree.delete(x)
    # Create connection
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    select = cur.execute("select*from custom order by name asc")
    conn.commit()

    for row in select:
        tree.insert('', END, values = row)
    conn.close()

def SearchByName(event):
    # clear the treeview
    for x in tree.get_children():
        tree.delete(x)
    name = entrySearchByName.get()
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    select = cur.execute("SELECT*FROM custom where name = (?)", (name,))
    conn.commit()
    for row in select:
        tree.insert('', END, values = row)
    conn.close()

def SearchByPhone(event):
    # clear the treeview
    for x in tree.get_children():
        tree.delete(x)
    phone = entrySearchByPhone.get()
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    select = cur.execute("SELECT*FROM custom where phone = (?)", (phone,))
    conn.commit()
    for row in select:
        tree.insert('', END, values = row)
    conn.close()

def BrowsePhoto():
    entryPhoto.delete(0,END)
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select File")
    entryPhoto.insert(END, filename)

def treeActionSelect(event):
    # load image
    label_image.destroy()
    idSelect = tree.item(tree.selection())['values'][0]
    nameSelect = tree.item(tree.selection())['values'][1]
    phoneSelect = tree.item(tree.selection())['values'][2]
    moreInfoSelect = tree.item(tree.selection())['values'][3]
    imgProfile = "images/profil_" + str(idSelect) + "." + "jpg"
    load = Image.open(imgProfile)
    load.thumbnail((100,100))
    photo = ImageTk.PhotoImage(load)
    Profile[1] = photo
    lblImage = Label(root ,  image = photo)
    lblImage.place(x=10 , y=350)
    lid = Label(root, text = "ID : " + str(idSelect))
    lid.place(x = 110, y = 350 , width = 50)
    lname = Label(root, text = " Name : " + nameSelect)
    lname.place(x=110 , y = 380 , width = 150)
    lphone = Label(root, text = "Phone : " + str(phoneSelect))
    lphone.place(x = 110 , y = 410 , width = 150)
    Tmore = Text(root)
    Tmore.place(x = 260 , y = 360 , width = 280 , height =100)
    Tmore.insert(END , "More Info : " +  moreInfoSelect)



root = Tk()
root.title("Address Book")
root.geometry("550x450")
#root.configure(bg = "#eaeaea")

# Add Title
lblTitle = Label(root , text = "Address Book" , font = ("Arial" , 21) , bg="darkblue" , fg = "white" )
lblTitle.place(x = 0 , y = 0 , width = 250, height = 41)

# Search area
lblSearchByName = Label(root, text ="Search by name :", bg ="darkblue", fg ="white")
lblSearchByName.place(x = 250, y=0, width = 120)
entrySearchByName = Entry(root)
entrySearchByName.bind("<Return>" , SearchByName)
entrySearchByName.place(x = 380, y = 0, width = 160)

lblSearchByPhone = Label(root, text="Search by phone", bg="darkblue", fg="white")
lblSearchByPhone.place(x = 250, y = 20, width = 120)
entrySearchByPhone = Entry(root)
entrySearchByPhone.bind("<Return>", SearchByPhone)
entrySearchByPhone.place(x = 380, y = 20, width = 160)

# label Name & Surname
lblName = Label(root, text="name & surname :", bg="grey", fg="yellow")
lblName.place(x = 5, y = 45, width = 125)
entryName = Entry(root)
entryName.place(x = 140, y = 45, width = 400 )

# Phone Number
lblPhoneNumber = Label(root, text="Phone Number :", bg="grey", fg="yellow")
lblPhoneNumber.place(x = 5, y = 70, width = 125 )
entryPhoneNumber = Entry(root)
entryPhoneNumber.place(x = 140, y = 70, width = 400)

# Photo
lblPhoto = Label(root, text="Photo :", bg="grey", fg="yellow")
lblPhoto.place(x = 5, y = 95, width = 125 )
Bphoto = Button(root, text="Browse", bg="darkblue", fg="yellow", command = BrowsePhoto)
Bphoto.place(x = 490, y = 95, height = 19 )
entryPhoto = Entry(root)
entryPhoto.place(x = 140, y = 95, width = 320)

# More info
lblMoreInfo = Label(root, text="More Info :", bg="grey", fg="yellow")
lblMoreInfo.place(x = 5, y = 120, width = 125 )
entryMoreInfo = Entry(root)
entryMoreInfo.place(x = 140, y = 120, width = 400)

# button command
bAdd = Button(root, text="Add Customer", bg="darkblue", fg="yellow", command = add_customer)
bAdd.place(x = 5, y = 145, height= 30, width = 250)
bDelete = Button(root, text="Delete Selected", bg="darkblue", fg="yellow", command = delete_customer)
bDelete.place(x = 5, y = 170, height= 30, width = 250)
bEdit = Button(root, text="Edit Selected", bg="darkblue", fg="yellow")
bEdit.place(x = 5, y = 195, height= 30, width = 250)
bSort = Button(root, text="Sort by name", bg="darkblue", fg="yellow", command = sortByName)
bSort.place(x = 5, y = 220, height= 30, width = 250)
bExit = Button(root, text="Exit app", bg="darkblue", fg="yellow", command = quit)
bExit.place(x = 5, y = 245, height= 30, width = 250)

load = Image.open("images/profil_.png")
load.thumbnail((130,130))
photo = ImageTk.PhotoImage(load)
label_image = Label(root, image = photo)
label_image.place(x = 10, y = 300)

# add Treeview
tree = ttk.Treeview(root, columns = (1, 2, 3), height = 5, show = "headings")
tree.place(x = 265, y = 145, width = 290, height = 175)
tree.bind("<<TreeviewSelect>>", treeActionSelect)

# add headings
tree.heading(1, text = "ID")
tree.heading(2, text = "Name")
tree.heading(3, text = "Phone")

# Define column width
tree.column(1, width = 50)
tree.column(2, width = 100)

# Display data in treeview object
conn = sqlite3.connect('database.db')
cur = conn.cursor()
select = cur.execute("select*from custom")
for row in select:
    tree.insert('', END, value = row)
conn.close()

root.mainloop()

