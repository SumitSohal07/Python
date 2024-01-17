from tkinter import*


root=Tk()
#title of window
root.title("MY FIRST GUI")

#resizing the window
root.geometry("500x500")


entry = Entry(root, width = 50, font=('arial',15))
entry.pack(padx=20,pady=20)

def click():
    text1 = "hello " + entry.get()
    lbl1 = Label(root,text = text1, font = ('arial',15))
    lbl1.pack()

Mybutton=Button(root, text = 'click Me', font = ('arial',15),command=click)
Mybutton.pack(padx=50,pady=50)


root.mainloop()