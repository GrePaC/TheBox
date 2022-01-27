import hashlib
from unittest import result


import mysql.connector

class LogInADjdbc:

    def startApp(self, data):
        data[1]=data[1].encode('utf-8')
        h=hashlib.new("sha256",data[1])
        
        HOST = "scouting-db.cyeuqx4nk3mi.us-east-2.rds.amazonaws.com"
        USER = "admin"
        PASSWORD = "steamex6832"
        DATABASE = "SiaBox"
        
        try:
            db_connection = mysql.connector.connect(host=HOST,database = DATABASE, user= USER, password = PASSWORD )


            query= "SELECT * FROM Scouter WHERE name ='"+ data[0] + "' AND password = '"+ h.hexdigest()+"'"

            statement = db_connection.cursor()
            statement.execute(query)

            tupla = statement.fetchone()

            statement.close()
            db_connection.close()
            try:

                if(len(tupla) == 3):
                    return tupla[2]
            except:

                return 0
        except:
            return 1
        

        
