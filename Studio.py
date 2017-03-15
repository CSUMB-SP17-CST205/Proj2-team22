from Tkinter import *
from tkMessageBox import *
from tkFileDialog import askopenfilename
import PIL
from PIL import Image, ImageTk,ImageFilter
from resizeimage import resizeimage
import cv2 as cv2
import numpy

class App:
	def __init__(self, window):
		
		window.title("Photo Studio")
		
		window.	wm_iconbitmap('favicon.ico')
		window.geometry("1200x900")
		self.refPt = []
		self.cropping = False
		self.sel_rect_endpoint = []
		#self.panel= Label(window,text="DOES THIS SHOW?", fg="white",bg="white")
		#self.panel.place(relx=0.6,rely=0.6)
		window.configure(background="dim gray")
		self.titletxt=Label(window, text = "\t\t\tPhoto Studio", fg="ghost white" ,bg="dim gray")
		self.titletxt.grid()
		self.titletxt.place(relheight=0.02, relwidth=0.9)

		self.file=None
		self.Pick_photo=Button(window, text="Pick a photo to begin", command= self.openPic)
		self.Pick_photo.place(relx=0.45, rely=0.4)
		#self.init_buttons()
		
		self.buttons=[]
		photo= Image.open("eraser.png")
		self.photo_image=ImageTk.PhotoImage(photo)
		E= Button(window, image=self.photo_image, bg="dim gray", bd=0, activebackground="black", command= self.reset)
		self.buttons.append(E)

		#E.place(x=100,y=100)
		


		ph= Image.open("filter.png")
		self.photo_ima=ImageTk.PhotoImage(ph)
		F= Button(window, image=self.photo_ima, bg="dim gray", bd=0, activebackground="black", command=self.picFilter)
		self.buttons.append(F)

		#F.grid(column=5, row=2, pady=100)

		p= Image.open("sticker.png")
		self.photo_im=ImageTk.PhotoImage(p)
		S= Button(window, image=self.photo_im, bg="dim gray", bd=0, activebackground="black", command=self.draw)
		#S.grid(column=6, row=2,pady=100, )
		self.buttons.append(S)



		pho= Image.open("crop.png")
		self.photo_i=ImageTk.PhotoImage(pho)
		C= Button(window, image=self.photo_i, bg="dim gray", bd=0, activebackground="black",command=self.cropImg)
		#C.grid(column=7, row=2, pady=100, padx=25)
		self.buttons.append(C)
		
		
		
		for i in range(4):
			self.buttons[i].place(relx=0.2+i*0.15, rely=0.81)
		

		

	

	def openPic(self):
		#Tk().widthdraw()
		self.file= askopenfilename()
		#print self.file
		if(self.file == ''):
			self.file=None
			return
		self.Pick_photo.place_forget()
		if self.file is not None:
			self.saveButton=Button(root,text="Save Picture",command=self.savePIC)
			self.newButton=Button(root,text="New Picture",command=self.openPic)
			self.saveButton.place(relx=0.8, rely=0.9)
			self.newButton.place(relx=0.8, rely=0.85)
			self.img=Image.open(self.file)
			self.saveOriginal()
			self.showPic()
	def saveOriginal(self):
		self.original=self.img
			
	def picFilter(self):
		if(self.file == None):
			return
		self.buttons[1].config(state="disabled")
		self.fFrame=Frame(root)
		self.blur=Button (self.fFrame, text="Blur",command=self.bluryPIC)
		self.blur.pack(side=LEFT)
		self.emboss=Button (self.fFrame, text="Emboss", command=self.embossPIC)
		self.emboss.pack(side=LEFT)
		self.contour=Button(self.fFrame,text="Contour",command=self.contourPIC)
		self.contour.pack(side=LEFT)
		self.detail=Button(self.fFrame,text="Detail", command =self.detailPIC)
		self.detail.pack(side=LEFT)
		self.edge=Button(self.fFrame,text="Edge", command =self.edge_enhancePIC)
		self.edge.pack(side=LEFT)
		self.smooth=Button(self.fFrame,text="Smooth",command = self.smoothPIC)
		self.smooth.pack(side=LEFT)
		self.sharpen=Button(self.fFrame,text="Sharpen", command= self.sharpenPIC)
		self.sharpen.pack(side=LEFT)
		self.quitFrame=Button(self.fFrame, text="Exit Filters", command = self.quit)
		self.quitFrame.pack(side=LEFT)
		
		
		self.fFrame.place(relx=0.275,rely=0.8)
	def quit(self):
		self.fFrame.place_forget()
		self.buttons[1].config(state="normal")
		
	
	def bluryPIC(self):
		self.img = self.img.filter(ImageFilter.BLUR)
		self.Cimg = ImageTk.PhotoImage(self.img)
		
		self.pic.create_image(0,0,image=self.Cimg, anchor='nw')
		
	def contourPIC(self):
		self.img = self.img.filter(ImageFilter.CONTOUR)
		self.Cimg = ImageTk.PhotoImage(self.img)
		
		self.pic.create_image(0,0,image=self.Cimg, anchor='nw')
		
	def detailPIC(self):
		self.img = self.img.filter(ImageFilter.DETAIL)
		self.Cimg = ImageTk.PhotoImage(self.img)
		
		self.pic.create_image(0,0,image=self.Cimg, anchor='nw')
		
	def edge_enhancePIC(self):
		self.img = self.img.filter(ImageFilter.EDGE_ENHANCE_MORE)
		self.Cimg = ImageTk.PhotoImage(self.img)
		
		self.pic.create_image(0,0,image=self.Cimg, anchor='nw')
	
	def embossPIC(self):
		self.img = self.img.filter(ImageFilter.EMBOSS)
		self.Cimg = ImageTk.PhotoImage(self.img)
		
		self.pic.create_image(0,0,image=self.Cimg, anchor='nw')
		
	def smoothPIC(self):
		self.img = self.img.filter(ImageFilter.SMOOTH)
		self.Cimg = ImageTk.PhotoImage(self.img)
		
		self.pic.create_image(0,0,image=self.Cimg, anchor='nw')
	def sharpenPIC(self):
		self.img = self.img.filter(ImageFilter.SHARPEN)
		self.Cimg = ImageTk.PhotoImage(self.img)
		
		self.pic.create_image(0,0,image=self.Cimg, anchor='nw')
	def reset(self):
		if(self.file == None):
			return
		self.img = self.original
		self.showPic()
		
	def savePIC(self):
		self.toplevel=Toplevel()
		self.toplevel.wm_iconbitmap('favicon.ico')
		label1=Label(self.toplevel, text="What would you like this to be called? \nEnter the picture name and .extension")
		label1.pack()
		self.entry=Entry(self.toplevel)
		self.entry.pack()
		self.entry.focus_set()
		enter=Button(self.toplevel, text="Save",command = self.saving)
		enter.pack()
	def saving(self):
		path=self.entry.get()
		try:
			self.img.save(path)
		except:
			print "BAD!"
		self.toplevel.destroy()
		
		
		
		
			
	def showPic(self):
		
		basewidth = 400
		wpercent = (basewidth/float(self.img.size[0]))
		hsize = int((float(self.img.size[1])*float(wpercent)))
		self.img = resizeimage.resize_contain(self.img, [650,650])
		#print "DID YOU GET HERE?"
		self.pic=Canvas(root, width=650,height=650)
		
		self.Cimg = ImageTk.PhotoImage(self.img)
		
		self.pic.create_image(0,0,image=self.Cimg, anchor='nw')
		self.pic.place(relx=.25,rely=.02)
		
		"""
		
		self.panel = Label(root, image = self.img)
		self.panel.pack()
		"""
	def draw(self):
		showinfo('Sorry!','This functionality has not yet been implemented.\nIf you would like to speed up development,\nplease donate at lvalencia@csumb.edu')
	def cropImg(self):
		if(self.file == None):
			return
		showinfo('NOTE','Click and hold to crop.\nPress \'C\' to crop. \'R\' to reset.\nNOTE: Please crop starting from left to right.')
		self.cropImage = numpy.array(self.img)
		self.cropImage= cv2.cvtColor(self.cropImage, cv2.COLOR_BGR2RGB)
		self.clone = self.cropImage.copy()
		cv2.namedWindow("Cropping")
		cv2.setMouseCallback("Cropping", self.click_and_crop)
		
		while True:
			# display the image and wait for a keypress
			if not self.cropping:
				
				cv2.imshow('Cropping', self.cropImage)
			elif self.cropping and self.sel_rect_endpoint:
				
				rect_cpy = self.cropImage.copy()
				#roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
				cv2.rectangle(rect_cpy, self.refPt[0], self.sel_rect_endpoint[0], (0, 255, 0), 1)
				cv2.imshow('Cropping', rect_cpy)
			key = cv2.waitKey(1) & 0xFF

			# if the 'r' key is pressed, reset the cropping region
			if key == ord("r"):
				
				self.cropImage = self.clone.copy()
				cv2.setMouseCallback("Cropping", self.click_and_crop)

			# if the 'c' key is pressed, break from the loop
			elif key == ord("c"):
				
				cv2.setMouseCallback("Cropping",self.dummy)
				break


		# if there are two reference points, then crop the region of interest
		# from teh image and display it
		if len(self.refPt) == 2:
			self.roi = self.clone[self.refPt[0][1]:self.refPt[1][1], self.refPt[0][0]:self.refPt[1][0]]
			#cv2.imshow("ROI", self.roi)
			
			if self.roi== None:
				cv2.destroyAllWindows()

			self.roi=cv2.cvtColor(self.roi,cv2.COLOR_BGR2RGB)
			self.img=Image.fromarray(self.roi)
			#self.img.save("cropped.png")
			#print "got here?"
			

		# close all open windows
		
		self.showPic()
		cv2.destroyAllWindows()
	
	def dummy(self,event, x, y, flags, param):
		print ""

	def click_and_crop(self,event, x, y, flags, param):
		
		
		# grab references to the global variables
		

		# if the left mouse button was clicked, record the starting
		# (x, y) coordinates and indicate that cropping is being
		# performed
		if event == cv2.EVENT_LBUTTONDOWN:
			#print "BUTTON DOWN"
			self.refPt = [(x, y)]
			self.ix=x
			self.iy=y
			self.cropping = True

		# check to see if the left mouse button was released
		elif event == cv2.EVENT_LBUTTONUP:
			#print "BUTTON UP"
			# record the ending (x, y) coordinates and indicate that
			# the cropping operation is finished
			self.refPt.append((x, y))
			
			self.cropping = False
			cv2.setMouseCallback("Cropping",self.dummy)
			#self.refPt = [(min(self.ix,x), min(self.iy,y)), (abs(self.ix-x), abs(self.iy-y)) ]
			
			# draw a rectangle around the region of interest
			cv2.rectangle(self.cropImage, self.refPt[0], self.refPt[1], (0, 255, 0), 2)
			cv2.imshow("Cropping", self.cropImage)
		elif event == cv2.EVENT_MOUSEMOVE and self.cropping:
			self.sel_rect_endpoint = [(x, y)]
				

root=Tk()

app= App(root)

root.mainloop()