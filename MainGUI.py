#Main screen

from tkinter import *
from tkinter import messagebox as MessageBox
from turtle import goto
from LogInADjdbc import LogInADjdbc
from MainCuantiGUI import MainCuanti
import Data as dGeneral

name = " "
rol= " "
frames ={}


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
                    dGeneral.name= name
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



main = LogIn()

#test = GeneralSpecs()


