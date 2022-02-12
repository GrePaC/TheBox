import mysql.connector
import Data as dGeneral
class GeneralADjdbc:

    def saveData(self, data):
        try:
            db_connection = mysql.connector.connect(host=dGeneral.HOST,database = dGeneral.DATABASE, user= dGeneral.USER, password = dGeneral.PASSWORD )
            query= "INSERT INTO General VALUES (" + data[0] + "," + data[1] + "," + data[2] +")"
           
            statement = db_connection.cursor()
            statement.execute(query)
            db_connection.commit()
            
            
            statement.close()
            db_connection.close()
            try:
                db_connection = mysql.connector.connect(host=dGeneral.HOST,database = dGeneral.DATABASE, user= dGeneral.USER, password = dGeneral.PASSWORD )
                query= "UPDATE Equipo SET scouter= '"+dGeneral.name + "' WHERE numero ="+data[0]

                statement = db_connection.cursor()
                statement.execute(query)
                db_connection.commit()
                
                
                statement.close()
                db_connection.close()
                return 1
            except:
                return 0
        except:
            return 0
    
    def saveRobotSpecs(self, data):
            try:
                db_connection = mysql.connector.connect(host=dGeneral.HOST,database = dGeneral.DATABASE, user= dGeneral.USER, password = dGeneral.PASSWORD )
                query= "INSERT INTO Specs VALUES (" + str(data[0]) + "," + str(data[1]) + "," + str(data[2])+ "," + str(data[3]) +"," + str(data[4]) + "," + str(data[5])+ ","+ str(data[6])+ ","+ str(data[7])+")"
                statement = db_connection.cursor()
                statement.execute(query)
                db_connection.commit()
                statement.close()
                db_connection.close()
                return True
            except:
                return False
    
    def saveProgramming(self, data):
        try:
            db_connection = mysql.connector.connect(host=dGeneral.HOST,database = dGeneral.DATABASE, user= dGeneral.USER, password = dGeneral.PASSWORD )
            query= "INSERT INTO Programming VALUES (" + str(data[0]) + "," + str(data[1]) + "," + str(data[2])+ "," + str(data[3]) +"," + str(data[4]) + "," + str(data[5])+ ","+ str(data[6])+ ","+ str(data[7])+ ","+ str(data[8])+ ","+ str(data[9])+ ","+ str(data[10])+ ","+ str(data[11])+")"
            print(query)
            statement = db_connection.cursor()
            statement.execute(query)
            db_connection.commit()
            statement.close()
            db_connection.close()
            return True
        except:
            return False
    
    def saveMechanisms(self, data):
        try:
            db_connection = mysql.connector.connect(host=dGeneral.HOST,database = dGeneral.DATABASE, user= dGeneral.USER, password = dGeneral.PASSWORD )
            query= "INSERT INTO Mecanismo VALUES (" + str(data[0]) + "," + str(data[1]) + "," + str(data[2])+ "," + str(data[3]) +"," + str(data[4]) + "," + str(data[5])+ ","+ str(data[6])+ ","+ str(data[7])+ ","+ str(data[8]) +")"
            print(query)
            statement = db_connection.cursor()
            statement.execute(query)
            db_connection.commit()
            statement.close()
            db_connection.close()
            return True
        except:
            return False

    def savePreview(self, data):
        try:
            db_connection = mysql.connector.connect(host=dGeneral.HOST,database = dGeneral.DATABASE, user= dGeneral.USER, password = dGeneral.PASSWORD )
            query= "INSERT INTO PartidoPre VALUES (" + str(data[0]) + "," + str(data[1]) + "," + str(data[2])+ "," + str(data[3])+ "," + str(data[4]) +")"
           
            statement = db_connection.cursor()
            statement.execute(query)
            db_connection.commit()
            
            
            statement.close()
            db_connection.close()
            try:
                db_connection = mysql.connector.connect(host=dGeneral.HOST,database = dGeneral.DATABASE, user= dGeneral.USER, password = dGeneral.PASSWORD )
                query= "UPDATE Equipo SET prioridad= '"+str(data[5])+ "' WHERE numero ="+data[0]

                statement = db_connection.cursor()
                statement.execute(query)
                db_connection.commit()
                
                
                statement.close()
                db_connection.close()
                return 1
            except:
                return 0
        except:
            return 0

    def saveNotes(self, data):
        try:
            db_connection = mysql.connector.connect(host=dGeneral.HOST,database = dGeneral.DATABASE, user= dGeneral.USER, password = dGeneral.PASSWORD )
            query= f"UPDATE Equipo SET notePit= '{str(data[1])}' AND pitScouting = 1 WHERE numero ="+data[0]
            print(query)
            statement = db_connection.cursor()
            statement.execute(query)
            db_connection.commit()
            statement.close()
            db_connection.close()
            return True
        except:
            return False

