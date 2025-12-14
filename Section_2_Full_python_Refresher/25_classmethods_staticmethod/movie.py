class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating 
        
    def summary(self):
        return f"{self.title} has a rating of {self.rating}/10"
        
    @classmethod
    def from_award_winner(cls, movie):
        return cls(movie.title, movie.rating + 1)
    
    @staticmethod
    def describe_movie(movie):
        return f"Movie: {movie.title}, (Rating: {movie.rating})"
    
m1 = Movie("Inception", 8)
m2 = Movie.from_award_winner(m1)

print(m2.summary())
print(Movie.describe_movie(m1))