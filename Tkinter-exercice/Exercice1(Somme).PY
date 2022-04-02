from tkinter import *
from turtle import width
  

root = Tk()
root.geometry("300x320" )
def calc():
  s= int(A.get()) + int (B.get()) + int (Q.get())
  r.config(text=s)
 
 


a=Label(text="A"  )
a.grid(row=0 ,column=0 , pady=10)
A=Entry( width=45 , bg="red" , fg="black"  )
A.grid(row=0 , column=1   )
 
b =Label(text="B")
b.grid(row=1 ,column=0 , pady=10)
B=Entry(width=45 , bg="red" , fg="black")
B.grid(row=1 , column=1)

q =Label(text="C")
q.grid(row=2 ,column=0 , pady=10)
Q=Entry(width=45 , bg="red" , fg="black" )
Q.grid(row=2 , column=1)

btn = Button(text='Somme' , command=calc )
btn.grid(row=3  , column=1 , pady=10)



btn = Button(text='Quitter' , command=quit , bg="gold" )
btn.grid(row=4 , column=1)

r = Label(text="resultat : " , pady=15)
r.grid(row=5 , column=1)


root.mainloop()



