from helpers import (
    exit_program,
    list_doctors,
    find_doctor_by_name,
    find_doctor_by_id,
    create_doctor,
    update_doctor,
    delete_doctor,
    list_patients,
    find_patient_by_name,
    find_patient_by_id,
    create_patient,
    update_patient,
    delete_patient,
    list_diagnoses,
    find_diagnosis_by_patient_id,
    create_diagnosis,
    update_diagnosis,
    delete_diagnosis
)

def print_menu():
    menu = """
    1. List all doctors
    2. Find doctor by name
    3. Find doctor by ID
    4. Create a new doctor
    5. Update a doctor
    6. Delete a doctor
    7. List all patients
    8. Find patient by name
    9. Find patient by ID
    10. Create a new patient
    11. Update a patient
    12. Delete a patient
    13. List all diagnoses
    14. Find diagnoses by patient ID
    15. Create a new diagnosis
    16. Update a diagnosis
    17. Delete a diagnosis
    18. Exit
    """
    print(menu)

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            list_doctors()
        elif choice == '2':
            find_doctor_by_name()
        elif choice == '3':
            find_doctor_by_id()
        elif choice == '4':
            create_doctor()
        elif choice == '5':
            update_doctor()
        elif choice == '6':
            delete_doctor()
        elif choice == '7':
            list_patients()
        elif choice == '8':
            find_patient_by_name()
        elif choice == '9':
            find_patient_by_id()
        elif choice == '10':
            create_patient()
        elif choice == '11':
            update_patient()
        elif choice == '12':
            delete_patient()
        elif choice == '13':
            list_diagnoses()
        elif choice == '14':
            find_diagnosis_by_patient_id()
        elif choice == '15':
            create_diagnosis()
        elif choice == '16':
            update_diagnosis()
        elif choice == '17':
            delete_diagnosis()
        elif choice == '18':
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
