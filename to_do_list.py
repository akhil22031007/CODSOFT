import tkinter
window = tkinter.Tk()

# To rename the window
window.title("To Do List")
window.geometry('400x500')
window.resizable(False,False)
task_list = []

# To do add task
def addTask():
    task = task_entry.get()
    task_entry.delete(0, tkinter.END)
    task_list.append(task)
    listbox.insert( tkinter.END, task)   

# To delete the task
def deleteTask():
    global task_list
    task = str(listbox.get(tkinter.ANCHOR))
    if task in task_list:
        task_list.remove(task)
        listbox.delete(tkinter.ANCHOR)

    
  
#icon
icon_path = "E:/Akhil/App_icon.png"
icon = tkinter.PhotoImage(file=icon_path)
window.iconphoto(False,icon)

#top bar
file_path = "E:/Akhil/Top bar.png" 
Top_bar = tkinter.PhotoImage(file="E:/Akhil/black.png")
top_bar_label = tkinter.Label(window,image=Top_bar)
top_bar_label.pack()

noteImage = tkinter.PhotoImage(file="E:/Akhil/dock.png")
note_image_Label = tkinter.Label(window,image=noteImage,bg="black")
note_image_Label.place(x=30,y=20)

dockImage = tkinter.PhotoImage(file="E:/Akhil/dock.png")

heading = tkinter.Label(window,text="ALL TASK", font="arial 15 bold",fg="white",bg="black")
heading.place(x=100,y=20)

#main 
frame = tkinter.Frame(window,width=400,height=35,bg="white")
frame.place(x=0,y=170)

task=tkinter.StringVar()
task_entry = tkinter.Entry(frame,width=10, font="Arial 12",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()
button = tkinter.Button(frame,text="ADD",bg="black",fg="white",font="Arial 15 bold",width=5,bd=0,command=addTask)
button.place(x=339,y=-3)

#list box
frame1 = tkinter.Frame(window,bd=3,width=700,height=280,bg="black")
frame1.pack(pady=(160,0))

listbox = tkinter.Listbox(frame1,font=('arial',12),width=40,height=8,bg="#928e85",fg="black",cursor="hand2",selectbackground="black")
listbox.pack(side="left", fill="both", padx=2,pady=5)
scrollbar = tkinter.Scrollbar(frame1)
scrollbar.pack(side = "right",fill="both")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# delete

delete_icon = tkinter.PhotoImage(file="E:/Akhil/delete.png")
tkinter.Button(window, image=delete_icon,bd=0,command=deleteTask).pack(side="bottom",pady=1)
window.mainloop()