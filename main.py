#main. Graph intrerfeice
import tkinter as tk
root = tk.Tk()
root.geometry('600x400')

#----------------button-----------
but1 = tk.Button(root, text='Кнопка 1')

but2 = tk.Button(root, text='Кнопка 2')

but3 = tk.Button(root, text='Кнопка 3')

def printer(event):
    print('Hello, dear')

#------place button---------
but1.grid(row=0,column=5,padx=110,pady=10)
but2.grid(row=0,column=6,padx=10,pady=10)
but3.grid(row=0,column=7,padx=10,pady=10)

#---------left mouse on but1--------------
but1.bind("<Button-1>",printer)



root.mainloop()
