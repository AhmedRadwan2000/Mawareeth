from pprint import pprint
from tkinter import *
from tkinter.messagebox import showwarning
from heirs import *

heirs = {'son':'إبن', 'son-of-son':'إبن ابن',
         'father':'أب', 'grand-father':'جد',
         'husband':'زوج', 'brother':'أخ شقيق',
         'daughter':'بنت', 'daughter-of-son':'بنت إبن',
         'mother':'أم', 'grand-mother':'جدة',
         'wife':'زوجة', 'fbrother':'أخ لأب',
         'son-of-brother':'إبن أخ شقيق', 'son-of-fbrother':'إبن أخ لأب',
         'uncle':'عم شقيق', 'funcle':'عم لأب',
         'cousin':'إبن عم شقيق', 'fcousin':'إبن عم لأب',
         'sister':'أخت شقيقة', 'fsister':'أخت لأب',
         'msiblings':'أخوة لأم'}


def reverse_words(heirs):
    for heir in heirs:
        l = heirs[heir].split()
        l.reverse()
        heirs[heir] = ' '.join(l)
    return


reverse_words(heirs)


def validate(data):
    if data['husband'] == 1 and data['wife'] == 1:
        return False
    elif inheritance_box.get(1.0, END).strip() == '':
        return False
    for data_ in data:
        temp = data[data_]
        if temp > 100 or temp < 0:
            return False
    return True


def get_data():
    data = {}
    for heir_data in heirs_data:
        if heir_data[2].get():
            if heir_data[4] == 'father' or heir_data[4] == 'mother' or heir_data[4] == 'grand-father' or heir_data[4] == 'grand-mother' or heir_data[4] == 'husband':
                data[heir_data[4]] = 1
            elif heir_data[0].get(1.0, END).strip() == '':
                data[heir_data[4]] = 1
            else:
                data[heir_data[4]] = eval(heir_data[0].get(1.0, END).strip())
        else:
            data[heir_data[4]] = 0
    pprint(data)
    if validate(data):
        inheritance = eval(inheritance_box.get(1.0, END).strip())
        results = calc(data, inheritance)
        display_result(results, data)
    else:
        showwarning(title='Error', message='Invalid Data')
    return


def display_result(results, data):
    global new_window
    if new_window != 0:
        new_window.destroy()
    new_window = Toplevel()
    new_window.title('Mawareeth')
    results_box = Text(new_window, font=('Verdana', 16), height=25, width=26, padx=16, pady=16)
    results_box.grid(row=0, pady=16, padx=16, sticky=N)
    results_box.insert(END, 'الشخص')
    results_box.insert(END, '\t\t')
    results_box.insert(END, 'شخص كل نصيب')
    results_box.insert(END, '\n')
    results_box.insert(END, '---------------------------------')
    results_box.insert(END, '\n')
    for heir_data in results:
        results_box.insert(END, heirs[heir_data])
        results_box.insert(END, '\t\t')
        if data[heir_data] > 1:
            temp = round(results[heir_data] / data[heir_data], 2)
            results_box.insert(END, f'{temp} x {data[heir_data]}')
            results_box.insert(END, '\n')
        else:
            results_box.insert(END, results[heir_data])
            results_box.insert(END, '\n')

    return



root = Tk()
root.title('Mawareeth')
new_window = 0


heirs_frame = Frame(width=380, height=380)
heirs_frame.grid(row=0,column=0, padx=8, pady=8, sticky=N)
heirs_frame.grid_columnconfigure(1, weight=1)
heirs_frame.grid_propagate(False)

heirs_first_frame = Frame(heirs_frame)
heirs_first_frame.grid(row=0, column=0, sticky=N)
heirs_second_frame = Frame(heirs_frame)
heirs_second_frame.grid(row=0, column=2, sticky=N)

toggle_frame = heirs_first_frame

heirs_data = []
for i, heir in enumerate(heirs):
    if i > 9:
        toggle_frame = heirs_second_frame
    heir_data = [0]*5
    heir_data[0] = Text(toggle_frame, font=('Verdana', 16), height=1, width=2)
    if heir == 'father' or heir == 'mother' or heir == 'grand-father' or heir == 'grand-mother' or heir == 'husband':
        heir_data[0].configure(state=DISABLED)
    heir_data[0].grid(row=i, column=0)
    heir_data[1] = Label(toggle_frame, text=heirs[heir], font=('Verdana', 16))
    heir_data[1].grid(row=i, column=1)
    heir_data[2] = IntVar()
    heir_data[3] = Checkbutton(toggle_frame, var=heir_data[2])
    heir_data[3].grid(row=i, column=2)
    heir_data[4] = heir
    heirs_data.append(heir_data)


result_frame = Frame()
result_frame.grid(row=1)
btn = Button(result_frame, text='وزَّع', font=('Verdana', 16), width=8, command=get_data)
btn.grid(row=1, column=0, pady=8, padx=8)
inheritance_box = Text(result_frame, font=('Verdana', 16), height=1, width=15)
inheritance_box.grid(row=0, column=0, sticky=E)
inheritance_label = Label(result_frame, font=('Verdana', 16), text=' : التركة')
inheritance_label.grid(row=0, column=1, sticky=E)


mainloop()