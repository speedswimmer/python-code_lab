from tkinter import*
from tkinter import ttk
#import picamera

root = Tk()
root.title("Photobox")
root.minsize(250,150)

def callback():
    t1.delete("1.0", "end")
    t1.insert("1.0", res.get())

# Button Widget
button = ttk.Button(root, text="Click me!", command = callback)

# Text Widget for info output
t1 = Text(root, width = 20, height=1)
t1.config(wrap = 'word')

# Radiobutton

label = ttk.LabelFrame(root, text='Resolution:', width = 120, height = 100)
label.config(padding=(10,10))
label.pack()

res = StringVar()
res.set = 'Nothing'
check1 = ttk.Radiobutton(label, text ='640 x 480', variable = res, value = '640x480').pack()
check2 = ttk.Radiobutton(label, text = '1024 x 768', variable = res, value = '1024x768').pack()
check3 = ttk.Radiobutton(label, text = '1280 x 960', variable = res, value = '1280x960').pack()

t1.pack()
button.pack()

root.mainloop()

