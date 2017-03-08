#import the tkinter module
import Tkinter
from tkFileDialog import askopenfilename
from PIL import Image, ImageTk

window=Tkinter.Tk()

window.title("Photo Studio")
window.geometry("1200x800")
window.configure(background="dim gray")
#window.resizable(False, False)


def openPic():
	#Tk().widthdraw()
	file= askopenfilename()
	return file


window.wm_iconbitmap('favicon.ico')
buttons=[]

lbl =Tkinter.Label(window, text="\t\t\tPhoto Studio", fg="ghost white" ,bg="dim gray")
lbl.place(relheight=0.02, relwidth=0.9)

Pick_photo=Tkinter.Button(window, text="Pick a photo to begin", command= openPic)
Pick_photo.place(relx=0.45, rely=0.4)


#Empty=Tkinter.Button(window,bg="dim gray", bd=0, activebackground="dim gray")


photo= Image.open("eraser.png")
photo_image=ImageTk.PhotoImage(photo)
E=Tkinter.Button(window, image=photo_image, bg="dim gray", bd=0, activebackground="black")
buttons.append(E)

#E.place(x=100,y=100)



ph= Image.open("filter.png")
photo_ima=ImageTk.PhotoImage(ph)
F=Tkinter.Button(window, image=photo_ima, bg="dim gray", bd=0, activebackground="black")
buttons.append(F)

#F.grid(column=5, row=2, pady=100)

p= Image.open("sticker.png")
photo_im=ImageTk.PhotoImage(p)
S=Tkinter.Button(window, image=photo_im, bg="dim gray", bd=0, activebackground="black")
#S.grid(column=6, row=2,pady=100, )
buttons.append(S)



pho= Image.open("crop.png")
photo_i=ImageTk.PhotoImage(pho)
C=Tkinter.Button(window, image=photo_i, bg="dim gray", bd=0, activebackground="black")
#C.grid(column=7, row=2, pady=100, padx=25)
buttons.append(C)

for i in range(4):
	buttons[i].place(relx=0.2+i*0.15, rely=0.75)



window.mainloop()
