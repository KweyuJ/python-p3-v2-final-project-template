# Phase 3 CLI+ORM Project 

# PROJECT TITLE: (MEDICAL RECORD MANAGEMENT SYSTEM)

#### Date, 2024/06/13

#### By *KWEYU JOY AYIEKO*

## Description
A Python CLI application that helps manage patient records, including their diagnoses and the doctors responsible for their treatment. The system allows users to add, view, delete, and find doctors, patients, and diagnoses, offering an efficient way to handle medical records.



## MINIMAL VIABLE PRODUCT(MVP)

###   1.Database Management with ORM Methods

Implemented a database using Python ORM methods to handle data storage and manipulation.
The data model includes three primary classes: Doctor, Patient, and Diagnosis.
Established one-to-many relationships where each doctor can have multiple patients, and each patient can have multiple diagnoses.

###    2.Data Model Requirements

Doctor class
Attributes: doctor_id (primary key), name, specialization, and years_of_experience.
Patient class
Attributes: patient_id (primary key), name, age, doctor_id (foreign key).
Diagnosis class
Attributes: diagnosis_id (primary key), patient_id (foreign key), description, and date.
Property methods to add constraints to ensure valid data entry.
ORM methods for each class to create, delete, get all, and find by name.

###    3.CLI Requirements

A user-friendly CLI that displays interactive menus for users to navigate through the application.
Options for each class to create an object, delete an object, display all objects, view related objects, and find an object by attribute.
User input validation and informative error messages to guide users through the process.
The CLI will use loops to keep the user in the application until they choose to exit.

## Installation
1.Clone the repository

2.Navigate to the project directory

3.Install required dependencies:
    -pipenv install
    -pipenv shell

4.To start the CLI application, run:
    python3 cli.py

## PROJECT STRUCTURE

=> testing/cli.py: The entry point for the CLI application. Manages the main menu and user interactions.
=> testing/helpers.py: Contains helper functions to support the main functionality of the CLI. These include operations like listing, finding, creating, updating, and deleting records for doctors, patients, and diagnoses.

=> models/doctor.py: Contains the Doctor class and its methods for database operations.
=> models/patient.py: Contains the Patient class and its methods for database operations.
=> models/diagnosis.py: Contains the Diagnosis class and its methods for database operations.

=> lib/seed.py: Populates the database with initial seed data for doctors, patients, and diagnoses. Useful for testing and development purposes.
=> config/__init__.py: Contains database connection setup.

=>db/hospital.db :SQLite database file where all the data for the Medical Record Management System is stored. This includes information about doctors, patients, and diagnoses.

## Technologies used
-Python 3.x
-SQLite

## Support and contact details
github.com/KweyuJ

### License
The content of this site is licensed under the MIT license
Copyright (c) 2024.




