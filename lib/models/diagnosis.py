import re
from config.__init__ import CURSOR, CONN
class Diagnosis:

    all = {}

    def __init__(self, patient_id, description, date, diagnosis_id=None):
        self.diagnosis_id = diagnosis_id
        self.patient_id = patient_id
        self.description = description
        self.date = date

    def __repr__(self):
        return f"Diagnosis(diagnosisid={self.diagnosis_id}, patient_id={self.patient_id}, description='{self.description}', date='{self.date}')"

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Description cannot be empty")
        self._description = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):   
        if isinstance(value, str) and re.match(r'\d{4}-\d{2}-\d{2}', value):
            self._date = value
        else:
            raise ValueError("Date must be a string in the format YYYY-MM-DD")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS diagnoses (
                diagnosis_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER,
                description TEXT,
                date TEXT,
                FOREIGN KEY (patient_id) REFERENCES patients (patient_id)
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS diagnoses;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO diagnoses (patient_id, description, date)
            VALUES (?, ?, ?);
        """
        CURSOR.execute(sql, (self.patient_id, self.description, self.date))
        CONN.commit()
        self.diagnosis_id = CURSOR.lastrowid
        type(self).all[self.diagnosis_id] = self

    @classmethod
    def create(cls, patient_id, description, date):
        diagnosis = cls(patient_id, description, date)
        diagnosis.save()
        return diagnosis    
    
    def update(self):
        sql = """
            UPDATE diagnoses
            SET patient_id = ?, description = ?, date = ?
            WHERE diagnosis_id = ?;
        """
        CURSOR.execute(sql, (self.patient_id, self.description, self.date, self.diagnosis_id))
        CONN.commit()

    def delete(self):
        sql = "DELETE FROM diagnoses WHERE diagnosis_id = ?;"
        CURSOR.execute(sql, (self.diagnosis_id,))
        CONN.commit()
        del type(self).all[self.diagnosis_id]
        self.diagnosis_id = None

    @classmethod
    def instance_from_db(cls, row):
        diagnosis = cls.all.get(row[0])
        if diagnosis:
            diagnosis.patient_id = row[1]
            diagnosis.description = row[2]
            diagnosis.date = row[3]
        else:
            diagnosis = cls(row[1], row[2], row[3])
            diagnosis.diagnosis_id = row[0]
            cls.all[diagnosis.diagnosis_id] = diagnosis
        return diagnosis
    
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM diagnoses;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, diagnosis_id):
        sql = "SELECT * FROM diagnoses WHERE diagnosis_id = ?;"
        row = CURSOR.execute(sql, (diagnosis_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_patients_by_description(cls, description):
        """
        Find patients with a specific diagnosis description.
        """
        from models.patients import Patient
        sql = """
            SELECT patients.*
            FROM diagnosis
            JOIN patients ON diagnosis.patient_id = patients.patient_id
            WHERE diagnosis.description = ?
        """
        rows = CURSOR.execute(sql, (description,)).fetchall()

        return [Patient.instance_from_db(row) for row in rows]
