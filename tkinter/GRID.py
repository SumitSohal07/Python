from tkinter import*

root=Tk()
root.geometry("500x500")

#here we are using the pack

lbl1= Label(root,text="Sumit",font=('18,Bold'))

#here we are positing the text

lbl1.grid(row=0,column=0)

lbl1= Label(root,text="Sumit1",font=('18,Bold'))
lbl1.grid(row=0,column=1)

lbl1= Label(root,text="Sumit2",font=('18,Bold'))
lbl1.grid(row=1,column=0)

lbl1= Label(root,text="Sumit3",font=('18,Bold'))
lbl1.grid(row=1,column=1)

root.mainloop()