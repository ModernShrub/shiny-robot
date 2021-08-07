from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("iijgg")
root.geometry("600x400")

img = ImageTk.PhotoImage(Image.open("SKletalcard.jpg"))

inputboxboi = Entry(root)
inputboxboi.place(relx=0.5,rely=0.2,anchor=CENTER)

imglabel = Label(root, image=img)
imglabel.place(relx=0.5,rely=0.8,anchor=CENTER)

def auth() :
    pin = 0
    try:
        pin = int(inputboxboi.get())
        messagebox.showinfo("Alert", "PIN is right")
        
    except:
        messagebox.showinfo("Error", "PIN is wrong")
            
btn = Button(root, text="Authenticate card",command=auth)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

root.mainloop()

