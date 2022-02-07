
from tkinter import *
from tkinter import messagebox as MessageBox
from PitScoutingGUI import PitScouting

class MainCuanti():

    def __init__(self):

        #General settings

        self.frameCuanti = Tk()
        self.frameCuanti.title("THE BOX: Main Menu Cuanti")
        self.frameCuanti.geometry("1123x673")

        #Define background image

        self.bgImage = PhotoImage(file ="Images/MainCuanti.png")
        self.labelBg = Label(self.frameCuanti,image = self.bgImage)
        self.labelBg.place(x = 0, y = 0)

        #Define and create components (pit scouting and match scouting button)

        self.bPitScouting = Button(self.frameCuanti, text="Pit Scouting", bg = "#B9E5EF", height = 6, width = 28, command = self.goToPitSct)
        self.bMatchScouting = Button(self.frameCuanti, text="Match Scouting", bg = "#B9E5EF",height = 6, width = 28, command = self.goToMatchSct)

        #Position the components

        self.bPitScouting.place(x = 195, y= 423)
        self.bMatchScouting.place(x =725, y= 430)
        self.frameCuanti.mainloop()

    #Functions

    def goToPitSct(self):
        self.frameCuanti.destroy()
        toShow = PitScouting()

    def goToMatchSct(self):

        print("Voy a hacer match scouting")
        self.frameCuanti.destroy()

