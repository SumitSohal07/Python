from tkinter import*

root=Tk()
root.geometry("500x500")

#here we are using the pack

lbl1= Label(root,text="Sumit",font=('18,Bold'))

#here we are positing the text

lbl1.pack(side=TOP)

lbl1= Label(root,text="Sumit1",font=('18,Bold'))
lbl1.pack(side=BOTTOM)

lbl1= Label(root,text="Sumit2",font=('18,Bold'))
lbl1.pack(side=LEFT)

lbl1= Label(root,text="Sumit3",font=('18,Bold'))
lbl1.pack(side=RIGHT)

root.mainloop()