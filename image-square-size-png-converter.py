from tkinter import *
from tkinter import filedialog as fd
import os
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

win = Tk()

win.geometry('500x500')
win.resizable(False, False)
win.title('Image Square Size')

file = ""
txt = StringVar()
width = IntVar()
height = IntVar()

def checkSize(wdth, hgth):
	if wdth <= 0  or hgth <= 0:
		messagebox.showerror("Size Error", "Please Provide width and Height")
	elif wdth != hgth:
		messagebox.showerror("Square Error", "Please Provide Same Value for Width and Height")

def openFile():
	global file
	file = fd.askopenfilename(initialdir=os.path.normpath("C://Users/Shaik/OneDrive/Pictures/Screenshots"), title="Example", filetypes =(("PNG", "*.png"),("JPG", "*.jpg"),("All Files","*.*")))
	# print(file)
	txt.set(file)
	try:
		img = Image.open(file)
		# img.show()
		img = img.resize((300,300))
		showImg = ImageTk.PhotoImage(img)
		imgLbl = Label(image=showImg)
		imgLbl.image = showImg
		imgLbl.place(y=60,x=85)
	except:
		messagebox.showerror("File Error", "Please Select a File")

def resizeFile():
	global file
	wdth = width.get()
	hgt = height.get()
	try:
		img = Image.open(file)
	except:
		messagebox.showerror("File Error", "Please Select a File")
	newSize = (wdth, hgt)
	state = False
	if file:
		try:
			img = img.resize(newSize)
			state = True
		except:
			checkSize(wdth,hgt)
	if state:
		newPath = os.path.dirname(os.path.abspath(file))
		newPath = os.path.join(newPath,'ResizeImage')
		fileName = os.path.join(newPath, os.path.basename(file))
		# print(fileName)
		if not os.path.exists(newPath):
			try:
				os.makedirs(newPath)
			except:
				messagebox.showerror("Folder Error", "Folder Creation Failed")
			# print('hello')
		try:
			img.save(fileName)
			messagebox.showinfo("Successfull", "Operation Done Successfully")
			width.set(0)
			height.set(0)
		except:
			messagebox.showerror("Error", "Unknown error")

def convertToPng():
	global file
	wdth = width.get()
	hgt = height.get()
	try:
		img = Image.open(file)
	except:
		messagebox.showerror("File Error", "Please Select a File")
	newSize = (wdth, hgt)
	state = False
	if file:
		try:
			img = img.resize(newSize)
			state = True
		except:
			checkSize(wdth,hgt)
	if state:
		newPath = os.path.dirname(os.path.abspath(file))
		newPath = os.path.join(newPath,'ResizeImage')
		fileName = os.path.basename(file).split('.')[-2] + '.png'
		filePath = os.path.join(newPath, fileName)
		# print(img)
		if not os.path.exists(newPath):
			try:
				os.makedirs(newPath)
			except:
				messagebox.showerror("Folder Error", "Folder Creation Failed")
			# print('hello')
		try:
			img.save(filePath)
			messagebox.showinfo("Successfull", "Operation Done Successfully")
			width.set(0)
			height.set(0)
		except:
			messagebox.showerror("Error", "Unknown error")

lbl = Label(win, text='Select Your Image:')
lbl.place(x=20, y=20)

widthLbl = Label(win, text='Enter New Width: ')
widthLbl.place(x=20, y=390)

heightLbl = Label(win, text='Enter New Height: ')
heightLbl.place(x=250, y=390)

# print(file)
entryBox = ttk.Entry(win, textvariable=txt)
entryBox.place(y=20, x=130)

widthBox = ttk.Entry(win, textvariable=width)
widthBox.place(y=390, x=120)

heightBox = ttk.Entry(win, textvariable=height)
heightBox.place(y=390, x=355)

btn = Button(text="Open File", command=openFile)
btn.place(y=20, x=270)

resizeBtn = Button(text="Resize", height = 2, width = 20, command=resizeFile)
resizeBtn.place(y=420, x=90)

pngBtn = Button(text="Convert To png", height = 2, width = 20, command=convertToPng)
pngBtn.place(y=420, x=260)

# print(file)

win.mainloop()