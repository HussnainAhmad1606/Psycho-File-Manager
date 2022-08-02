from tkinter import *
from tkinter.messagebox import showinfo
import webbrowser
import os
from PIL import Image, ImageTk

root = Tk()
root.title("Psycho File Manager")

# Delaring useful variables
softwareVersion = "1.0"
currentLocation = StringVar()
currentLocation.set("D:/Coding/Python/Notepad/")
status = StringVar()
status.set("Ready")
totalFiles = StringVar("")
totalFiles.set("Total Files: 0")

# By default window will be open in full screen
# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))
root.geometry("600x500")
# Setting the icon of the GUI
icon = PhotoImage(file = "Icons/folder.png")
root.iconphoto(False, icon)

# ALL Functions are here
# About function
def about():
	aboutInfo = f"Software: Psycho File Manager\nProgrammer: Psycho Coder\nVersion: {softwareVersion}" 
	showinfo("About", aboutInfo)


# Visit Website function
def visitWebsite():
	webbrowser.open("https://github.com/HussnainAhmad1606/")

# When user click Search button this function will run
def changeDir():
	previousChilds = folderFrame.winfo_children()
	for child in previousChilds:
		child.destroy()
	global locationEntry
	print(locationEntry.get())
	if locationEntry.get().rfind("/")+1 == len(locationEntry.get()):
		currentLocation.set(locationEntry.get())
	else:
		currentLocation.set(locationEntry.get() + "/")
		# Set the location of the cursor to the end
	showFoldersOnLocation()


# Function to find second last occurance from string
def findSecondLast(text, value):
	return text.rfind(value, 0, text.rfind(value))


# On clicking back button, directory will be one step backward
def directoryBack():
	index = findSecondLast(currentLocation.get(), "/")
	print(index)
	if len(currentLocation.get()) > 3:
		newLocation = currentLocation.get()[0:index] + "/"
		print(newLocation)
		currentLocation.set(newLocation)
		previousChilds = folderFrame.winfo_children()
		for child in previousChilds:
			child.destroy()
		showFoldersOnLocation()

	
# This function will show the folders of specific location on GUI
def showFoldersOnLocation():
	files = os.listdir(currentLocation.get())
	global totalFiles
	totalFiles.set(f"Total Files: {len(files)}")
	for file in files:
		label  = Label(folderFrame, text=file)
		label.pack()
	if (len(currentLocation.get()) < 4):
		backBtn["state"] = DISABLED
	else:
		backBtn["state"] = NORMAL

# Showing current location on top
locationFrame = Frame(root)

backBtn = Button(locationFrame, text="< Back", command=directoryBack)
backBtn.pack(side=LEFT)
locationEntry = Entry(locationFrame, textvariable=currentLocation, width=120)
locationEntry.pack(side=LEFT)
goButton = Button(locationFrame, text="Search", command=changeDir)
goButton.pack(side=LEFT)
locationFrame.pack(side=TOP)

folderFrame = Frame(root, bg="red")
files = os.listdir(currentLocation.get())
totalFiles.set(f"Total Files: {len(files)}")
for file in files:
	print(file)
	# photo = ImageTk.PhotoImage(Image.open("Icons/folder.jpg"))
	# label = Label(folderFrame,image=photo, width=100, height=100)
	# label.pack()
	name = Label(folderFrame, text=file)
	name.pack()

folderFrame.pack(side=TOP)

# Status bar
statusBarFrame = Frame(root, borderwidth=4)
totalFilesLabel = Label(statusBarFrame, textvariable=totalFiles)
totalFilesLabel.pack(side=LEFT)
statusBar = Label(statusBarFrame, textvariable=status)
statusBar.pack(side=RIGHT)
statusBarFrame.pack(side=BOTTOM, fill=X)

# Main Menu
mainMenu = Menu(root)

# Help Menu
helpMenu = Menu(mainMenu, tearoff=0)
helpMenu.add_command(label="Visit Website", command=visitWebsite)
helpMenu.add_command(label="About", command=about)
mainMenu.add_cascade(label="Help", menu=helpMenu)

root.config(menu=mainMenu)
root.mainloop()