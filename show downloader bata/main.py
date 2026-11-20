# TO DO
# - create a check button for quick input on my inputs     DONE
#   (file address for the download location) for future github support
# - add windows support
# - upload to github

from tkinter import *
from tkinter import ttk
from helper import start

root = Tk()
needsAudio = BooleanVar(value=False)
isShow = BooleanVar(value=False)
deleteOld = BooleanVar(value=False)
indexURL = StringVar()
audioIndexURL = StringVar()
Name = StringVar()
SName = StringVar()
EpNum = StringVar()
SnNum = StringVar()

needsPath = BooleanVar(value=True)
Path = StringVar()

def backend():
    start(isShow.get(), needsAudio.get(), indexURL.get(), audioIndexURL.get(), SName.get(), SnNum.get(), EpNum.get(), Name.get(), deleteOld.get(), needsPath.get(), Path.get())

def audioTB():
    if needsAudio.get() == True:
        audioTextBox.grid()
        ATBtext.grid()
    else:
        audioTextBox.grid_remove()
        ATBtext.grid_remove()

def showDataTB():
    if isShow.get() == True:
        SnameText.grid()
        SnameTextBox.grid()
        EpText.grid()
        EpTextBox.grid()
        SnText.grid()
        SnTextBox.grid()
    else:
        SnameText.grid_remove()
        SnameTextBox.grid_remove()
        EpText.grid_remove()
        EpTextBox.grid_remove()
        SnText.grid_remove()
        SnTextBox.grid_remove()

def pathTB():
    if needsPath.get() == False:
        pathText.grid()
        pathTextBox.grid()
    else:
        pathText.grid_remove()
        pathTextBox.grid_remove()


frm = ttk.Frame(root, padding=10)
frm.grid()

#quit button
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=0)

#check boxes
ttk.Checkbutton(frm, text="Delete seperate files?", variable=deleteOld).grid(column=3, row=0, padx=20)
ttk.Checkbutton(frm, text="Show?", variable=isShow, command=showDataTB).grid(column=3, row=1, padx=20)
ttk.Checkbutton(frm, text="needs Audio?", variable=needsAudio, command=audioTB).grid(column=3, row=2, padx=20)
ttk.Checkbutton(frm, text="DanTheMan?", variable=needsPath, command=pathTB).grid(column=3, row=3, padx=20)

#visual/main URL
ttk.Label(frm, text="URL:").grid(column=0, row=1)
ttk.Entry(frm, width=50, textvariable=indexURL).grid(column=1, row=1)
#audio URL
ATBtext = ttk.Label(frm, text="Audio URL:")
ATBtext.grid(column=0, row=2)
ATBtext.grid_remove()
audioTextBox = ttk.Entry(frm, width=50, textvariable=audioIndexURL)
audioTextBox.grid(column=1, row=2)
audioTextBox.grid_remove()

#data
#Ep/movie name
nameText = ttk.Label(frm, text="Ep/Movie Name:")
nameText.grid(column=0, row=3)
nameTextBox = ttk.Entry(frm, width=50, textvariable=Name)
nameTextBox.grid(column=1, row=3)
#show name
SnameText = ttk.Label(frm, text="Show Name:")
SnameText.grid(column=0, row=4)
SnameText.grid_remove()
SnameTextBox = ttk.Entry(frm, width=50, textvariable=SName)
SnameTextBox.grid(column=1, row=4)
SnameTextBox.grid_remove()
#season num
SnText = ttk.Label(frm, text="Season num:")
SnText.grid(column=0, row=5)
SnText.grid_remove()
SnTextBox = ttk.Entry(frm, width=50, textvariable=SnNum)
SnTextBox.grid(column=1, row=5)
SnTextBox.grid_remove()
#episode num
EpText = ttk.Label(frm, text="Episode Num:")
EpText.grid(column=0, row=6)
EpText.grid_remove()
EpTextBox = ttk.Entry(frm, width=50, textvariable=EpNum)
EpTextBox.grid(column=1, row=6)
EpTextBox.grid_remove()

#path
pathText = ttk.Label(frm, text="File Path:")
pathText.grid(column=0, row=7)
pathText.grid_remove()
pathTextBox = ttk.Entry(frm, width=50, textvariable=Path)
pathTextBox.grid(column=1, row=7)
pathTextBox.grid_remove()




#run button
ttk.Button(frm, text="run", command=backend).grid(column=0, row=500)


root.mainloop()