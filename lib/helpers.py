from models.doctors import Doctor
from models.patients import Patient
from models.diagnosis import Diagnosis

def exit_program():
    print("Exiting program.")
    exit()

def list_doctors():
    doctors = Doctor.get_all()
    for doctor in doctors:
        print(doctor)

def find_doctor_by_name():
    name = input("Enter the doctor's name: ")
    doctor = Doctor.find_by_name(name)
    if doctor:
        print(doctor)
    else:
        print(f"No doctor found with name {name}")

def find_doctor_by_id():
    doctor_id = int(input("Enter the doctor's id: "))
    doctor = Doctor.find_by_id(doctor_id)
    if doctor:
        print(doctor)
    else:
        print(f"No doctor found with id {doctor_id}")

def create_doctor():
    name = input("Enter the doctor's name: ")
    specialization = input("Enter the doctor's specialization: ")
    years_of_experience = int(input("Enter the doctor's years of experience: "))
    doctor = Doctor.create(name, specialization, years_of_experience)
    print(f"Created doctor: {doctor}")

def update_doctor():
    doctor_id = int(input("Enter the doctor's id to update: "))
    doctor = Doctor.find_by_id(doctor_id)
    if doctor:
        doctor.name = input("Enter the doctor's new name: ")
        doctor.specialization = input("Enter the doctor's new specialization: ")
        doctor.years_of_experience = int(input("Enter the doctor's new years of experience: "))
        doctor.update()
        print(f"Updated doctor: {doctor}")
    else:
        print(f"No doctor found with id {doctor_id}")

def delete_doctor():
    doctor_id = int(input("Enter the doctor's id to delete: "))
    doctor = Doctor.find_by_id(doctor_id)
    if doctor:
        doctor.delete()
        print(f"Deleted doctor with id {doctor_id}")
    else:
        print(f"No doctor found with id {doctor_id}")

def list_patients():
    patients = Patient.get_all()
    for patient in patients:
        print(patient)

def find_patient_by_name():
    name = input("Enter the patient's name: ")
    patient = Patient.find_by_name(name)
    if patient:
        print(patient)
    else:
        print(f"No patient found with name {name}")

def find_patient_by_id():
    patient_id = int(input("Enter the patient's id: "))
    patient = Patient.find_by_id(patient_id)
    if patient:
        print(patient)
    else:
        print(f"No patient found with id {patient_id}")

def create_patient():
    name = input("Enter the patient's name: ")
    age = int(input("Enter the patient's age: "))
    gender = input("Enter the patient's gender (Male, Female, Other): ")
    weight = float(input("Enter the patient's weight: "))
    doctor_id = int(input("Enter the patient's doctor id: "))
    patient = Patient.create(name, age, gender, weight, doctor_id)
    print(f"Created patient: {patient}")

def update_patient():
    patient_id = int(input("Enter the patient's id to update: "))
    patient = Patient.find_by_id(patient_id)
    if patient:
        patient.name = input("Enter the patient's new name: ")
        patient.age = int(input("Enter the patient's new age: "))
        patient.gender = input("Enter the patient's new gender (Male, Female, Other): ")
        patient.weight = float(input("Enter the patient's new weight: "))
        patient.doctor_id = int(input("Enter the patient's new doctor id: "))
        patient.update()
        print(f"Updated patient: {patient}")
    else:
        print(f"No patient found with id {patient_id}")

def delete_patient():
    patient_id = int(input("Enter the patient's id to delete: "))
    patient = Patient.find_by_id(patient_id)
    if patient:
        patient.delete()
        print(f"Deleted patient with id {patient_id}")
    else:
        print(f"No patient found with id {patient_id}")

def list_diagnoses():
    diagnoses = Diagnosis.get_all()
    for diagnosis in diagnoses:
        print(diagnosis)

def find_diagnosis_by_patient_id():
    patient_id = int(input("Enter the patient's id: "))
    diagnoses = Diagnosis.find_by_patient_id(patient_id)
    if diagnoses:
        for diagnosis in diagnoses:
            print(diagnosis)
    else:
        print(f"No diagnoses found for patient id {patient_id}")

def create_diagnosis():
    patient_id = int(input("Enter the patient's id: "))
    description = input("Enter the diagnosis description: ")
    date = input("Enter the diagnosis date (YYYY-MM-DD): ")
    diagnosis = Diagnosis.create(patient_id, description, date)
    print(f"Created diagnosis: {diagnosis}")

def update_diagnosis():
    diagnosis_id = int(input("Enter the diagnosis id to update: "))
    diagnosis = Diagnosis.find_by_patient_id(diagnosis_id)
    if diagnosis:
        diagnosis.patient_id = int(input("Enter the new patient id: "))
        diagnosis.description = input("Enter the new diagnosis description: ")
        diagnosis.date = input("Enter the new diagnosis date (YYYY-MM-DD): ")
        diagnosis.update()
        print(f"Updated diagnosis: {diagnosis}")
    else:
        print(f"No diagnosis found with id {diagnosis_id}")

def delete_diagnosis():
    diagnosis_id = int(input("Enter the diagnosis id to delete: "))
    diagnosis = Diagnosis.find_by_id(diagnosis_id)
    if diagnosis:
        diagnosis.delete()
        print(f"Deleted diagnosis with id {diagnosis_id}")
    else:
        print(f"No diagnosis found with id {diagnosis_id}")