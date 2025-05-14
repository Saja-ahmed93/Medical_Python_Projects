try:
   while True:
        menu = ["Exist", "New patient information", "Appointments", "Vital signs records"]
        
        for index, choose in enumerate(menu):
            print(index, choose)
        select = int(input("Enter a choice: "))
        
    # NEW PAITENT INFORMATION
        if select == 0:
             break
        else:
            if select == 1:
             print(menu[select])
             name = input("Enter the name of patient: ")
             age = input ("Enter the age of patient: ")
             gender = input("Enter gender: ")
             address = input("Enter the address: ")
             date_of_admission = input("Entry date: ")
             
            # Write information to CSV file:
             file = open("patient_details.csv", "a+")
             file.write("{},{},{},{},{}\n".format(name, age, gender, address, date_of_admission))
             file.close()
             print("\nThe information saved successfully!\n")
             
        # APPOINTEMENTS:
            elif select == 2:
                print(menu[select])
                
                appo = ["Back","New appointment", "Previous appointments"] 
                for index,selection in enumerate(appo):
                 print(index,selection)
                sel = int(input("Enter a choice: "))
                if sel == 1:
                    specialist = {"Sugery: Dr.Adam", "Medicine: Dr.Khalid", "ENT: Dr.Sara", "Dermatology: Dr.Eman"}
                    for index, field in enumerate(specialist):
                        print(index+1, field)
                if sel == 2:
                    print("\n You don't have any previous appointments \n")
        
        #VITAL SIGNS RECORDS        
            elif select == 3:
                print(menu[select])
                print("Do general examination and add the following vial signs:")
                temp = input("Temperture: ")
                pressure = input("Blood Pressure: ")
                respiration = input("Respiratory Rate: ")
                pulsation = input("Pulse rate: ")
                
                vital_signs = open("patient_details.csv", "a+")
                vital_signs.write("{},{},{},{}".format(temp, pressure, respiration, pulsation))
                vital_signs.close()
                
            else:
                print("Nothing here. Try another number")
            
    
except Exception as error:
    print(error)