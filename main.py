from tkinter import *

window = Tk()
window.title('Mile to KM Converter')
window.minsize(width=450, height=250)

# entry window

user_entry = Entry(width=10)
user_entry.grid(column=1,row=0)

# label for entry window

label_of_miles = Label(text='Miles')
label_of_miles.grid(column=2,row=0)

window.mainloop()








#TODO: create entry window where user can specify number of miles they'd desire to convert to km
#TODO: below that, 'is equal to' then a label that updates with the km conversion 'KM'
#TODO: a calculate button that commands a function that returns the conversion



