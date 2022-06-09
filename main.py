# this is a project to make a clock and put it on an interface

import time
import tkinter as tk

# step one, create the interface after creating the conception of time.

def displaytime():
    current = time.ctime()
    clock["text"] = current
    root.after(1000, displaytime)
#we have time as a concept, make a window and display it

root = tk.Tk()

#infos about the main window 'root'
root.title("MyTasks")
root.geometry('400x400')

#creation of the label for the question
tsknametl = tk.Label(root, text="What tasks do you have to do?")
tsknametl.grid(row=2, column=3)

#Our clock is now showing the time
clock = tk.Label(root,)
clock.grid(row=0, column=0)
displaytime()

#Making the entry for the question
taskentry = tk.Entry(root)
taskentry.grid(row=3, column=3)

#our list/dictionaries going to be used later
tasklist = []


#labels for the time question as well as the min and hour labels
tasktime = tk.Label(root, text="When will you do it")
tasktime.grid(row=5, column=3)

hrlabel = tk.Label(root, text="Hour:")
hrlabel.grid(row=6, column=2)

minlabel = tk.Label(root, text="Minutes:")
minlabel.grid(row=7,column=2)

#making a list going to be used for the choices of hour in the option menu
timechoicehr = []
for n in range(24):
    list.append(timechoicehr, str(n)+" h")

#making the option menu
var1 = tk.StringVar(root)
var1.set("choose an option")
optnmenuhr = tk.OptionMenu(root,var1, *timechoicehr)
optnmenuhr.grid(row=6, column=3)

#a list used for the choices of mins in option menu
timechoicemin = []
for i in range(60):
    list.append(timechoicemin, str(i))

#the option menu for mins
var2 = tk.StringVar(root)
var2.set("choose an option")
optnmenumin = tk.OptionMenu(root, var2, *timechoicemin)
optnmenumin.grid(row=7, column=3)



#make a function that is going to keep the results and display them
def storedisplay(keypress):


    tskmin = var2.get()
    tskhr = var1.get()
    taskresult = taskentry.get()

    tasklist.append(taskresult)
    tasklist.append(tskhr)
    tasklist.append(tskmin)
    # the tasks follow each other in vertical order
    output = " ".join(tasklist) + "\n"


    rturnlabel = tk.Label(root, text=output)
    rturnlabel.grid(row=15, column=3)


# showing the results of the function storing


#binding Enter key to storing
keypress = root.bind('<Return>', storedisplay)




#Expression label
youhave = tk.Label(root, text="Here are your tasks for the day!")
youhave.grid(row=14, column=3)



#make a possibility to remove a task meaning erasing a label
#do a memory of the tasks so that the app keeps memory of a task when closed
#A save button (Val), of course(clem)
#a change so that github stop fucking around...

root.mainloop()


