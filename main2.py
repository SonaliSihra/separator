from tkinter import *

master = Tk()
master.geometry("400x400")
Label(master,
      text="Please enter your text here: ").grid(row=0)
Label(master,
      text="OUTPUT").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=0, column=1)

e2.columnconfigure(0, weight=10)
# By default the frame will shrink to whatever is inside of it and
# ignore width & height. We change that:

e2.place(x=170, y=20, height=25, width=175)


def retrieve_input():
    inputValue = e1.get()
    input1 = inputValue.replace(',', '\n')
    e2.insert(END, input1)
    print(input1)
    # e2.see(END)  # Scroll if necessary


Button(master,
       text='Quit',
       command=master.quit).grid(row=4,
                                 column=0,
                                 sticky=W,
                                 pady=4)
Button(master,
       text='Show', command=retrieve_input).grid(row=3,
                                                 column=0,
                                                 sticky=W,
                                                 pady=4)

with open('text') as infile:
    contents = infile.read()
    contents = contents.replace(',', '\n')
    print(contents)

master.mainloop()
