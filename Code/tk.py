import swaln as swa
from tkinter import *


root=Tk()

root.title("Tool")
thelabel = Label(root,text="Application for alignment").grid(row=1,column=2)
#thelabel.pack()

seqA = StringVar()
seqB = StringVar()

Label(root,text="Enter Referance Sequence = ").grid(row=7,column=1)
e1 = Entry(root,textvariable = seqA)
e1.grid(row=7,column=2)
Label(root, text='Enter Query Sequence = ').grid(row=8,column=1) 
e2 = Entry(root,textvariable = seqB) 
e2.grid(row=8, column=2) 


button = Button(root,text="Align Sequence",command=lambda:swa.s_w(seqA.get(),seqB.get())).grid(row=9,column=2)


"""menu = Menu(root) 
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_command(label='Refresh') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') """
root.mainloop()