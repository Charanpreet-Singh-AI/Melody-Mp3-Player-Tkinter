from tkinter import *
root=Tk()
root.geometry("300x300")
def play_btn():
    print("btn working")
def rewind_btn():
    play_btn()
rewind_photo = PhotoImage(file="rewind.png")
btn = Button(root,image = rewind_photo, command=play_btn)
btn.pack()

rewind_photo = PhotoImage(file="rewind.png")
btn = Button(root,image = rewind_photo, command=rewind_btn)
btn.pack()

root.mainloop()
