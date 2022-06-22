# Let's make a save button.
import tkinter
import tkinter as tk

root = tk.Tk()
root.geometry=("250x250")

#var 1 = mins
var1 = tk.stringVar(root)
var1.set("Choose an Option")


OptionMenu =
#var 2 = hours


tasklist = []
tskmin =
tskhr =
taskresult =

def storedisplay():
    tskmin = var2.get()
    tskhr = var1.get()
    taskresult = taskentry.get()

    tasklist.append(taskresult)
    tasklist.append(tskhr)
    tasklist.append(tskmin)
    # the tasks follow each other in vertical order
    output = " ".join(tasklist)


    rturnlabel = tk.Label(root, text=output)
    rturnlabel.grid(row=15, column=3)


SaveButton = tk.Button(
    text="Save",
    padx=10,
    pady=5,
    command= storedisplay
)

SaveButton.place(x=75, y=75)

#binding Enter key to storing
keypress = root.bind('<Return>', storedisplay)

root.mainloop()




#BELOW IS TEMPORARY STUFF
#TEMP ENVIRONMENT BELOW
#-----------------------------
#
#SaveButton.place(height= 50, width= 50, relx= .4, rely=.5)
#
#
#
