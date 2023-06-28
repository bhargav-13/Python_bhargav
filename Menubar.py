from tkinter import *

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0, font=('MV Boli',15))
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="EXIT", command=quit)

editmenu = Menu(menubar, tearoff=0, font=('MV Boli',15))
menubar.add_cascade(label="EDIT",menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_separator()
editmenu.add_command(label="Delete", command=quit)

frame = Frame(window,bg="pink",bd=5,relief=SUNKEN)
frame.pack()

Button(frame,text="W",font=("Consolas",25),width=3).pack(side=TOP)
Button(frame,text="A",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="S",font=("Consolas",25),width=3).pack(side=LEFT)
Button(frame,text="D",font=("Consolas",25),width=3).pack(side=LEFT)

canvas = Canvas(window, height=500, width=500)
# canvas.create_line(0,0,500,500 ,fill="blue", width=5)
# canvas.create_line(0,500,500,0 ,fill="red", width=5)
# canvas.create_rectangle(10,100,400,400)
# canvas.create_rectangle(100,10,400,400)
# canvas.create_rectangle(100,100,490,400)
# canvas.create_rectangle(100,100,400,490)
# canvas.create_rectangle(200,200,300,300)

#Pokemane
canvas.create_arc(0,0,500,500,style=PIESLICE , fill="red", extent=180, width=10 )
canvas.create_arc(0,0,500,500,style=PIESLICE , fill="white", extent=180, start=180, width=10 )
canvas.create_oval(190,190,310,310, fill="white", width=10)
canvas.pack()



window.mainloop()