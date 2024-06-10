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
