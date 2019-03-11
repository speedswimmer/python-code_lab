import tkinter
import time


main=tkinter.Tk()
main.title("Leeres Programm")

#Funktion zum aktualisieren der Zeitangabe
def clock():
    acttime=time.strftime("%H:%M:%S")
    main.title("Leeres Programm - {}".format(acttime))
        
def callback_1(event):
    d1.insert("end","Linker Maus-Button wurde gedrückt!")
    d1.insert("end","\n")

def callback_2(event):
    d1.insert("end","Rechter Maus-Button wurde gedrückt!")
    new_line()

def callback_3(event):
    d1.insert("end","Enter wurde gedrückt")
    new_line()

def clean():
    d1.delete(1.0,"end")

def new_line():
    d1.insert("end","\n")

def refresh(time1=''):
    time2=time.strftime("%H:%M:%S")
    if time2 != time1:
        time1 = time2
        label_clock.config(text=time2)

        clock.after(200, refresh)

#Inhalt - aktueller Tag etc.
weekday = time.strftime("%A")
month=time.strftime("%B")
day=time.strftime("%d")

content=("Today is {}!".format(weekday))
datum=("{}. {}".format(day,month))

#GUI Widgets
d1=tkinter.Text(main)
d1.config(state="normal", width=50, height=10, bg="#d3e5ff", fg="#4c4c4c", relief="sunken") #allows that text is inserted and deleted
d1.insert("end",content)
new_line()
d1.insert("end",datum)
new_line()

d1.grid(row=0,columnspan=4)
d1.bind("<Button-1>", callback_1)
d1.bind("<Button-3>", callback_2)

b1=tkinter.Button(main, text = "End", command=main.destroy).grid(row=1, column=0)
b2=tkinter.Button(main, text = "Refresh", command=clock).grid(row=1, column=1)
b3=tkinter.Button(main, text = "Clean",command=clean).grid(row=1, column=2)
label_clock=tkinter.Label(main, text=time.strftime("%H:%M:%S"),bg="#4286f4", fg="#ffffff", relief="ridge").grid(row=1, column=3)
refresh()
                    
main.mainloop()

