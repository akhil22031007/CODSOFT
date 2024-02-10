import tkinter
from tkinter import *

calc = Tk()
calc.title("Calculator")
calc.geometry("260x400+100+200")
calc.resizable(False,False)
calc.configure(bg="#FFA586")

equation = ""

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def show(value):
    global equation
    if value == "." and "." in equation: # Prevent adding multiple dots
        return
    equation += value
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation !="":
        try:
            result= eval (equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)
    equation = str(result)

 


label_result = Label(calc,width = 25, height= 2,text="",font=("arial",25), bg="black",fg="white")
label_result.pack()

icon_path = "E:/Akhil/calculator.png"
icon = tkinter.PhotoImage(file=icon_path)
calc.iconphoto(False,icon)

Button(calc,text="C",bg="#190019",fg="white",height=2,width=6,bd=1,command=lambda: clear()).place(x=9,y=100)
Button(calc,text="%",bg="#190019",fg="white",height=2,width=6, bd=1,command=lambda: show("%")).place(x=75,y=100,)
Button(calc,text="/",bg="#190019",fg="white",height=2,width=6, bd=1,command=lambda: show("/")).place(x=140,y=100)
Button(calc,text="*",bg="#190019",fg="white",height=2,width=6, bd=1,command=lambda: show("*")).place(x=205,y=100)

Button(calc,text="7",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("7")).place(x=9,y=150)
Button(calc,text="8",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("8")).place(x=75,y=150)
Button(calc,text="9",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("9")).place(x=140,y=150)
Button(calc,text="-",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("-")).place(x=205,y=150)

Button(calc,text="4",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("4")).place(x=9,y=200)
Button(calc,text="5",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("5")).place(x=75,y=200)
Button(calc,text="6",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("6")).place(x=140,y=200)
Button(calc,text="+",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("+")).place(x=205,y=200)

Button(calc,text="1",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("1")).place(x=9,y=250)
Button(calc,text="2",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("2")).place(x=75,y=250)
Button(calc,text="3",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show("3")).place(x=140,y=250)
Button(calc,text="=",bg="#190019",fg="white",height=5,width=7, bd=1, command=lambda: calculate()).place(x=196,y=250)

Button(calc,text="0",bg="#190019",fg="white",height=2,width=16, bd=1, command=lambda: show("0")).place(x=9,y=300)
Button(calc,text=".",bg="#190019",fg="white",height=2,width=6, bd=1, command=lambda: show(".")).place(x=140,y=300)

calc.mainloop()