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

    @property
    def years_of_experience(self):
        return self._years_of_experience

    @years_of_experience.setter
    def years_of_experience(self, years):
        if isinstance(years, int) and years >= 0:
            self._years_of_experience = years
        else:
            raise ValueError("Years of experience must be a non-negative integer")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS doctors (
                doctor_id INTEGER PRIMARY KEY,
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

    @classmethod
    def create(cls, name, specialization, years_of_experience):
        sql = """
            INSERT INTO doctors (name, specialization, years_of_experience)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (name, specialization, years_of_experience))
        CONN.commit()
        return cls(name, specialization, years_of_experience, CURSOR.lastrowid)
