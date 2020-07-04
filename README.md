import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("font.ico")
window.config(background = '#4B88BE')

# creer la frame principale
frame = Frame(window, bg = "#4B88BE")

# creation d'image
width = 300
height = 300
image = PhotoImage(file = "password.png")
canvas = Canvas(frame, width = width, height = height, bg = "#4B88BE", bd = 0, highlightthickness = 0 )
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row = 0, column = 0, sticky = W)

# creer une sous boite
right_frame = Frame(frame, bg="#4B88BE")
right_frame.grid(row = 0, column = 1, sticky = W)

# creer un titre
label_title = Label(right_frame, text = "Mot de passe", font =("Helvetica", 20), bg = "#4B88BE", fg = "white")
label_title.pack()

# creer un input
password_entry = Entry(right_frame, font =("Helvetica", 20), bg = "#4B88BE", fg = "white")
password_entry.pack()

# creer un bouton
generate_password_button = Button(right_frame, text = "Générer", font =("Helvetica", 20), bg = "#4B88BE", fg = "white", command= generate_password)
generate_password_button.pack(fill=X)


frame.pack(expand = YES)

menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff = 0)
file_menu.add_command(label="Nouveau", command = generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
menu_bar.add_cascade

window.config(menu=menu_bar)



window.mainloop()
