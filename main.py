from tkinter import *

master = Tk()
master.geometry("200x200")
Label(master,
      text="Please enter your text here: ").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)


def retrieve_input():
    inputValue = e1.get()
    print(inputValue)


Button(master,
       text='Quit',
       command=master.quit).grid(row=3,
                                 column=0,
                                 sticky=W,
                                 pady=4)
Button(master,
       text='Show', command=retrieve_input).grid(row=3,
                                                 column=1,
                                                 sticky=W,
                                                 pady=4)

with open('text') as infile:
    contents = infile.read()
    contents = contents.replace(',', '\n')
    print(contents)

master.mainloop()
