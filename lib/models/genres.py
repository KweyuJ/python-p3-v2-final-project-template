class Genre:
    def __init__(self, name, description, genre_id=None):
        self.genre_id = genre_id
        self.name = name
        self.description = description

    def __repr__(self):
        return (
            f"Genre(id={self.genre_id}, name='{self.name}', description='{self.description}')"
        )
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
