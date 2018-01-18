'''Created on Jan 13, 2018, @author: daneaadland'''


from tkinter import *

label_list = ['Name', 'Seasons', 'Episodes', 'Category', 'Priority Score']
show_count = 0
entries_list = []

root = Tk()
label_frame = Frame(root)
entries_frame = Frame(root)

label_frame.pack(side=TOP, expand=True, fill='both')
#label_frame.grid(sticky=N+S+E+W)
entries_frame.pack(side=BOTTOM)

def init_labels():
    for index, col in enumerate(label_list):
        col_label = Label(label_frame, text=col)
        #col_label.pack(side=LEFT)
        col_label.grid(row=0, column=index, sticky=N+S+E+W)

def add_show():
    #global entries_list
    new_frame = Frame(entries_frame)
    new_frame.pack()
    for entry in range(len(label_list)):
        global show_count
        v_entry = StringVar()
        entries_list.append(v_entry)
        entry_location = len(entries_list) - 1
        show_count += 1
        new_entry = Entry(new_frame, textvariable=entries_list[entry_location])
        new_entry.pack(side=LEFT)
        
def print_shows():
    for entry in entries_list:
        print(entry.get())

# L_name = Label(label_frame, text="Name")
# L_seasons = Label(label_frame, text="Seasons")
# L_episodes = Label(label_frame, text="Episodes")
# L_category = Label(label_frame, text="Category")
# L_priority = Label(label_frame, text="Priority Score")
# 
# L_name.pack()
# L_seasons.pack()
# L_episodes.pack()
# L_category.pack()
# L_priority.pack()
# 
# v_name = StringVar()
# v_seasons = DoubleVar()
# v_episodes = DoubleVar()
# v_category = StringVar()
# v_priority = DoubleVar()
# 
# e1NameVar = StringVar()
# nameVar.set('Its Always Sunny')
# e_name = Entry(table_frame, textvariable=e1NameVar)
# 
# b1 = Button(table_frame, text='Save', command=calc_amt)
# b2 = Button(table_frame, text='Pick Random Show', command=calc_amt)
b3 = Button(entries_frame, text = 'Add New Show', command=add_show)
b3.pack(side=BOTTOM)
b4 = Button(entries_frame, text = 'Print', command=print_shows)
b4.pack()

init_labels()

mainloop( )