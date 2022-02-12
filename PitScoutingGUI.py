from tkinter import *
from tkinter import messagebox as MessageBox

from matplotlib import get_backend

from GeneralADjdbc import GeneralADjdbc
import Data as dGeneral

gteam = 0

class Notes():
    admin = GeneralADjdbc()
    

    def __init__(self):

        #General settings
        self.frameNotes= Tk()
        self.frameNotes.title("THE BOX: Notes")
        self.frameNotes.geometry("1123x673")

        #Define background image

        self.bgImage = PhotoImage(file="Images/generalBg2.png")
        self.labelBg = Label(self.frameNotes,image=self.bgImage)
        self.labelBg.place(x=0,y=0)
        
        #Define components
        
        self.tfNotes = Text(self.frameNotes, width=90, height=10)


        self.bBack = Button(self.frameNotes, text ="Back", bg="#B9E5EF", command = self.back)

        self.bSave = Button(self.frameNotes, text ="Save", bg="#B9E5EF", command=self.saveNotes)

        #Position elements

        self.tfNotes.place(relx = 0.5,rely = 0.5, anchor = CENTER)

        self.bBack.place(x=500, y = 500)

        self.bSave.place(x=570, y=500)

        self.frameNotes.mainloop()

    def back(self):

        self.frameNotes.destroy()
        toShow = PitScouting()
    
    def getData(self):
        notes= self.tfNotes.get("1.0", END)
        notes = notes.split("\n")

        datos = dGeneral.team + "," + notes[0]
        return datos
    
    def saveNotes(self):
        datos= self.getData()
        datos = datos.split(",")
        response =self.admin.saveNotes(datos)
        if response:
            MessageBox.showinfo("Alert", "Data SAVED")
        else:
            MessageBox.showinfo("Alert", "ERROR Saving the data")


class MatchPreview():

    

    admin = GeneralADjdbc()

    def __init__(self):
        #General settings

        self.framePreview = Tk()
        self.framePreview.title("THE BOX: Match Preview")
        self.framePreview.geometry("1123x673")

        #Define background image

        self.bgImage = PhotoImage(file="Images/generalBg2.png")
        self.labelBg = Label(self.framePreview,image=self.bgImage)
        self.labelBg.place(x=0,y=0)

        self.priority = StringVar(self.framePreview)
        self.defense = StringVar(self.framePreview)

        self.priority.set("Team's priority")
        self.defense.set("Defense")

        #Define components

        def click(*args):
            self.tfCargosUpper.delete(0, 'end')

        def click2(*args):
            self.tfCargosLower.delete(0, 'end')
        
        def click3(*args):
            self.tfCycles.delete(0, 'end')
        
        def leave(*args):
            self.framePreview.focus()
        
        self.tfCargosUpper= Entry(self.framePreview, width=40)

        self.tfCargosUpper.insert(0,"Number of cargos on upper hub")

        self.tfCargosUpper.bind("<Button-1>", click)

        self.tfCargosUpper.bind("<Leave>", leave)

        self.tfCargosLower= Entry(self.framePreview, width=40)

        self.tfCargosLower.insert(0,"Number of cargos on lower hub")

        self.tfCargosLower.bind("<Button-1>", click2)

        self.tfCargosLower.bind("<Leave>", leave)

        self.tfCycles= Entry(self.framePreview, width=40)

        self.tfCycles.insert(0,"Number of cycles")

        self.tfCycles.bind("<Button-1>", click3)

        self.tfCycles.bind("<Leave>", leave)

        self.dDPriority = OptionMenu(self.framePreview, self.priority,"None","Upper Hub", "Lower Hub", "Climb", "Defense")

        self.dDDefense = OptionMenu(self.framePreview, self.defense,"True","False")

        self.bBack = Button(self.framePreview, text ="Back", bg="#B9E5EF", command = self.back)
        self.bSave = Button(self.framePreview, text ="Save", bg="#B9E5EF", command= self.savePreview)

        #Position elements
        self.tfCargosUpper.place(x= 270, y=200)
        self.tfCargosLower.place(x=270, y=270)
        self.tfCycles.place(x=270, y=340)
        self.dDPriority.place(x=600, y=200)
        self.dDDefense.place(x=600, y=270)

        self.bBack.place(x=480, y=450 )

        self.bSave.place(x=600, y=450)


        self.framePreview.mainloop()
    
    def back(self):

        self.framePreview.destroy()
        toShow = PitScouting()
    
    def getData(self):
        cUpper = self.tfCargosUpper.get()
        cLower = self.tfCargosLower.get()
        cycles = self.tfCycles.get()
        defense = self.defense.get()
        priority = self.priority.get()

        dicBool = {"True": 1, "False": 0}
        datos = dGeneral.team + ","+ str(cUpper) + "," + str(cLower) + "," + str(cycles)+ "," + str(dicBool[defense])+ "," + priority
        return datos


    def savePreview(self):
        datos = self.getData()
        datos = datos.split(",")
        response =self.admin.savePreview(datos)
        if response:
            MessageBox.showinfo("Alert", "Data SAVED")
        else:
            MessageBox.showinfo("Alert", "ERROR Saving the data")
        
class Mechanisms():

    admin = GeneralADjdbc()
    

    def __init__(self):

        #General settings
        self.frameMechanisms = Tk()
        self.frameMechanisms.title("THE BOX: Mechanisms")
        self.frameMechanisms.geometry("1123x673")

        self.mechanismUpper = StringVar(self.frameMechanisms)
        self.actuatorUpper = StringVar(self.frameMechanisms)
        self.mechanismLower = StringVar(self.frameMechanisms)
        self.actuatorLower = StringVar(self.frameMechanisms)
        self.mechanismIntake = StringVar(self.frameMechanisms)
        self.actuatorIntake = StringVar(self.frameMechanisms)
        self.mechanismClimber = StringVar(self.frameMechanisms)
        self.actuatorClimber = StringVar(self.frameMechanisms)


        self.mechanismUpper.set("Type of mechanism for Upper hub")
        self.actuatorUpper.set("Type of actuator for Upper hub")
        self.mechanismLower.set("Type of mechanism for Lower hub")
        self.actuatorLower.set("Type of actuator for Lower hub")
        self.mechanismIntake.set("Type of mechanism for Intake")
        self.actuatorIntake.set("Type of actuator for Intake")
        self.mechanismClimber.set("Type of mechanism for Climber")
        self.actuatorClimber.set("Type of actuator for Climber")

        #Define background image

        self.bgImage = PhotoImage(file="Images/generalBg2.png")
        self.labelBg = Label(self.frameMechanisms,image=self.bgImage)
        self.labelBg.place(x=0,y=0)

        #Define and create components

        self.dDMechUpper = OptionMenu(self.frameMechanisms,self.mechanismUpper,"None","Shooter", "Assited shooter", "Catapult", "Other")
        self.dDActUpper = OptionMenu(self.frameMechanisms,self.actuatorUpper,"None","Pneumatic", "Electric linear actuator", "Motor", "Mixed")
        self.dDMechLower = OptionMenu(self.frameMechanisms,self.mechanismLower,"None","Shooter", "Assited shooter", "Catapult", "Position", "Ramp","Other")
        self.dDActLower = OptionMenu(self.frameMechanisms,self.actuatorLower,"None","Pneumatic", "Electric linear actuator", "Motor", "Mixed")
        self.dDMechIntake = OptionMenu(self.frameMechanisms, self.mechanismIntake,"None","Floor", "Terminal", "Both")
        self.dDActIntake = OptionMenu(self.frameMechanisms,self.actuatorIntake,"None","Pneumatic", "Electric linear actuator", "Motor", "Mixed")
        self.dDMechClimber = OptionMenu(self.frameMechanisms, self.mechanismClimber,"None", "Double", "Linear actuator", "Pulley", "Scissor", "Position", "Other")
        self.dDActClimber = OptionMenu(self.frameMechanisms,self.actuatorClimber,"None","Pneumatic", "Electric linear actuator", "Motor", "Mixed")
        self.bBack = Button(self.frameMechanisms, text ="Back", bg="#B9E5EF", command = self.back)
        self.bSave = Button(self.frameMechanisms, text ="Save", bg="#B9E5EF", command= self.saveMechanisms)

        #Position elements

        self.dDMechUpper.place(x= 270, y=150)
        self.dDActUpper.place(x= 270, y=220)
        self.dDMechLower.place(x= 270, y=290)
        self.dDActLower.place(x=270, y=360)
        self.dDMechIntake.place(x=570, y=150)
        self.dDActIntake.place(x=570, y=220)
        self.dDMechClimber.place(x=570, y= 290 )
        self.dDActClimber.place(x=570, y=360)
        self.bBack.place(x=450, y = 500)

        self.bSave.place(x=570, y=500)

        self.frameMechanisms.mainloop()
    
    def back(self):

        self.frameMechanisms.destroy()
        toShow = PitScouting()
    
    def getData(self):
        upperType = self.mechanismUpper.get()
        actUpper = self.actuatorUpper.get()
        lowerType = self.mechanismLower.get()
        actLower = self.actuatorLower.get()
        intakeType = self.mechanismIntake.get()
        actIntake = self.actuatorIntake.get()
        climbType = self.mechanismClimber.get()
        actClimb = self.actuatorClimber.get()

        dicUpper = {"None": 0,"Shooter": 1, "Assited shooter": 2, "Catapult":3, "Other": 3}
        dicLower = {"None": 0,"Shooter": 1, "Assited shooter": 2, "Catapult": 3, "Position": 4, "Ramp": 5,"Other": 6}
        dicIntake = {"None": 0,"Floor": 1, "Terminal": 2, "Both": 3}
        dicClimber = {"None": 0, "Double": 1, "Linear actuator": 2, "Pulley": 3, "Scissor": 4, "Position": 5, "Other": 6}
        dicAcuators = {"None": 0,"Pneumatic": 1, "Electric linear actuator": 2, "Motor": 3, "Mixed": 4}

        datos = dGeneral.team + "," + str(dicUpper[upperType]) + "," + str(dicAcuators[actUpper]) + ","+ str(dicLower[lowerType])+ ","+ str(dicAcuators[actLower]) + ","+ str(dicIntake[intakeType])+ ","+ str(dicAcuators[actIntake]) + ","+ str(dicClimber[climbType])+ ","+ str(dicAcuators[actClimb])
        return datos

    def saveMechanisms(self):
        datos = self.getData()
        datos = datos.split(",")
        response= self.admin.saveMechanisms(datos)
        if response:
            MessageBox.showinfo("Alert", "Data SAVED")
        else:
            MessageBox.showinfo("Alert", "ERROR Saving the data")

class Programming():
    
    admin = GeneralADjdbc()

    def __init__(self):

        #General settings
        self.frameProgram = Tk()
        self.frameProgram.title("THE BOX: Programming")
        self.frameProgram.geometry("1123x673")

        self.vision = StringVar(self.frameProgram)
        self.auto = StringVar(self.frameProgram)
        self.taxi = StringVar(self.frameProgram)
        self.language = StringVar(self.frameProgram)
    

        self.vision.set("Computer Vision")
        self.auto.set("Autonomous")
        self.taxi.set("Taxi")
        self.language.set("Programming Language")

        

        #Define background image

        self.bgImage = PhotoImage(file="Images/generalBg2.png")
        self.labelBg = Label(self.frameProgram,image=self.bgImage)
        self.labelBg.place(x=0,y=0)

        #Define and create components

        def click(*args):
            self.tfCameras.delete(0, 'end')
        
        def click2(*args):
            self.tfGyros.delete(0, 'end')

        def click3(*args):
            self.tfEncoders.delete(0, 'end')

        def click4(*args):
            self.tfNavx.delete(0, 'end')
        
        def click5(*args):
            self.tfUltrasonics.delete(0, 'end')
        
        def click6(*args):
            self.tfCargosLower.delete(0, 'end')
        
        def click7(*args):
            self.tfCargosUpper.delete(0, 'end')
       

        def leave(*args):
            self.frameProgram.focus()

        self.dDProgramming = OptionMenu(self.frameProgram,self.language,"Java", "C++", "Labview")

        self.dDComputer = OptionMenu(self.frameProgram,self.vision,"True", "False")

        self.tfCameras = Entry(self.frameProgram, width=40)

        self.tfCameras.insert(0,"Number of cameras")

        self.tfCameras.bind("<Button-1>", click)

        self.tfCameras.bind("<Leave>", leave)

        self.tfGyros = Entry(self.frameProgram, width=40)

        self.tfGyros.insert(0,"Number of gyros")

        self.tfGyros.bind("<Button-1>", click2)

        self.tfGyros.bind("<Leave>", leave)

        self.tfEncoders= Entry(self.frameProgram, width=40)

        self.tfEncoders.insert(0,"Number of encoders")

        self.tfEncoders.bind("<Button-1>", click3)

        self.tfEncoders.bind("<Leave>", leave)

        self.tfNavx= Entry(self.frameProgram, width=40)

        self.tfNavx.insert(0,"Number of NAVX")

        self.tfNavx.bind("<Button-1>", click4)

        self.tfNavx.bind("<Leave>", leave)

        self.tfUltrasonics= Entry(self.frameProgram, width=40)

        self.tfUltrasonics.insert(0,"Number of Ultrasonics")

        self.tfUltrasonics.bind("<Button-1>", click5)

        self.tfUltrasonics.bind("<Leave>", leave)

        self.dDAuto = OptionMenu(self.frameProgram,self.auto,"True", "False")

        self.dDTaxi = OptionMenu(self.frameProgram,self.taxi,"True", "False")

        self.tfCargosLower= Entry(self.frameProgram, width=40)

        self.tfCargosLower.insert(0,"Cargos on Lower Hub")

        self.tfCargosLower.bind("<Button-1>", click6)

        self.tfCargosLower.bind("<Leave>", leave)

        self.tfCargosUpper= Entry(self.frameProgram, width=40)

        self.tfCargosUpper.insert(0,"Cargos on Upper Hub")

        self.tfCargosUpper.bind("<Button-1>", click7)

        self.tfCargosUpper.bind("<Leave>", leave)

        self.bBack = Button(self.frameProgram, text ="Back", bg="#B9E5EF", command = self.back)

        self.bSave = Button(self.frameProgram, text ="Save", bg="#B9E5EF", command=self.saveProgramming)

        #Position Elements

        self.dDProgramming.place(x=90, y=150)

        self.dDComputer.place(x=90, y = 230 )

        self.tfCameras.place(x=90, y= 310)

        self. tfGyros.place(x=90, y= 390)

        self.tfEncoders.place(x=430, y= 150)

        self.tfNavx.place(x=430, y=230)

        self.tfUltrasonics.place(x=430, y=310)

        self.dDAuto.place(x=430, y=390)

        self.dDTaxi.place(x=770, y=150)
        
        self.tfCargosLower.place(x=770, y=230)

        self.tfCargosUpper.place(x=770, y=310)

        self.bBack.place(x=500, y = 500)

        self.bSave.place(x=580, y=500)


        self.frameProgram.mainloop()


    def back(self):

        self.frameProgram.destroy()
        toShow = PitScouting()
    
    def getData(self):

        pLanguage = self.language.get()
        cVision = self.vision.get()
        camera = self.tfCameras.get()
        gyro = self.tfGyros.get()
        encoder = self.tfEncoders.get()
        navx = self.tfNavx.get()
        ultrasonic = self.tfUltrasonics.get()
        auto = self.auto.get()
        taxi = self.taxi.get()
        cargoLow = self.tfCargosLower.get()
        cargoUp = self.tfCargosUpper.get()

        dicBool = {"True": 1, "False" : 0}

        datos = dGeneral.team + ",'" + str(pLanguage) + "'," + str(dicBool[cVision]) + "," + str(camera) + "," +str(navx) + "," + str(gyro) + "," + str(encoder)+ "," + str(ultrasonic) + "," + str(cargoLow) + "," + str(cargoUp) + "," + str(dicBool[taxi])+ ","+ str(dicBool[auto])
        
        return datos 
    
    def saveProgramming(self):
        datos= self.getData()
        datos = datos.split(",")
        response = self.admin.saveProgramming(datos)
        if response:
            MessageBox.showinfo("Alert", "Data SAVED")
        else:
            MessageBox.showinfo("Alert", "ERROR Saving the data")

class RobotSpecs():
    
    admin = GeneralADjdbc()

    def __init__(self):

        #General settings
        self.frameRobot = Tk()
        self.frameRobot.title("THE BOX: Robot Specs")
        self.frameRobot.geometry("1123x673")

        self.velocity = StringVar(self.frameRobot)
        self.chassis = StringVar(self.frameRobot)
        self.wheels = StringVar(self.frameRobot)

        self.velocity.set("Double Traction")
        self.chassis.set("Type of Chassis")
        self.wheels.set("Type of wheels")
        #Define background image

        self.bgImage = PhotoImage(file="Images/generalBg2.png")
        self.labelBg = Label(self.frameRobot,image=self.bgImage)
        self.labelBg.place(x=0,y=0)

       
        #Define and create components (number of motors on chassis, collector, shooter and climber / double transmission, type of chassis, type of wheels)

        def click(*args):
            self.tfMChasis.delete(0, 'end')

        def click2(*args):    
            self.tfMIntake.delete(0,'end')

        def click3(*args):
            self.tfMShooter.delete(0,'end')

        def click4(*args):
            self.tfMClimber.delete(0,'end')
  
        def leave(*args):
            self.frameRobot.focus()

        self.tfMChasis = Entry(self.frameRobot, width=50)

        self.tfMChasis.insert(0,"Number of motors on chassis")

        self.tfMChasis.bind("<Button-1>", click)

        self.tfMChasis.bind("<Leave>", leave)

        self.tfMIntake = Entry(self.frameRobot, width=50)

        self.tfMIntake.insert(0,"Number of motors on intake")

        self.tfMIntake.bind("<Button-1>", click2)

        self.tfMIntake.bind("<Leave>", leave)

        self.tfMShooter = Entry(self.frameRobot, width=50)

        self.tfMShooter.insert(0,"Number of motors on shooter")

        self.tfMShooter.bind("<Button-1>", click3)

        self.tfMShooter.bind("<Leave>", leave)

        self.tfMClimber = Entry(self.frameRobot, width=50)

        self.tfMClimber.insert(0,"Number of motors on climber")

        self.tfMClimber.bind("<Button-1>", click4)

        self.tfMClimber.bind("<Leave>", leave)

        self.dDVelocity = OptionMenu(self.frameRobot,self.velocity,"true", "false")

        self.dDChassis = OptionMenu(self.frameRobot,self.chassis, "KOP", "Tread tank", "West Coast", "H-drive", "Holonomic", "Mecanum","Swerve", "Kiwi", "Butterfly", "Hybrid", "Other")

        
        self.dDWheels = OptionMenu(self.frameRobot, self.wheels, "KOP", "Colson", "Plaction", "Mecanum", "Omni", "Pneumatic", "Other")

        self.bBack = Button(self.frameRobot, text ="Back", bg="#B9E5EF", command = self.back)

        self.bSave = Button(self.frameRobot, text ="Save", bg="#B9E5EF", command=self.saveRobotSpecs)

        #Position components

        self.tfMChasis.place(x=250, y=150)
        self.tfMIntake.place(x=250, y=225)
        self.tfMShooter.place(x=250, y=300)
        self.tfMClimber.place(x=250, y=375)

        self.dDVelocity.place(x=600, y=150)
        self.dDChassis.place(x=600, y=225)
        self.dDWheels.place(x=600, y=300)

        self.bBack.place(x=520, y = 450)

        self.bSave.place(x=600, y=450)

        self.frameRobot.mainloop()

    def back(self):

        self.frameRobot.destroy()
        toShow = PitScouting()

    def getData(self):
        mChasis = self.tfMChasis.get()
        mIntake = self.tfMIntake.get()
        mShooter = self.tfMShooter.get()
        mClimber = self.tfMClimber.get()
        dVelocity =self.velocity.get()
        tChassis = self.chassis.get()
        tWheels = self.wheels.get()

        dicVelocity = {"true" : 1, "false" : 0}
        
        dicChassis = {"KOP": 1, "Tread tank": 2, "West Coast" : 3, "H-drive" : 4, "Holonomic" : 5 , "Mecanum" : 6,"Swerve" : 7, "Kiwi" : 8, "Butterfly" : 9, "Hybrid" : 10, "Other": 11}
        
        dicWheels = {"KOP" : 1, "Colson" : 2, "Plaction" :3 , "Mecanum" : 4, "Omni" : 5, "Pneumatic" :6 , "Other" : 7}

        datos= dGeneral.team+ "," +mShooter +","+ mChasis +","+ mClimber +","+ mIntake+ "," + str(dicChassis[tChassis]) + ","+ str(dicWheels[tWheels])+","+ str(dicVelocity[dVelocity]) 

        return datos

    
    def saveRobotSpecs(self):
        datos= self.getData()
        datos = datos.split(",")                            

        value = self.admin.saveRobotSpecs(datos)

        if value:
            MessageBox.showinfo("Alert", "Data SAVED")
            
        else: 
            MessageBox.showinfo("Alert", "ERROR saving the data")
            
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

        self.bSave = Button(self.frameGeneral, text ="Save", bg="#B9E5EF", command=self.saveGeneral)

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
    
        
        team = self.tfTeam.get()
        dGeneral.team= team
        weight = self.tfWeight.get()
        height = self.tfHeight.get()

        if (team == "Team number" or team == "") or (weight == "Robot Weight" or weight == "") or (height == "Robot Height" or height == ""):

            datos = "VACIO"
        else:

            datos= team +","+ weight +","+ height +","+ dGeneral.name
        
        return datos
    
    def saveGeneral(self):
        datos = self.getData()
        
        if(datos != "VACIO"):

            data = datos.split(",")
            value = self.adminGeneral.saveData(data)
            if value == 0:
                MessageBox.showinfo("Alert", "ERROR saving the data")
            else: 
                MessageBox.showinfo("Alert", "Data SAVED")
                
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
        self.bRobotSpecs = Button(self.framePit, text = "Robot Specs", bg="#B9E5EF", height=6, width=28, command=self.goToRobotSpecs)
        self.bProgramming = Button(self.framePit, text = "Programming", bg="#B9E5EF", height=6, width=28, command=self.goToProgramming)
        self.bMechanisms = Button(self.framePit, text = "Mechanisms", bg="#B9E5EF", height=6, width=28, command=self.goToMechanisms)
        self.bMatchPre = Button(self.framePit, text = "Match Preview", bg="#B9E5EF", height=6, width=28, command=self.goToPreview)
        self.bNotes = Button(self.framePit, text = "Notes", bg="#B9E5EF", height=6, width=28, command=self.goToNotes)

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
    
    def goToRobotSpecs(self):
        self.framePit.destroy()
        toShow = RobotSpecs()
    
    def goToProgramming(self):
        self.framePit.destroy()
        toShow = Programming()
    
    def goToMechanisms(self):
        self.framePit.destroy()
        toShow = Mechanisms()
    
    def goToPreview(self):
        self.framePit.destroy()
        toShow = MatchPreview()

    def goToNotes(self):
        self.framePit.destroy()
        toShow = Notes()

test = Notes()