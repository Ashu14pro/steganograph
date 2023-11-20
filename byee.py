from tkinter import *
from tkinter import filedialog, simpledialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb

# Caesar Cipher Encryption and Decryption Functions
def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.isupper():
                result += chr((shifted - 65) % 26 + 65)
            else:
                result += chr((shifted - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, key):
    return encrypt(text, -key)

root = Tk()
root.title("Steganography - Hide a Secret Text Message in an Image")
root.geometry("700x500+250+180")
root.resizable(True, True)
root.configure(bg="#2f4155")

filename = ""

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title='Select Image File',
                                          filetypes=(("PNG file", "*.png"),
                                                     ("JPG File", "*.jpg"),
                                                     ("All files", "*.*")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

def set_password():
    global password
    password = simpledialog.askstring("Set Password", "Enter the encryption password:", show='*')

def enter_password():
    global password
    password = simpledialog.askstring("Enter Password", "Enter the decryption password:", show='*')

def Hide():
    global filename, password
    set_password()
    message = text1.get(1.0, END)
    
    # Encrypt the message using Caesar Cipher
    key = 3  # You can change the key
    encrypted_message = encrypt(message, key)
    
    secret = lsb.hide(filename, encrypted_message)
    secret.save("hidden.png")

def Show():
    global filename, password
    enter_password()
    clear_message = lsb.reveal(filename)
    
    # Decrypt the message using Caesar Cipher
    key = 3  # You should use the same key as used during encryption
    decrypted_message = decrypt(clear_message, key)
    
    text1.delete(1.0, END)
    text1.insert(END, decrypted_message)

# logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#2f4155").place(x=10, y=0)

Label(root, text="CYBER SECURITY", bg="#2d4155", fg="white", font="arial 25 bold").place(x=100, y=20)

# first frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=0, y=0)

# second Frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# third frame
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold").place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

# fourth frame
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=Show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()

root.mainloop()
