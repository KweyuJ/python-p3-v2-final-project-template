class Diagnosis:
    def __init__(self, patient_id, description, date, diagnosis_id=None):
        self.diagnosis_id = diagnosis_id
        self.patient_id = patient_id
        self.description = description
        self.date = date

    def __repr__(self):
        return f"Diagnosis(id={self.diagnosis_id}, patient_id={self.patient_id}, description='{self.description}', date='{self.date}')"

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            raise ValueError("Description cannot be empty")
        self._description = value
