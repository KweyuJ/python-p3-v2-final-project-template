from config.__init__ import CURSOR, CONN

class Doctor:
    all = {}

    def __init__(self, name, specialization, years_of_experience, doctor_id=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.years_of_experience = years_of_experience

    def __repr__(self):
        return f"Doctor(id={self.doctor_id}, name='{self.name}', specialization='{self.specialization}', years_of_experience={self.years_of_experience})"

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
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, specialization):
        if isinstance(specialization, str) and len(specialization):
            self._specialization = specialization
        else:
            raise ValueError("Specialization must be a non-empty string")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS doctors (
                doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                specialization TEXT,
                years_of_experience INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS doctors;"
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO doctors (name, specialization, years_of_experience)
        VALUES (?, ?, ?);
        """
        CURSOR.execute(sql, (self.name, self.specialization, self.years_of_experience))
        CONN.commit()
        self.doctor_id = CURSOR.lastrowid  
        type(self).all[self.doctor_id] = self

    @classmethod
    def create(cls, name, specialization, years_of_experience):
        doctor = cls(name, specialization, years_of_experience)
        doctor.save()
        return doctor
    
    def update(self):
        sql = """
            UPDATE doctors
            SET name = ?, specialization = ?, years_of_experience = ?
            WHERE doctor_id = ?;
        """
        CURSOR.execute(sql, (self.name, self.specialization, self.years_of_experience, self.doctor_id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM doctors
            WHERE doctor_id = ?;
        """
        CURSOR.execute(sql, (self.doctor_id,))
        CONN.commit()
        del type(self).all[self.doctor_id]
        self.doctor_id = None

    @classmethod
    def instance_from_db(cls, row):
        doctor = cls.all.get(row[0])
        if doctor:
            doctor.name = row[1]
            doctor.specialization = row[2]
            doctor.years_of_experience = row[3]
        else:
            doctor = cls(row[1], row[2], row[3])
            doctor.doctor_id = row[0]  
            cls.all[doctor.doctor_id] = doctor
        return doctor

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM doctors;"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM doctors WHERE name = ?;"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_id(cls, doctor_id):
        sql = "SELECT * FROM doctors WHERE doctor_id = ?;"
        row = CURSOR.execute(sql, (doctor_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def patients(self):
        from models.patients import Patient
        sql = "SELECT * FROM patients WHERE doctor_id = ?;"
        rows = CURSOR.execute(sql, (self.doctor_id,)).fetchall()
        return [Patient.instance_from_db(row) for row in rows]
