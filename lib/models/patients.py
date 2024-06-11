class Patient:
    def __init__(self, name, age, doctor_id, patient_id=None):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.doctor_id = doctor_id

    def __repr__(self):
        return f"Patient(id={self.patient_id}, name='{self.name}', age={self.age}, doctor_id={self.doctor_id})"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
