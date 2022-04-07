from tkinter import *
import backend
from fileread import createLayout
from fileread import findrc





def main():
    root = Tk()
##    root.iconbitmap('Logo.ico')
    root.title('PacMan Shortest Path Finding')
    root.geometry('1190x780')
    root.config(bg='white')
    #root.resizable(width=FALSE, height=FALSE)
    count = 0                                           # for identifying each button/vertex and passing unique parameters
    button_list = []                                    # stores button created during runtime

    frame_up=LabelFrame(root,text='Options',highlightbackground='#00154F', bg ='white', fg='#00154F', highlightthickness=4,font=('Helvetica', 18, 'bold'))                                   # stores button created during runtime)

    frame_down = LabelFrame(root,text='Path',highlightbackground='#00154F',fg='#00154F',highlightthickness=4,font=('Helvetica', 18, 'bold'))  

    frame_up.pack(side=LEFT) 

    frame_up.place(x=30,y=30)

    frame_down.pack()

    frame_down.place(x=200,y=30)


    # frame_up = LabelFrame(root, text='options')
    # frame_down = LabelFrame(root, text='path')
    # frame_up.pack()
    # frame_down.pack()
    global supply_mode                                  # for differentiating b/w starting, ending & obstacles point
    supply_mode = 0
    global src                                          # src is starting point
    src = 0
    global obstacle_list                                # stores the obstacles when supply_mode is 2
    obstacle_list = []
    global dest                                         # final destination variable
    dest = 1000

    global x
    x = 'mediumSafeSearch'   ########## Layout Selection
    global row
    global col

    list1 = [0,1]
    list1 = findrc(x)

    row = list1[0]
    col = list1[1]

    #print (list1)

    def button_mode(mode):                              # input field by user starting/obstacles/destination point
        global supply_mode
        supply_mode = mode
        # print(supply_mode)

    def button_click(but_no):                           # clicked buttons in path
        #print(but_no)
        global supply_mode
        if supply_mode == 1:                                # for starting point when supply_mode = 1
            button_list[but_no].config(bg='yellow')
            global src
            src = but_no
            start_button['state'] = DISABLED
            supply_mode = 0
        if supply_mode == 2:                                # for obstacles      when supply_mode = 2
            button_list[but_no].config(bg='#2F4F4F')
            global obstacle_list
            obstacle_list.append(but_no)
        if supply_mode == 3:                                # for destination    when supply_mode = 3
            button_list[but_no].config(bg='red')
            global dest
            dest=but_no
            destination_button['state'] = DISABLED
            supply_mode = 0

    start_button = Button(frame_up, text='Select Start Point',font=('arial',10,'bold'),bg='#808080', fg='white',relief=SUNKEN, command=lambda: button_mode(1))
    obstacle_button = Button(frame_up, text='Select Obstacles',font=('arial',10,'bold'),bg='#808080', fg='white',relief=SUNKEN, command=lambda: button_mode(2))
    destination_button = Button(frame_up, text='Select Destination',font=('arial',10,'bold'),bg='#808080', fg='white',relief=SUNKEN, command=lambda: button_mode(3))

    start_button.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
    obstacle_button.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
    destination_button.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

    for i in range(row):
        for j in range(col):
            button_list.append(Button(frame_down, text='', padx=10, pady=7, command=lambda x=count: button_click(x)))
            button_list[count].grid(row=i, column=j, sticky="ew")
            count += 1

    def solution():                                         # backend script is called
        parent = backend.backened(src, obstacle_list, dest)
        for value in parent:
            button_list[value].config(bg='#00c5ff')         # path color is turned blue
        button_list[src].config(bg='#ffe525')               # starting pt color is turned back yellow

    go_button = Button(frame_up, text='Go',font=('arial',10,'bold'),bg='#808080', fg='white',relief=SUNKEN,command=solution)
    go_button.grid(row=3, column=1, padx=10, pady=5)

    def restart():
        root.destroy()
        main()
        
    restart_button = Button(frame_up, text='Restart',font=('arial',10,'bold'),bg='#808080', fg='white',relief=SUNKEN, command=restart)
    restart_button.grid(row=4, column=1, padx=10, pady=5)

    def level_tut():
        a= createLayout(x)

        already_generated_obstacle = []
        already_generated_obstacle = a
        
        global obstacle_list
        obstacle_list = already_generated_obstacle
        for every in already_generated_obstacle:
            button_list[every].config(bg='#2F4F4F')
            button_list[every].config(state = DISABLED)

    # level_button = Button(frame_up, text='Maze', command=level_tut)
    level_button = Button(frame_up, text='Layout',font=('arial',10,'bold'),bg='#808080', fg='white',relief=SUNKEN,command=level_tut)
    level_button.grid(row=5, column=1, padx=10, pady=5)

    mainloop()
####    
main()
