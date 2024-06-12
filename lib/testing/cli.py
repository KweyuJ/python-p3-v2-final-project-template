# lib/cli.py

from lib.testing.helpers import (
    exit_program,
    helper_1
)


# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             helper_1()
#         else:
#             print("Invalid choice")


# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. Some useful function")


# if __name__ == "__main__":
#     main()




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
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_doctors()
        elif choice == "2":
            find_doctor_by_name()
        elif choice == "3":
            find_doctor_by_id()
        elif choice == "4":
            create_doctor()
        elif choice == "5":
            update_doctor()
        elif choice == "6":
            delete_doctor()
        elif choice == "7":
            list_patients()
        elif choice == "8":
            find_patient_by_name()
        elif choice == "9":
            find_patient_by_id()
        elif choice == "10":
            create_patient()
        elif choice == "11":
            update_patient()
        elif choice == "12":
            delete_patient()
        elif choice == "13":
            list_diagnoses()
        elif choice == "14":
            find_diagnosis_by_patient_id()
        elif choice == "15":
            create_diagnosis()
        else:
            print("Invalid choice. Please select a valid option.")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all doctors")
    print("2. Find doctor by name")
    print("3. Find doctor by id")
    print("4. Create doctor")
    print("5. Update doctor")
    print("6. Delete doctor")
    print("7. List all patients")
    print("8. Find patient by name")
    print("9. Find patient by id")
    print("10. Create patient")
    print("11. Update patient")
    print("12. Delete patient")
    print("13. List all diagnoses")
    print("14. Find diagnosis by patient id")
    print("15. Create diagnosis")

if __name__ == "__main__":
    main()
