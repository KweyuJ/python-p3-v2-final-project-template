class Movie:
    def __init__(
        self,
        title,
        release_year,
        genre_id,
        director_id,
        duration,
        rating,
        movie_id=None,
    ):
        self.movie_id = movie_id
        self.title = title
        self.release_year = release_year
        self.genre_id = genre_id
        self.director_id = director_id
        self.duration = duration
        self.rating = rating

    def __repr__(self):
        return (
            f"Movie(movie_id={self.movie_id}, title='{self.title}', release_year={self.release_year}, "
            f"genre_id={self.genre_id}, director_id={self.director_id}, duration={self.duration}, "
            f"rating={self.rating})"
        )
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty")
        self._title = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not (0 <= value <= 10):
            raise ValueError("Rating must be between 0 and 10")
        self._rating = value
