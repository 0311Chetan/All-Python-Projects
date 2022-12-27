# -*- coding: utf-8 -*-
"""
Created on Sun May 29 18:45:27 2022

@author: HP
"""

class Tevis:
    def __init__(self):
        pass
    def status(self):
        print("--------------------------------------------------------------------------------------------")
        print("************************************the system is initiated*********************************")
        print("--------------------------------------------------------------------------------------------")
class employee(Tevis):
    def __init__(self):
        pass

class manager(employee):
    def __init__(self):
        pass
    def fetch_manager_data(self,mydb):
        print("--------------------------------------------------------------------------------------------")
        manager_name = input("Provide the manager name : ")
        manager_ID   = input("provide manager ID : ")
        
        mycursor = mydb.cursor()
        sql      = "INSERT INTO manager(manager_name,manager_ID) VALUES (%s, %s)"
        val      = (manager_name, manager_ID)
        mycursor.execute(sql, val)
        mydb.commit()
        
        print("                             THE INFOMATION IS STORED SUCCESFULLY IN DATABASE                ")
        print("--------------------------------------------------------------------------------------------")
        
        self.__manager_name = manager_name
        self.__manager_ID   = manager_ID
    def print_truck_details_to_manager(self,mydb):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT truck_number ,truck_item from truck;")
        myresult = mycursor.fetchall()
        myresult.reverse()
        
        print("--------------------------------------------------------------------------------------------")
        print('                     printing the truck details to manager                              ')
        print(    myresult[0])
        print("--------------------------------------------------------------------------------------------")        
        
    def get_truck_info(self,mydb):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT truck_number ,ticket_number from security;")
        myresult = mycursor.fetchall()
        myresult.reverse()
        print("        ",myresult[0],"      ")
        
        
    def responce_to_the_truck_driver(self,mydb):
        k=input("please enter the responce : ")
        l=input("please enter the door mumber : ")
        if (k=="allow"):
            mycursor = mydb.cursor()
            sql      = "UPDATE warehouse SET status = %s WHERE door_number = %s"
            val      = ( "grey" , l)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            print("             LED SCREEN             ")
            print(" -----------------------------------")
            print("   the truck is",k,"for unloading   ")
            print("                grey                ")
            print("------------------------------------")
            
            mycursor = mydb.cursor()
            sql = "UPDATE warehouse SET status = %s WHERE door_number = %s"
            val = ( "yellow" , l)
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record(s) affected")
            print("             LED SCREEN             ")
            print(" -----------------------------------")
            print("the truck is leaving the territory  ")
            print("                yellow              ")
            print("------------------------------------")
            
            
            
            
              
        
class security(employee):
    def __init__(self):
        pass
    def fetch_security_data(self,mydb):
        print("--------------------------------------------------------------------------------------------")
        security_name = input("Provide security name :")
        security_ID   = input("provide the security ID:")
        ticket_number = input("give the ticket number : ")
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO security(security_name,security_ID,ticket_number) VALUES (%s, %s,%s)"
        val = (security_name, security_ID,ticket_number)
        mycursor.execute(sql, val)
        mydb.commit()
        
        print("                             THE INFOMATION IS STORED SUCCESFULLY IN DATABASE                ")
        print("--------------------------------------------------------------------------------------------")
        
        
        self.__security_name = security_name
        self.__security_ID   = security_ID
        self.__ticket_number = ticket_number
        
    def get_security_details(self,mydb):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT truck_number ,ticket_number from security;")
        myresult = mycursor.fetchall()
        myresult.reverse()
        print(" the regestration of CARGO is completed")
        print("")
        print("           LED SCREEN        ")
        print(" ----------------------------")
        print("      the token provided     ")
        print("        ",myresult[0],"      ")
        print("-----------------------------")        
                
    def exit_status_of_truck(self,mydb):
        l=input("please enter the door mumber : ")
        mycursor = mydb.cursor()
        sql      = "UPDATE warehouse SET status = %s WHERE door_number = %s"
        val      = ( "green" , l)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        
        print("sucurity confrims the truck left the territory")
        print("       ready to accept the next truck         ")
        
        
class truck:
    def __init__ (self):
        pass
    def fetch_truck_data(self,mydb):
        truck_num    = input("provide the truck number      :")
        truck_name   = input("provide the truck name        :")
        truck_item   = input("provide the item in the truck :")
        Item_vender  = input("provide the item vender       :")
        
        
        mycursor = mydb.cursor()
        sql      = "INSERT INTO truck(truck_number,truck_name,truck_item,item_vender) VALUES (%s, %s,%s,%s)"
        val      = (truck_num, truck_name,truck_item,Item_vender)
        mycursor.execute(sql, val)
        mydb.commit()
        
        print("                             THE INFOMATION IS STORED SUCCESFULLY IN DATABASE                ")
        print("--------------------------------------------------------------------------------------------")
        
        
        self.truck_num     = truck_num
        self.__truck_name  = truck_name
        self.__truck_item  = truck_item
        self.__Item_vender = Item_vender
    def get_truck_details(self,mydb):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * from truck;")
        myresult = mycursor.fetchall()
        myresult.reverse()
        
        print("--------------------------------------------------------------------------------------------")
        print('                                   Printing the truck details                             ')
        print(myresult[0])
        print("--------------------------------------------------------------------------------------------")        
                       
        
class driver(truck):
    def __init__(self):
        pass
    def Fetch_driver_data(self,mydb):
        driver_name           = input("provide the driver name :")
        driver_license_number = input("provide the driver_license_number :")
        
        mycursor = mydb.cursor()
        sql      = "INSERT INTO driver(driver_name,driver_license) VALUES (%s, %s)"
        val      = (driver_name, driver_license_number)
        mycursor.execute(sql, val)
        mydb.commit()
        
        print("                             THE INFOMATION IS STORED SUCCESFULLY IN DATABASE                ")
        print("--------------------------------------------------------------------------------------------")
        
        self.__driver_license_number = driver_license_number
        self.__driver_name           = driver_name
    
    def get_driver_details(self,mydb):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * from driver;")
        myresult = mycursor.fetchall()
        myresult.reverse()
        
        print("--------------------------------------------------------------------------------------------")
        print('                                   Printing the driver details                             ')
        print(myresult[0])
        print("--------------------------------------------------------------------------------------------")        
                         
        
        
class warehouse(manager):
    def __init__(self):
        pass
    def entering_the_status_of_ramp(self,mydb):
        ramp_item   = input("provide the new ramp status : ")
        door_number = input("provide door number")
        status      = input("provide the status :")
        
        
        mycursor = mydb.cursor()
        sql = "INSERT INTO warehouse(ramp_item,door_number,status) VALUES (%s,%s, %s)"
        val = (ramp_item, door_number,status)
        mycursor.execute(sql, val)
        mydb.commit()
        
        print("                             THE INFOMATION IS STORED SUCCESFULLY IN DATABASE                ")
        print("--------------------------------------------------------------------------------------------")
        
        self.__ramp_item   = ramp_item 
        self.__door_number = door_number
        self.__status      = status
     
    def see_doc_details(self,mydb):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * from warehouse;")
        myresult = mycursor.fetchall()
        for x in myresult:
          print(x)
        
        