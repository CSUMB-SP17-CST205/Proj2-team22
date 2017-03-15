from Tkinter import *
from PIL import Image, ImageTk
from tkFileDialog import askopenfilename


class Artapp():

    artOption = ["line", "pencil"]

    drawingTool = "line"

    width = 0

    height = 0

    filename = ""

    color = "black"

    index = 0

    colorOptions = ["red" , "green", "blue", "black", "blue", "cyan", "yellow", "magenta"]

    leftMouseClick = "no"

    x_pos, y_pos = None, None

    x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None,None, None
    # Default Constructor
    def __init__(self, root):

        self.filename = askopenfilename()
        self.img = Image.open(self.filename)
        self.width, self.height = self.img.size
        self.TEST = ImageTk.PhotoImage(Image.open(self.filename))

        self.platform = Canvas(root,width = self.width, height = self.height)
        self.platform.pack()
        self.platform.create_image(0,0, image = self.TEST, anchor = NW)
        self.platform.bind("<Motion>", self.motion)
        # Left Button Clicks
        self.platform.bind("<ButtonPress-1>", self.mouseTriggerd)
        # Left Button Release
        self.platform.bind("<ButtonRelease-1>", self.mouseStable)

    def mouseTriggerd(self, event = None):
        self.leftMouseClick = "yes"
        self.x1_line_pt = event.x
        self.y1_line_pt = event.y


    def mouseStable(self, event = None):
        self.leftMouseClick = "no"
        self.x_pos = None
        self.y_pos = None

        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if self.drawingTool == "line":
            self.line_draw(event)

    def motion(self, event = None):

        if(self.drawingTool == "pencil"):
            self.pencil_draw(event)


    def pencil_draw(self, event = None):
        if(self.leftMouseClick == "yes"):
            if (self.x_pos is not None and self.y_pos is not None):
                event.widget.create_line(self.x_pos, self.y_pos, event.x, event.y, smooth = True, fill = self.color)

            self.x_pos = event.x
            self.y_pos = event.y
    def line_draw(self, event = None):
        if(None not in (self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt)):
            event.widget.create_line(self.x1_line_pt, self.y1_line_pt, self.x2_line_pt, self.y2_line_pt, smooth = True, fill = self.color)


    def red(self):
        self.color = "red"

    def green(self):
        self.color = "green"

    def blue(self):
        self.color = "blue"

    def black(self):
        self.color = "black"

    def cyan(self):
        self.color = "cyan"

    def yellow(self):
        self.color = "yellow"

    def line(self):
        self.drawingTool = "line"

    def freeDraw(self):
        self.drawingTool = "pencil"
    def clear(self):
        self.platform.delete("all")
        self.platform.create_image(0,0, image = self.TEST, anchor = NW)
    def save(self):
        self.platform.postscript(file="/Users/marcoaguilera/Desktop/ARTPostScript.eps")
        self.filename = "/Users/marcoaguilera/Desktop/ARTPostScript.eps"
        self.img = Image.open("/Users/marcoaguilera/Desktop/ARTPostScript.eps")
        self.img.save("ARTPostScript.png")



root = Tk()
artapp = Artapp(root)



Button(root, text = "Red", command = artapp.red).pack(side = "left")
Button(root, text = "Green", command = artapp.green).pack(side = "left")
Button(root, text = "Blue", command = artapp.blue).pack(side = "left")
Button(root, text = "Black", command = artapp.black).pack(side = "left")
Button(root, text = "Cyan", command = artapp.cyan).pack(side = "left")
Button(root, text = "Yellow", command = artapp.yellow).pack(side = "left")
Button(root, text = "Line Draw", command = artapp.line).pack(side = "top")
Button(root, text = "Free Draw", command = artapp.freeDraw).pack(side = "top")
Button(root, text = "CLEAR", command = artapp.clear).pack(side = "top")
Button(root, text = "SAVE", command = artapp.save).pack(side = "top")
root.mainloop()
