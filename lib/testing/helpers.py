# lib/helpers.py

# def helper_1():
#     print("Performing useful function#1.")

# lib/helpers.py

def exit_program():
    print("Goodbye!")
    exit()

from models.doctors import Doctor
from models.patients import Patient
from models.diagnosis import Diagnosis

# Doctor functions
def list_doctors():
    doctors = Doctor.get_all()
    for doctor in doctors:
        print(doctor)

def find_doctor_by_name():
    name = input("Enter the doctor's name: ")
    doctor = Doctor.find_by_name(name)
    print(doctor) if doctor else print(f'Doctor {name} not found')

def find_doctor_by_id():
    id_ = input("Enter the doctor's id: ")
    doctor = Doctor.find_by_id(id_)
    print(doctor) if doctor else print(f'Doctor {id_} not found')

def create_doctor():
    name = input("Enter the doctor's name: ")
    specialization = input("Enter the doctor's specialization: ")
    experience = input("Enter the doctor's years of experience: ")
    try:
        doctor = Doctor.create(name, specialization, experience)
        print(f'Success: {doctor}')
    except Exception as exc:
        print("Error creating doctor: ", exc)

def update_doctor():
    id_ = input("Enter the doctor's id: ")
    if doctor := Doctor.find_by_id(id_):
        try:
            name = input("Enter the doctor's new name: ")
            doctor.name = name
            specialization = input("Enter the doctor's new specialization: ")
            doctor.specialization = specialization
            experience = input("Enter the doctor's new years of experience: ")
            doctor.years_of_experience = experience

            doctor.update()
            print(f'Success: {doctor}')
        except Exception as exc:
            print("Error updating doctor: ", exc)
    else:
        print(f'Doctor {id_} not found')

def delete_doctor():
    id_ = input("Enter the doctor's id: ")
    if doctor := Doctor.find_by_id(id_):
        doctor.delete()
        print(f'Doctor {id_} deleted')
    else:
        print(f'Doctor {id_} not found')

# Patient functions
def list_patients():
    patients = Patient.get_all()
    for patient in patients:
        print(patient)

def find_patient_by_name():
    name = input("Enter the patient's name: ")
    patient = Patient.find_by_name(name)
    print(patient) if patient else print(f'Patient {name} not found')   

def find_patient_by_id():
    id_ = input("Enter the patient's id: ")
    patient = Patient.find_by_id(id_)
    print(patient) if patient else print(f'Patient {id_} not found')  

def create_patient():
    name = input("Enter the patient's name: ")
    age = input("Enter the patient's age: ")
    gender = input("Enter the patient's gender: ")
    weight = input("Enter the patient's weight: ")
    doctor_id = input("Enter the doctor's id :")

    try:
        patient = Patient.create(name, age, gender, weight, doctor_id)
        print(f'Success: {patient}')
    except Exception as exc:
        print("Error creating patient: ", exc)  

def update_patient():
    id_ = input("Enter the patient's id: ")
    if patient := Patient.find_by_id(id_):
        try:
            name = input("Enter the patient's new name: ")
            patient.name = name
            age = input("Enter the patient's new age: ")
            patient.age = age
            gender = input("Enter the patient's new gender: ")
            patient.gender = gender
            weight = input("Enter the patient's new weight: ")
            patient.weight = weight
            doctor_id = input("Enter the patient's new doctor id: ")
            patient.doctor_id = doctor_id

            patient.update()
            print(f'Success: {patient}')
        except Exception as exc:
            print("Error updating patient: ", exc)
    else:
        print(f'Patient {id_} not found')

def delete_patient():
    id_ = input("Enter the patient's id: ")
    if patient := Patient.find_by_id(id_):
        patient.delete()
        print(f'Patient {id_} deleted')
    else:
        print(f'Patient {id_} not found')

# Diagnosis functions
def list_diagnoses():
    diagnoses = Diagnosis.get_all()
    for diagnosis in diagnoses:
        print(diagnosis)

def find_diagnosis_by_patient_id():
    patient_id = input("Enter the patient's id: ")
    diagnoses = Diagnosis.find_by_patient_id(patient_id)
    if diagnoses:
        for diagnosis in diagnoses:
            print(diagnosis)
    else:
        print(f'No diagnoses found for patient id {patient_id}')

def create_diagnosis():
    patient_id = input("Enter the patient's id: ")
    doctor_id = input("Enter the doctor's id: ")
    condition = input("Enter the diagnosis condition: ")
    treatment = input("Enter the treatment: ")
    try:
        diagnosis = Diagnosis.create(patient_id, doctor_id, condition, treatment)
        print(f'Success: {diagnosis}')
    except Exception as exc:
        print("Error creating diagnosis: ", exc)

def update_diagnosis():
    id_ = input("Enter the diagnosis id: ")
    if diagnosis := Diagnosis.find_by_id(id_):
        try:
            condition = input("Enter the new diagnosis condition: ")
            diagnosis.condition = condition
            treatment = input("Enter the new treatment: ")
            diagnosis.treatment = treatment

            diagnosis.update()
            print(f'Success: {diagnosis}')
        except Exception as exc:
            print("Error updating diagnosis: ", exc)
    else:
        print(f'Diagnosis {id_} not found')

def delete_diagnosis():
    id_ = input("Enter the diagnosis id: ")
    if diagnosis := Diagnosis.find_by_id(id_):
        diagnosis.delete()
        print(f'Diagnosis {id_} deleted')
    else:
        print(f'Diagnosis {id_} not found')






