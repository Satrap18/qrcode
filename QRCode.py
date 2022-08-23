#Start 1:13 AM 11/9/2021
#-----import library----------------#
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import qrcode
#-------------Create page and title-page-size-------#
window = Tk()
window.title("QRCode!-Satrap")
window.resizable(width=False,height=False)
#------------------------------------------------#
def ViewHelp():
    Toplevel = Tk()
    Toplevel.resizable(False,False)
    Toplevel.title("QRCode-Help")
    Label(Toplevel,text='First Enter To Create QRCode And Enter To Create',font="blod").pack()
    Label(Toplevel,text='Secend Save File',font="blod").pack()

def show_info():
    messagebox.showinfo("programmer","Satrap18\nversion 1.0.0")

def QRCode():
    data = e1.get()
    img = qrcode.make(data)
    file_path = filedialog.asksaveasfilename(defaultextension='.jpg',title="Save-Satrap",filetypes=[("png",".png"),("jpg",".jpg"),("Html",".Html"),("SVG",".svg")])
    img.save(file_path)

def Exit():
    if messagebox.askokcancel("Exit","Do you really want to Exit?"):
        window.destroy()
        window.protocol('WM_DELETE_WINDOW', Exit)

window.protocol('WM_DELETE_WINDOW', Exit)
#----------Create menu---------------------#
menubar = Menu(window)

filemenu = Menu(menubar,tearoff=0)
filemenu1 = Menu(menubar,tearoff=0)
#filemenu2 = Menu(menubar,tearoff=0)

menubar.add_cascade(label="File",menu=filemenu)
menubar.add_cascade(label="Help",menu=filemenu1)


filemenu.add_command(label="Exit",command=Exit,accelerator='Alt+F4')
filemenu1.add_command(label="ViewHelp",command=ViewHelp,accelerator='F1')
filemenu1.add_command(label="AboutQRCode",command=show_info)


window.config(menu=menubar)
#------------Create Canvas----------------------------------------#
cw = Canvas(window,width=300,height=150)
cw.pack()

cw.create_text(150,100,text="QRCode!",font=("Bold",30))
cw.create_text(90,75,text="Satrap")
#-----------Create Label-------------------------------------------#
lbl = Label(window,text="Enter QRCode Name")
lbl.pack()
#------------Create Entry-------------------------------------------#
e1 = Entry(window)
e1.pack()
#--------------------------------------Button-----------------------#
ttk.Button(window,text='Create',command=QRCode).pack()
#--------------------------------------------------------------------#
window.mainloop()
