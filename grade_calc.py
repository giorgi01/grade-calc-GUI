from tkinter import *


def calculate():
    lst = [
        float(first_grade.get()), float(second_grade.get()),
        float(third_grade.get()),float(fourth_grade.get()),
        float(fifth_grade.get()), float(sixth_grade.get())
    ]
    blank.insert(INSERT, str(round(sum(lst)/len(lst), 2)))
    root.update()


root = Tk()
root.title('Grade Calculator')
root.geometry('500x300')
Label(root, text='საგანი №1', height=2, width=15)\
    .grid(row=0)
first = Entry(root, width=30)
first.grid(row=0, column=1)
Label(root, text='საბოლოო ქულა', height=2, width=15)\
    .grid(row=0, column=2, padx=5)
first_grade = Entry(root, width=5)
first_grade.grid(row=0, column=3, padx=5)

Label(root, text='საგანი №2', height=2, width=15)\
    .grid(row=1)
second = Entry(root, width=30)
second.grid(row=1, column=1)
Label(root, text='საბოლოო ქულა', height=2, width=15)\
    .grid(row=1, column=2, padx=5)
second_grade = Entry(root, width=5)
second_grade.grid(row=1, column=3, padx=5)

Label(root, text='საგანი №3', height=2, width=15)\
    .grid(row=2)
third = Entry(root, width=30)
third.grid(row=2, column=1)
Label(root, text='საბოლოო ქულა', height=2, width=15)\
    .grid(row=2, column=2, padx=5)
third_grade = Entry(root, width=5)
third_grade.grid(row=2, column=3, padx=5)

Label(root, text='საგანი №4', height=2, width=15)\
    .grid(row=3)
fourth = Entry(root, width=30)
fourth.grid(row=3, column=1)
Label(root, text='საბოლოო ქულა', height=2, width=15)\
    .grid(row=3, column=2, padx=5)
fourth_grade = Entry(root, width=5)
fourth_grade.grid(row=3, column=3, padx=5)

Label(root, text='საგანი №5', height=2, width=15)\
    .grid(row=4)
fifth = Entry(root, width=30)
fifth.grid(row=4, column=1)
Label(root, text='საბოლოო ქულა', height=2, width=15)\
    .grid(row=4, column=2, padx=5)
fifth_grade = Entry(root, width=5)
fifth_grade.grid(row=4, column=3, padx=5)

Label(root, text='საგანი №6', height=2, width=15)\
    .grid(row=5)
sixth = Entry(root, width=30)
sixth.grid(row=5, column=1)
Label(root, text='საბოლოო ქულა', height=2, width=15)\
    .grid(row=5, column=2, padx=5)
sixth_grade = Entry(root, width=5)
sixth_grade.grid(row=5, column=3, padx=5)

Label(root, text='თქვენი სარეიტინგო ქულა:', height=2, width=25)\
    .grid(row=6, column=1)
blank = Entry(root, width=10)
blank.grid(row=6, column=2)

check_button = Button(root, text='Calculate', width=25, command=calculate)
check_button.place(x=111, y=250)
mainloop()
