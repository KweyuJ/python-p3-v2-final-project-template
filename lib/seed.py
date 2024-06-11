


from models.doctors import Doctor
from models.patients import Patient


Doctor.drop_table()
Doctor.create_table()

Patient.drop_table()
Patient.create_table()


    
doc1 = Doctor.create("Dr. Smith", "Cardiology", 15)
doc2 = Doctor.create("Dr. Jones", "Neurology", 10)



print (doc1)
    
    

