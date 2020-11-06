from threading import *
import webbrowser
from tkinter import *
from keyboard import *
url=''
def savevid():
    global url
    dlink=url.get()
    link=dlink
    download=link[:12]+"ss"+link[12:]

    webbrowser.open(download)

root=Tk()
lbl=Label(root, text='Download Any Video from Youtube',padx=20)
lbl.grid(row=0, column=2, pady=10)
down=Label(root,text='Enter Url: ')
down.grid(row=1, column=1, padx=(0,5))
url=Entry(root, width=30)
url.grid(row=1, column=2)
t=Thread(target=savevid)
btn=Button(root, text='Download', font='Digital-7 15 bold',command=savevid)
btn.grid(row=2, column=2, pady=30)
add_hotkey('Enter',savevid)
root.geometry('450x300')
root.mainloop()