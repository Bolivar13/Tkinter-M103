import tkinter  as tk 
from tkinter import  ttk


app = tk.Tk()

app.geometry('300x250')


personnes=[
    {'nom': 'med','age': 18},
    {'nom': 'nour','age': 30},
    {'nom': 'said','age': 20} ,
    {'nom': 'rachid','age': 20}
]

def search(e):
    s = chercher_Entry.get()
    print(s)

    for child in tree.get_children():
        tree.delete(child)

    for p in personnes:
        if s.lower() in p['nom']:
            tree.insert('', tk.END, values=[p['nom'], p['age']])

    


chercher = tk.Label(text= "chercher" , pady=10)
chercher.grid(column=0 , row=0)
chercher_Entry = tk.Entry()
chercher_Entry.grid (column=1 , row=0)



head =  ['Nom','Age'   ]
colms = ['Nom','Age' , ]

tree = ttk.Treeview(columns=colms, show='headings',   height=8 )
for x in range(len(colms)):
    tree.column(colms[x],width=100)
    tree.heading(colms[x],text=head[x])

tree.grid(column=1, row=1, rowspan=4 )


tree.insert(parent='', index=0, iid=0, text='', values=('med','10' )) 
tree.insert(parent='', index=1, iid=1, text='', values=('nour','18' )) 
tree.insert(parent='', index=1, iid=2, text='', values=('said','18' )) 
tree.insert(parent='', index=1, iid=3, text='', values=('rachid','18' )) 

app.bind('<KeyRelease>', search)
app.mainloop()