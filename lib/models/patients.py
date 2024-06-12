from config import CURSOR, CONN

class Patient:
    all = {}

    def __init__(self, name, age, gender, weight, doctor_id, patient_id=None):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        self.doctor_id = doctor_id

    def __repr__(self):
        return f"<Patient {self.patient_id}: name={self.name}, age={self.age}, gender={self.gender}, weight={self.weight}, doctor_id={self.doctor_id}>"

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
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if gender in ("Male", "Female", "Other"):
            self._gender = gender
        else:
            raise ValueError("Gender must be 'Male', 'Female', or 'Other'")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if isinstance(weight, (int, float)) and weight >= 0:
            self._weight = weight
        else:
            raise ValueError("Weight must be a non-negative number")

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
            patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            weight REAL,
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
            INSERT INTO patients (name, age, gender, weight, doctor_id)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(
            sql, (self.name, self.age, self.gender, self.weight, self.doctor_id)
        )
        CONN.commit()
        self.patient_id = CURSOR.lastrowid
        type(self).all[self.patient_id] = self

    @classmethod
    def create(cls, name, age, gender, weight, doctor_id):
        patient = cls(name, age, gender, weight, doctor_id)
        patient.save()
        return patient

    def update(self):
        sql = """
            UPDATE patients
            SET name = ?, age = ?, gender = ?, weight = ?, doctor_id = ?
            WHERE patient_id = ?;
        """
        CURSOR.execute(sql, (self.name, self.age, self.gender, self.weight, self.doctor_id, self.patient_id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM patients WHERE patient_id = ?;"
        CURSOR.execute(sql, (self.patient_id,))
        CONN.commit()
        del type(self).all[self.patient_id]
        self.patient_id = None

    @classmethod
    def instance_from_db(cls, row):
        patient = cls.all.get(row[0])
        if patient:
            patient.patient_id = row[0]
            patient.name = row[1]
            patient.age = row[2]
            patient.gender = row[3]
            patient.weight = row[4]
            patient.doctor_id = row[5]
        else:
            patient = cls(row[1], row[2], row[3], row[4], row[5], patient_id=row[0])
            cls.all[patient.patient_id] = patient
        return patient

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM patients;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM patients WHERE name = ?;"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_id(cls, patient_id):
        sql = "SELECT * FROM patients WHERE patient_id = ?;"
        row = CURSOR.execute(sql, (patient_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
