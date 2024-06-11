from models.doctors import Doctor
from models.patients import Patient
from models.diagnosis import Diagnosis


Doctor.drop_table()
Doctor.create_table()

Patient.drop_table()
Patient.create_table()

Diagnosis.drop_table()
Diagnosis.create_table()


# Creating seed data for my tables

# Seed data for doctors
doc1 = Doctor.create("Dr. Joy Kweyu", "Paedriatics", 15)
doc2 = Doctor.create("Dr. Jones Smith", "Neurology", 10)
doc3 = Doctor.create("Dr. Maurine Khalwale", "Gynecologist", 13)
doc4 = Doctor.create("Dr. Warren Wambura", "General Surgery", 7)
doc5 = Doctor.create("Dr. Jane Lee", "Dermatology", 8)
print(doc1)
print(doc2)



# Seed data for patients
patient1 = Patient.create("Jael Atuo", 40,"Female",80, doc3.doctor_id)
patient2 = Patient.create("Kennedy Brooks", 50,"Male", 90, doc2.doctor_id)
patient3 = Patient.create("Emily Brown", 25,"Female",57, doc4.doctor_id)
patient4 = Patient.create("Arnold Kweyu", 9,"Male",12, doc1.doctor_id)
patient5 = Patient.create("Ivy Anderson", 29,"Female",65, doc5.doctor_id)
print(patient1)


# Seed data for diagnosis

diagnosis1 = Diagnosis.create(patient1.patient_id, "Endometriosis", "2024-04-01")
diagnosis2 = Diagnosis.create(patient2.patient_id, "Stroke", "2020-06-14")
diagnosis3 = Diagnosis.create(patient3.patient_id, "Inguinal Hernia", "2019-12-08")
diagnosis4 = Diagnosis.create(patient4.patient_id, "Fever", "2023-08-20")
diagnosis5 = Diagnosis.create(patient5.patient_id, "Atopic dermatitis", "2018-10-03")

print (diagnosis1)



