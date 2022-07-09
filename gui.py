from ftplib import parse150
from tkinter import *
from movie import mrun,main
from series import srun,seasonwise,epwise
from custom.custom import *


def download():
    print("running manual download")
    url = e.get()
    print(url)
    preferred= str(var.get())
    choice= str(man.get())
    if pix.get() ==1:
        pixel = '1080p'
    elif pix.get() ==2:
        pixel = '720p'
    elif pix.get() ==3:
       pixel = 'HEVC 720p '
    elif pix.get() ==4:
       pixel = '480p'
    if preferred =='1':
        if  "season" in e.get().lower():
            preferred ="3"
        else:
            mrun.run(url,choice,pixel)
    if preferred == '2':
        global myLabel2,e2,getLink
        openbrowser(url)
        myLabel2 = Label(frame,text="Enter your prefered download link")
        myLabel2.grid(row=30,column=1)
        e2 = Entry(frame)
        e2.grid(row=20,column=2)
        getLink = Button(frame,text="Get link!", command=lambda: selecteDownload(e2.get()))
        getLink.grid(row=20,column=3)
    if preferred =="3":
        if eors.get() == 1:
            if ep.get() ==1:
                try:
                    print("All episode selected",pixel,choice)
                    season ="1"
                    episode= "all"
                    epwise.episodeSelect(choice,season,episode,pixel,url)
                except UnboundLocalError:
                    print("You have not selected all options!")
            elif ep.get()==2:
                try:
                    print("Latest episode selected")
                    season ="1"
                    episode= "latest"
                    epwise.episodeSelect(choice,season,episode,pixel,url)
                except UnboundLocalError:
                    print("You have not selected all options!")
            elif ep.get()==3:
                try:
                    epno= str(p10.get())
                    print(f"Episode {epno} is selected")
                    season ="1"
                    episode= epno
                    epwise.episodeSelect(choice,season,episode,pixel,url)
                except UnboundLocalError:
                    print("You have not selected all options!")
        elif eors.get()==2:
            print("season")

def selectep():
    global p10 
    p10 = Entry(frame)
    p10.grid(row=9,column=4)


def eps():
    global p7,p8,p9,p10
    p7 = Radiobutton(frame,text="All", variable=ep, value=1)
    p8 = Radiobutton(frame,text="Latest", variable=ep, value=2)
    p9 = Radiobutton(frame,text="Episode NO.", variable=ep, value=3)  
    p10 = Entry(frame)
    p7.grid(row=7,column=3)
    p8.grid(row=8,column=3)
    p9.grid(row=9,column=3)
    p10.grid(row=9,column=4)
    

    






def season():
    try:
        p7.grid_remove()
        p8.grid_remove()
        p9.grid_remove()
        p10.grid_remove()
    except:
        pass
    return
def manual():
    removeManual()
    if "season" not in e.get().lower():
        global myLabel, myLabel1, gds, gdrive,p1,p2,p3,p4,p5,p6,b7,p8

        myLabel = Label(frame,text="How do you want to download the file?")
        myLabel.grid(row=4,column=2)

        gds = Radiobutton(frame,text="1. GDS", variable=man, value= 1)
        gdrive = Radiobutton(frame,text="2. GDrive",variable=man, value=2)

        gds.grid(row=5,column=2)
        gdrive.grid(row=6,column=2)

        myLabel1 = Label(frame,text="What is the pixel?")
        myLabel1.grid(row=7,column=2)

        p1 = Radiobutton(frame,text="1080p", variable=pix, value=1)
        p2 = Radiobutton(frame,text="720p", variable=pix, value=2)
        p3 = Radiobutton(frame,text="720p HEVC", variable=pix, value=3)
        p4 = Radiobutton(frame,text="480p", variable=pix, value=4)
        p1.grid(row=8,column=2)
        p2.grid(row=9,column=2)
        p3.grid(row=10,column=2)
        p4.grid(row=11,column=2)
    elif "season" in e.get().lower():

        myLabel = Label(frame,text="How do you want to download the file?")
        myLabel.grid(row=4,column=2)

        gds = Radiobutton(frame,text="1. GDS", variable=man, value= 1)
        gdrive = Radiobutton(frame,text="2. GDrive",variable=man, value=2)

        gds.grid(row=5,column=2)
        gdrive.grid(row=6,column=2)

        myLabel1 = Label(frame,text="What is the pixel?")
        myLabel1.grid(row=7,column=2)

        p1 = Radiobutton(frame,text="1080p", variable=pix, value=1)
        p2 = Radiobutton(frame,text="720p", variable=pix, value=2)
        p3 = Radiobutton(frame,text="720p HEVC", variable=pix, value=3)
        p4 = Radiobutton(frame,text="480p", variable=pix, value=4)

        p1.grid(row=8,column=2)
        p2.grid(row=9,column=2)
        p3.grid(row=10,column=2)
        p4.grid(row=11,column=2)

        p5 = Label(frame,text="EP wise or Season wise?")
        p6 = Radiobutton(frame,text="EP", variable=eors, value=1, command= eps )
        b7 = Radiobutton(frame,text="Season", variable=eors, value=2, command = season)

        p5.grid(row=12,column=2)
        p6.grid(row=13,column=2)
        b7.grid(row=14,column=2)

        if str(eors.get()) == "1":
            print("Ep")
        elif str(eors.get()) =='2':
            print("season")

def removeManual():
    try:
        myLabel.grid_remove()
        myLabel1.grid_remove()
        p1.grid_remove()
        p2.grid_remove()
        p3.grid_remove()
        p4.grid_remove()
        gds.grid_remove()
        gdrive.grid_remove()
    except:
        pass
    try:
        myLabel2.grid_remove()
        e2.grid_remove()
        getLink.grid_remove()
    except:
        pass
    try:
        p5.grid_remove()
        p6.grid_remove()
    except:
        pass
    try:
        p7.grid_remove()
        p8.grid_remove()
        p9.grid_remove()
        p10.grid_remove()
    except:
        pass
    try:
        b7.grid_remove()
    except:
        pass

def custom():
    removeManual()

    return

# defining Tkinter

root= Tk()
root.title("Py downloader")
root.geometry("600x500")
try:
    root.iconbitmap("images/mlwbd.ico")
except:
    pass
#declaring variable
var = IntVar()
man = IntVar()
pix = IntVar()
eors = IntVar()
ep= IntVar()
#creating frame
frame = LabelFrame(root)
frame.pack(fill="both", expand="yes")
infoLabel = Label(frame,text="Etnter the MLWBD Movie or Series link ")
infoLabel.grid(row=1,column=1)
#creating entry point
e = Entry(frame)
e.grid(row=1,column=2)
#creating options
r1 = Radiobutton(frame,text="Manual", variable=var, value=1, command=manual)
r2 = Radiobutton(frame,text="Custom", variable=var, value=2, command=custom)

#Showing options
r1.grid(row=2,column=1)
r2.grid(row=30,column=1)
#submit button
submit=Button(frame,text="Submit",command=lambda: download() )
submit.grid(row=35,column=1)


root.mainloop()