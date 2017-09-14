import tkinter

#only press return once
okToPressReturn = True

#the player's attributes
hunger = 50
hour = 0

#-------------------------------------------------------------------

def startGame(event):

    global okToPressReturn

    if okToPressReturn == False:
        pass
    
    else:
        #update the time left label.
        startLabel.config(text="")
        #start updating the values
        updateHunger()
        updateHour()
        updateDisplay()

        okToPressReturn = False

#-------------------------------------------------------------------
 
def updateDisplay():

    #use the globally declared variables above.
    global hunger
    global hour

    if hunger > 50:
        catPic.config(image = catfullphoto)
    if hunger == 50:
        catPic.config(image = titlephoto)
    elif hunger>=45 and hunger <50:
        catPic.config(image = normalphoto)
    elif hunger>38 and hunger<45:
        catPic.config(image=yeahphoto)
    elif hunger>=33 and hunger <=38:  
        catPic.config(image=stickyphoto)
    elif hunger>27 and hunger <33:
        catPic.config(image=nothingphoto)
    elif hunger >=21 and hunger <=27:
        catPic.config(image = calmphoto)    
    elif hunger >=16 and hunger<21:
        catPic.config(image = hungryphoto)
    elif hunger >=11 and hunger<16:
        catPic.config(image = hungerphoto)
    elif hunger >=6 and hunger<11:
        catPic.config(image = almostphoto)
    elif hunger>=1 and hunger<6:
        catPic.config(image = baseballbatphoto)
    elif hunger ==0:
        catPic.config(image = revengephoto)    
    else: 
        catPic.config(image = titlephoto)

    #update the time left label.
    hungerLabel.config(text="Hunger: " + str(hunger))

    #update the hour's label.
    hourLabel.config(text="hour: " + str(hour))   

    #run the function again after 50ms.       
    catPic.after(50, updateDisplay)

#-------------------------------------------------------------------
 
def updateHunger():

    #use the globally declared variables above.
    global hunger

    #decrement the hunger.
    hunger -= 1

    if isAlive():
        #run the function again after 500ms.
        hungerLabel.after(500, updateHunger)

#-------------------------------------------------------------------

def updateHour():

    #use the globally declared variables above.
    global hour

    #decrement the hunger.
    hour += 1

    if isAlive():
        #run the function again after 3 seconds.
        hourLabel.after(3000, updateHour)

#-------------------------------------------------------------------

def feed():

    global hunger
    
    if hunger <= 95:
        hunger += 10
    else:
        hunger -=10
        
#-------------------------------------------------------------------

def isAlive():

    global hunger
    
    if hunger <= 0:
        #update the start info label.
        startLabel.config(text="""GAME OVER! 
        YOU KILLED YOUR CAT!
        Remember, cats have nine lives.
        Now, it's the cat's turn!

        Thanks for playing!""")
        return False
    else:
        return True


def close_window():
    import sys
    sys.exit()       
#-------------------------------------------------------------------


#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("All Fed Up")
#set the size.
root.geometry("400x525")

#add a label for the start text.
startLabel = tkinter.Label(root, text="Press 'Return/Enter' to start!", font=('Helvetica', 12))
startLabel.pack()

#add a hunger label.
hungerLabel = tkinter.Label(root, text="Hunger: " + str(hunger), font=('Helvetica', 12))
hungerLabel.pack()

#add a 'hour' label.
hourLabel = tkinter.Label(root, text="Hour: " + str(hour), font=('Helvetica', 12))
hourLabel.pack()

titlephoto = tkinter.PhotoImage(file = "cover.gif")
yeahphoto = tkinter.PhotoImage(file = "yeah.gif")
normalphoto = tkinter.PhotoImage(file="regular.gif")
stickyphoto = tkinter.PhotoImage(file = "sticky.gif")
nothingphoto = tkinter.PhotoImage(file = "nothing.png")
calmphoto = tkinter.PhotoImage(file = "calm.gif")
hungryphoto = tkinter.PhotoImage(file="hungrycat.gif")
hungerphoto =tkinter.PhotoImage(file ="feed_me.gif")
almostphoto = tkinter.PhotoImage(file = "hunger.gif")
baseballbatphoto = tkinter.PhotoImage(file = "baseballbat.gif")
revengephoto = tkinter.PhotoImage(file = "revenge.gif")
catfullphoto = tkinter.PhotoImage(file = "catfull.gif")

#add a cat image
catPic = tkinter.Label(root, image=titlephoto)
catPic.pack()

buttonFeed = tkinter.Button(root, text="Feed Me", font = "Arial", fg = "yellow", activebackground="blue",
                            activeforeground="black", bg = "black", width=20, command=feed)
buttonFeed.pack()

buttonEnd = tkinter.Button (root, text="Goodbye", fg = "yellow", bg = "black", activebackground="blue", 
                            font = "Arial", activeforeground="black",width=10, command=close_window)
buttonEnd.pack()

#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)

#start the GUI
root.mainloop()
