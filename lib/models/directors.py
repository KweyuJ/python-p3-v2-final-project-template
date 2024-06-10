class Director:
    def __init__(self, name, bio, birth_year, director_id=None):
        self.director_id = director_id
        self.name = name
        self.bio = bio
        self.birth_year = birth_year

    def __repr__(self):
        return f"Director(id={self.director_id}, name='{self.name}', bio='{self.bio}', birth_year={self.birth_year})"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
