#Main screen

from tkinter import *
from tkinter import messagebox as MessageBox
from turtle import goto
from LogInADjdbc import LogInADjdbc
from GeneralADjdbc import GeneralADjdbc

name = " "
rol= " "
frames ={}
teamG = ""


class GeneralSpecs():

    adminGeneral = GeneralADjdbc()

    def __init__(self):

        #General settings

        self.frameGeneral = Tk()
        self.frameGeneral.title("THE BOX: General Specs")
        self.frameGeneral.geometry("1123x673")
        

        #Define background image

        self.bgImage = PhotoImage(file="Images/generalBg.png")
        self.labelBg = Label(self.frameGeneral,image=self.bgImage)
        self.labelBg.place(x=0,y=0)

        #Define and create components (Team number, weight, height)

        def click(*args):
            self.tfTeam.delete(0, 'end')

        def click2(*args):    
            self.tfWeight.delete(0,'end')

        def click3(*args):
            self.tfHeight.delete(0,'end')
  
        def leave(*args):

            self.frameGeneral.focus()
  
        #Define and create components (username and password)

        self.tfTeam = Entry(self.frameGeneral, width=50)

        self.tfTeam.insert(0,"Team number")

        self.tfTeam.bind("<Button-1>", click)

        self.tfTeam.bind("<Leave>", leave)

        self.tfWeight = Entry(self.frameGeneral, width= 50)

        self.tfWeight.insert(0,"Robot Weight")

        self.tfWeight.bind("<Button-1>", click2)

        self.tfWeight.bind("<Leave>", leave)

        self.tfHeight = Entry(self.frameGeneral, width= 50)

        self.tfHeight.insert(0,"Robot Height")

        self.tfHeight.bind("<Button-1>", click3)

        self.tfHeight.bind("<Leave>", leave)

        self.bBack = Button(self.frameGeneral, text ="Back", bg="#B9E5EF", command = self.back)

        self.bSave = Button(self.frameGeneral, text ="Save", bg="#B9E5EF")

        #Position components

        self.tfTeam.place(relx = 0.5,rely = 0.5, anchor = CENTER)

        self.tfWeight.place(x = 410,y = 410)

        self.tfHeight.place(x = 410,y = 495)

        self.bBack.place(x=500, y = 560)

        self.bSave.place(x=570, y=560)

        self.frameGeneral.mainloop()
    
    def back(self):

        self.frameGeneral.destroy()
        toShow = PitScouting()
    
    def getData(self):
        global teamG, name
        team = self.tfTeam.get()
        teamG = team
        weight = self.tfWeight.get()
        height = self.tfHeight.get()

        if (team == "Team number" or team == "") or (weight == "Robot Weight" or weight == "") or (height == "Robot Height" or height == ""):

            datos = "VACIO"
        else:

            datos= team +","+ weight +","+ height + "," +  name
        
        return datos
    
    def saveGeneral(self):
        datos = self.getData()
        print(datos)
        if(datos != "VACIO"):

            data = datos.split(",")
            tupla = self.adminGeneral.saveData(data)
            
                
        else:
            MessageBox.showinfo("Alert", "Write the data")




class PitScouting():

    def __init__(self):

        #General settings
        self.framePit = Tk()
        self.framePit.title("THE BOX: Pit Scouting")
        self.framePit.geometry("1123x673")

        #Define background image

        self.bgImage = PhotoImage(file="Images/pitSct.png")
        self.labelBg = Label(self.framePit,image=self.bgImage)

        self.labelBg.place(x=0,y=0)

        #Define and create components (general specs, robot specs, programming, mechanisms, match preview, notes)

        self.bGeneralSpecs = Button(self.framePit, text = "General Specs", bg="#B9E5EF", height=6, width=28,command=self.goToGeneral)
        self.bRobotSpecs = Button(self.framePit, text = "Robot Specs", bg="#B9E5EF", height=6, width=28)
        self.bProgramming = Button(self.framePit, text = "Programming", bg="#B9E5EF", height=6, width=28)
        self.bMechanisms = Button(self.framePit, text = "Mechanisms", bg="#B9E5EF", height=6, width=28)
        self.bMatchPre = Button(self.framePit, text = "Match Preview", bg="#B9E5EF", height=6, width=28)
        self.bNotes = Button(self.framePit, text = "Notes", bg="#B9E5EF", height=6, width=28)

        #Position elements

        self.bGeneralSpecs.place(x = 40, y=295)
        self.bRobotSpecs.place(x=310, y=295)
        self.bProgramming.place(x=600, y=295)
        self.bMechanisms.place(x=875, y=295)
        self.bMatchPre.place(x=310,y=507)
        self.bNotes.place(x=600,y=507)
        
        self.framePit.mainloop()
    
    
    def goToGeneral(self):
        self.framePit.destroy()
        toShow = GeneralSpecs()

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

        print("Voy a hacer pit scouting")
        self.frameCuanti.destroy()
        toShow = PitScouting()

    def goToMatchSct(self):

        print("Voy a hacer match scouting")
        self.frameCuanti.destroy()

class LogIn() :
    
    adminLogIn = LogInADjdbc()

    
    def __init__(self):

        #General settings

        self.frame = Tk()
        self.frame.title("THE BOX: STEAMex 6832 scouting app")
        self.frame.geometry("1123x673")
        
        #Define background image
        
        self.bgImage = PhotoImage(file="Images/test.png")
        self.labelBg = Label(self.frame,image=self.bgImage)
        self.labelBg.place(x=0, y=0)

        #General Methods

        def click(*args):

            self.tfUser.delete(0, 'end')
  
        def leave(*args):

            self.frame.focus()
        
        def clickPassword(*args):

            self.tfPassword.delete(0, 'end')
            self.tfPassword.config(show ="*")
  
        #Define and create components (username and password)

        self.tfUser = Entry(self.frame, width=50)

        self.tfUser.insert(0,"Username")

        self.tfUser.bind("<Button-1>", click)

        self.tfUser.bind("<Leave>", leave)

        self.tfPassword = Entry(self.frame, width=50)

        self.tfPassword.insert(0,"Password")

        self.tfPassword.bind("<Button-1>", clickPassword)
        
        self.bLogIn = Button(self.frame, text ="Log In", bg="#84EC5F", command = self.blogInFunction)

        #Position the components
   
        self.tfUser.place(relx = 0.5,rely = 0.5, anchor = CENTER)

        self.tfPassword.place(x = 410,y = 395)

        self.bLogIn.place(x = 540,y = 450)


        self.frame.mainloop()

    #Log In functions          
            

    def obtenerDatos(self):

        user = self.tfUser.get()
        password = self.tfPassword.get()

        if user == "Username" or password == "Password":

            datos = "VACIO"
        else:

            datos= user +","+ password
        
        return datos
    
    def goToPage(self):
        global rol,frames
        
        if rol == "Cuanti":
            
            self.frame.destroy()
            toShow = MainCuanti()

    
    def blogInFunction(self):
        global name, rol
        datos=self.obtenerDatos()
        if(datos != "VACIO"):

            data = datos.split(",")
            tupla = self.adminLogIn.startApp(data)
            
            try:

                if(len(tupla) == 3):
                    name= tupla[0]
                    rol= tupla[2]
                    self.goToPage()
                if (tupla == 1):
                    print("ERROR connecting to database")
                    MessageBox.showinfo("Alert", "ERROR connecting to database")
                    
                    
            except:
                print("Wrong credentials")
                MessageBox.showinfo("Alert", "Wrong credentials")
                
        else:
            MessageBox.showinfo("Alert", "Write the username and password")



#main = LogIn()

test = GeneralSpecs()


