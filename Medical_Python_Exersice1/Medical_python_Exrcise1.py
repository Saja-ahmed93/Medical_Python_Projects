#Exercise 1: Create a program that takes a patient's name, age, and diagnosis as strings. 
# Concatenate these strings to form a patient summary.


patient_name = input(" Enter patient's Name: ")
age = input("Age of the patient: ")
diagnosis = input("Clinical Diagnosis: ")

summary = f'Patient: {patient_name}, Age: {age}, Diagnosis: {diagnosis}'

print(summary)

#Exercise 2: Create a list of patient IDs. 
# Write a function to add a new patient ID to the list and another function to remove a patient ID from the list.



# ADD a New patient ID:

patient_ids = ["PID001", "PID002", "PID003"]

def add_id(new_id):
    patient_ids.append(new_id)
    
# Remove a patient ID:

def remove_id(re_id):
    if re_id  in patient_ids:
        patient_ids.remove(re_id)
    else:
        print(f'Patient ID {re_id} is not found.')
  
        

new_id = input("Add new ID patient: ")
add_id(new_id)
print(patient_ids)


re_id = input("Add the ID that you want to remove: ")
remove_id(re_id)
print(patient_ids)


#Exercise3: Create a dictionary to store patient information (name, age, diagnosis). 
# Write a function to update the patient's diagnosis.

patient = {
    'name': 'Jhon Doe',
    'age': '35',
    'Diagnosis': 'Diabetes'
}

print(patient)

def update_diagnosis(patient, new_diagnosis):
    patient['Diagnosis'] = new_diagnosis

update_diagnosis(patient,  'Hypertension')

print(patient)


# Exercise4: Create a tuple to store coordinates (e.g., latitude and longitude) of a hospital. 
# Demonstrate how to access the elements of the tuple.

hospital_coordinates = (34.0522, -118.2437)

print(hospital_coordinates)

hospital_latitude = hospital_coordinates[0]
print("Latitude:", hospital_latitude)

hospital_longitude = hospital_coordinates[1]
print("Longitude:", hospital_longitude)


# # Create a module with a function that calculates the Body Mass Index (BMI) given weight (kg) and height (m). 
# # Import this module and use the function to calculate the BMI of a patient.

from bmi_module import BMI_calculator as bmi
weight = float(input("Enter patient weight: "))
height = float(input("Enter patient height: "))
body_mass_index = bmi(weight, height)
print(body_mass_index)


# #Exercise5: Create a CSV file containing patient data (name, age, diagnosis). 
# # Write a program to read the CSV file and print the data.

# # Writing CSV file

import csv
with open('patient_data.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerow(['name', 'age', 'diagnosis'])
    csv_writer.writerow(['Ali', '34', 'common cold'])
    csv_writer.writerow(['Sami', '20', 'Diabetes'])


# # Reading CSV file
import csv
with open('patient_data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        print(line)
        

# Exercise6: Create a class called Patient with attributes such as name, age, and diagnosis. 
# Include methods to update the diagnosis and display patient information. 
# Create instances of the Patient class and demonstrate the use of these methods.

class patient:
    def __init__(self, name, age, diagnosis):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        
    def update_diagnosis(self, new_diagnosis):
        self.diagnosis = new_diagnosis
    
    def patient_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Diagnosis:", self.diagnosis)
        
patient1 = patient("Ahmed", 45, "Hypertension")
patient2 = patient("Ali", 30, "Severe Malaria")
        
        
print(patient1.patient_info())
(patient2.update_diagnosis("Malaria Resolved"))
print(patient2.patient_info())


