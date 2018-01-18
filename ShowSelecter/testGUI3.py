'''Created on Jan 13, 2018, @author: daneaadland'''


from tkinter import *

label_list = ['Name', 'Seasons', 'Episodes', 'Category', 'Priority Score']
entries_list = []
entries_dict = {} # this is not being used yet

name, seasons, episodes, category, priority = 0, 1, 2, 3, 4

#---------------------FRAMES----------------------------------
root = Tk()
label_frame = Frame(root)
entries_frame = Frame(root)
button_frame = Frame(root)

label_frame.pack(expand=True, fill='both')
entries_frame.pack()
button_frame.pack()

#--------------------FUNCTIONS--------------------------------
def init_labels():
    for index, col in enumerate(label_list):
        col_label = Label(label_frame, text=col, padx=65)
        col_label.grid(row=0, column=index, sticky=N+S+E+W)

def add_show():
    global entries_list
    new_frame = Frame(entries_frame)
    new_frame.pack()
    new_list = []    
    for entry in range(len(label_list)):
        v_entry = StringVar()
        new_entry = Entry(new_frame, textvariable=v_entry)
        new_entry.pack(side=LEFT)
        new_list.append(v_entry)
    entries_list.append(new_list)
        
def print_shows():
    print('size of list is: ', len(entries_list))
    for entry in entries_list:
        for field in entry:
            print(field.get())           
    print(entries_list[2][priority].get())
    get_priority_scores()

#change this to calculate
def get_priority_scores():
    for scores in entries_list:
        print(scores[priority].get())

        
def pick_random_show():
    p_scores = get_p_score_list()
    p_scores = list(map(int, p_scores))
    p_scores.sort(reverse=True)
    choice = p_scores[0]
    print(choice)


def get_p_score_list():   
    
    p_score_list = []
    for entry in entries_list:
        for index, field in enumerate(entry):
            if index == get_p_score_index(): 
                p_score_list.append(field.get())    
    return p_score_list
    
    
#     p_scores_list = []
#     
#     p_score_index = get_p_score_index()
#     shows_dict = convert_to_dict()
#     for key in shows_dict:
#         values = shows_dict.get(key)
#         p_scores_list.append(values[p_score_index])
#     return p_scores_list
# 
# def convert_to_dict():
#     for index, entry in enumerate(entries_list):
#         name = str(entry[0].get())
#         items = []
#         for index2, field in enumerate(entries_list[index]):
#             if index2 != 0:
#                 items.append(str(field.get()))
#         new_dict = {name: items}
#         return new_dict
        

def get_p_score_index():
    for index, value in enumerate(label_list):
        if value == 'Priority Score':
            return index

#-----------------BUTTONS------------------------------------------------------------------
b_add = Button(button_frame, text = 'Add New Show', command=add_show)
b_print = Button(button_frame, text = 'Print', command=print_shows)
b_test_random = Button(button_frame, text = 'Test Random', command=pick_random_show)
# b1 = Button(table_frame, text='Save', command=calc_amt)
# b2 = Button(table_frame, text='Pick Random Show', command=calc_amt)

b_add.pack(side=LEFT)
b_print.pack(side=LEFT)
b_test_random.pack(side=LEFT)

#-------------------MAINLOOP-------------------------------------------------------------
init_labels()
mainloop( )