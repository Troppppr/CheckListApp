from tkinter import *
from tkinter import messagebox

def addItem():
    item = entry.get()
    if item != "":
        listBox.insert(END, item)
        entry.delete(0, END)
    else:
        messagebox.showerror("Error", "Enter something")


def deleteItem(event=None):
    try:
        if event:
            selected = listBox.nearest(event.y)
        else:
            selected = listBox.curselection()[0]
        item = listBox.get(selected)
        if item.startswith('\u2713'):
            item = item[1:]
            listBox.delete(selected)
            listBox.insert(selected, item)
            listBox.itemconfig(selected, {'fg': 'black'})
        else:
            checkedItem = "\u2713" + item
            listBox.delete(selected)
            listBox.insert(selected, checkedItem)
            listBox.itemconfig(selected, {'fg': 'gray'})
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Select something")


root = Tk()
root.title("Checklist App")
root.geometry("800x800")

frame1 = Frame(root)
frame1.pack(padx=10, pady=10)

listBox = Listbox(frame1, width=60, height=30, font=('Arial', 14))
listBox.pack(side=LEFT, fill=Y)

scrollBar = Scrollbar(frame1, orient=VERTICAL)
scrollBar.config(command=listBox.yview)
scrollBar.pack(side=LEFT, fill=Y)

listBox.config(yscrollcommand=scrollBar.set)
# Bind the double-click event to the deleteItem function
listBox.bind('<Double-Button-1>', deleteItem)

# Pre-set list of items with separators
preSetItems = [ "СПАЛЬНАЯ СИСТЕМА","---","Спальник", "Коврик / Матрас","Спальная одежда", "Подушка (при наличии)",
                " ",
                "КУХНЯ", "---", "Вилка / Ложка", "Кружка", "Тарелка глубокая",
                " ",

                "ВНЕШНЕЕ", "---", "Рюкзак", "Обувь (походная)", "Куртка непродуваемая", "Штаны", "Термобелье", "Носки (3-4 пары)",
                "Утепление для лагеря",
                '',

                "ДОПОЛНИТЕЛЬНО", "---", "Гигиена ( туалетка, щетка и тд)", "Салфетки влажные", "Зажигалка", "Нож (маленький)",
                "Мусорный мешок", "Фонарь налобный", "Павербанк", "Накидка от дождя"

               ]

# Insert pre-set items into the Listbox
for item in preSetItems:
    if item.startswith("---"):
        listBox.insert(END, "-"*60) # insert separator line
    else:
        listBox.insert(END, item)

entry = Entry(root, width=40, font=('Arial', 14))
entry.pack(padx=10, pady=10)

frame2 = Frame(root)
frame2.pack(padx=10, pady=10)

addButton = Button(frame2, text="Add", font=('Arial', 14), command=addItem)
addButton.pack(side=LEFT)

deleteButton = Button(frame2, text="Check", font=('Arial', 14), command=deleteItem)
deleteButton.pack(side=LEFT, padx=10)

root.mainloop()
