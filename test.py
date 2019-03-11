import tkinter
import time

def ende():
    main.destroy()
    
main=tkinter.Tk()
main.title("Programm")

content=time.asctime()
fr=tkinter.Frame(main, width=300, height=200)
tx=tkinter.Label(main, text=content)
button1=tkinter.Button(main,text="Ende", command=ende)
#button2=tkinter.button(main,text="Refresh", command=refresh)

def refresh():
    content=time.asctime()

tx.pack()
fr.pack()
button1.pack()
#button2.pack()

main.mainloop()
