class Doctor:
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
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
