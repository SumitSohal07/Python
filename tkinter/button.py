from tkinter import*


root=Tk()
#title of window
root.title("MY FIRST GUI")

#resizing the window
root.geometry("500x500")

#here we are linking the button with function

def click():
    lbl1 = Label(root,text = 'hi there', font = ('arial',15))
    lbl1.pack()

#here we are creating a button
    
Mybutton=Button(root,text ='click Me' ,font =('arial',20), fg='gold', bg ='black', command = click)
Mybutton.pack(padx=50,pady=50)

root.mainloop()