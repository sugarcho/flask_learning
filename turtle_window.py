from tkinter import *

window = Tk()
window.title("HI Let's start")
window.minsize(width=500, height=500)
window.resizable(width=False, height=500)

# # title
# Label = Label(text='my label', font=('Arial', 14, 'bold'), 
#               padx=5, pady=5, bg='red', fg='black'
#               )
# Label.pack()

# math of clicked
n = 0
a = StringVar()
a.set(n)

def add():
    global n
    n = n + 1
    a.set(n)

Label = Label(textvariable=a, font=('Arial', 20))
Label.pack()


# button create
def button_clicked():
    Label.config(text="Hi world!")

button = Button(text='Click Me', font=('Arial', 14, 'bold'), 
                padx=5, pady=5, bg='blue', fg='light green', 
                # command=button_clicked
                command=add
                )
button.pack()

# entry text
entry = Entry(width=30, font=('Arial', 14, 'bold'),
              bg="white", fg='black', state=NORMAL
              )
entry.insert(END, string="text please")
entry.pack()
print('entry.get:', entry.get())

# add text in entry
text = Text(height=5, width=30, font=("Arial", 14, "bold"), 
            bg="blue", fg="light green", state=NORMAL
            )
text.insert(END, "line 1\nline 2\nline 3")
text.pack()

print('2. text.get', text.get("1.0", "2.4"))

window.mainloop()