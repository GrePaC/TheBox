#Main screen

from tkinter import *
from tkinter import messagebox as MessageBox
from LogInADjdbc import LogInADjdbc



class LogIn :
    
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
        
        self.bLogIn = Button(self.frame, text="Log In", bg="#84EC5F", command=self.blogInFunction)

        #Position the components
   
        self.tfUser.place(relx = 0.5,rely = 0.5, anchor = CENTER)

        self.tfPassword.place(x = 410,y = 395)

        self.bLogIn.place(x = 540,y = 450)

        self.frame.mainloop()

    #Log In functions  

    def redirectMain(self, role):

        if(role == "Cuanti"):
            
            self.frame.destroy()
            exec(open("MainCuanti.py").read())
            
            

    def obtenerDatos(self):

        user = self.tfUser.get()
        password = self.tfPassword.get()

        if user == "Username" or password == "Password":

            datos = "VACIO"
        else:

            datos= user +","+ password
        
        return datos
    
    def blogInFunction(self):
        
        datos=self.obtenerDatos()
        
        if(datos != "VACIO"):

            data = datos.split(",")
            result = self.adminLogIn.startApp(data)

            if(result == 1):
                
                print("ERROR connecting to database")
                MessageBox.showinfo("Alert", "ERROR connecting to database")

            elif(result == 0):

                print("Wrong credentials")
                MessageBox.showinfo("Alert", "Wrong credentials")

            else:

                print("El rol del usuario es: "+ result)
                self.redirectMain(result)

login = LogIn()
