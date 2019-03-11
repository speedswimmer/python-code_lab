#clock
import time
import tkinter

def tick(time1=''):
    #get the current time from the PC
    time2=time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

    clock.after(500, tick)

main = tkinter.Tk()
clock=tkinter.Label(main, font=("arial", 20, "bold"), bg="green")
clock.pack(fill="both",expand=1)
tick()

main.mainloop()

        
