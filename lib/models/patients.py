from config.__init__ import CURSOR, CONN

class Patient:
    all = {}

    def __init__(self, name, age, doctor_id, patient_id=None):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.doctor_id = doctor_id

    def __repr__(self):
        return f"<Patient {self.patient_id}: {self.name}, {self.age}, {self.doctor_id}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age >= 0:
            self._age = age
        else:
            raise ValueError("Age must be a non-negative integer")

    @property
    def doctor_id(self):
        return self._doctor_id

    @doctor_id.setter
    def doctor_id(self, doctor_id):
        if isinstance(doctor_id, int) and doctor_id >= 0:
            self._doctor_id = doctor_id
        else:
            raise ValueError("Doctor ID must be a non-negative integer")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS patients (
            patient_id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            doctor_id INTEGER,
            FOREIGN KEY (doctor_id) REFERENCES doctors (doctor_id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO patients (name, age, doctor_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.age, self.doctor_id))
        CONN.commit()
        self.patient_id = CURSOR.lastrowid
        type(self).all[self.patient_id] = self

    @classmethod
    def create(cls, name, age, doctor_id):
        patient = cls(name, age, doctor_id)
        patient.save()
        return patient