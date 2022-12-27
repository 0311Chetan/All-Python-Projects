import sys
sys.path.append('C:/Users/HP/Desktop/pruthviraj')
from TEVIS_CLASES import *

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Paub#1234",
  database="TEVIS"
)


mycursor = mydb.cursor()
print(mydb)

print(" please enter the below values to get acces")
print(" enter 's' if you are security ")
print(" enter 'm' if you are manager ")
print(" enter 'd' if you are driver ")
print(" enter 'w' to update the DOC status ")


while True:
    i=input("enter Employee code :")
    if (i=="d"):
        t1=truck()
        t1.fetch_truck_data(mydb)

        t1.truck_num= driver()
        t1.truck_num.Fetch_driver_data(mydb)
        
    elif (i=="s"):
        s1=security()
        print("if you want to enter your metadata press'p'")
        print("if you want to edit exit status of truck press'q'")
        p=input("please enter:")
        if (p=='p'):
            
            s1.fetch_security_data(mydb)
            s1.get_security_details(mydb)
            
        elif (p=='q'):
            s1.exit_status_of_truck(mydb)
    elif (i=="m"):
        
        m1=manager()
        
        print("if you want to enter your metadata press'1'")
        print("if you want to acces DOC press'2'")
        t=input("please enter '1' or '2' :")
        if (t=='1'):
            
            m1.fetch_manager_data(mydb)
            m1.get_truck_info(mydb)
            
        elif (t=='2'):
            m1.print_truck_details_to_manager(mydb)
            print("enter 'e' if you  want to edit doc information ")
            print("enter 's' if you  want to see doc information ")
            
            j=1
            while (j!='0'):
                w1=warehouse()
                j=input("enter  to DOC setings:")
                if (j=='e'):
                    
                    w1.entering_the_status_of_ramp(mydb)
                elif (j=='s'):
                    w1.see_doc_details(mydb)
            
            m1.responce_to_the_truck_driver(mydb)                
              
        

        
        
        
    
        