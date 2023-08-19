from utils.DateFormat import DateFormat 

class Movie():
    
    def __init__(self, movie_id, title=None, duration=None, released=None):
        self.movie_id = movie_id
        self.title = title
        self.duration = duration
        self.released = released
        
    def to_JSON(self):
        return{

            'id' : self.movie_id,
            'title' : self.title,
            'duration' : self.duration,
            'released' : DateFormat.convert_date(self.released)
        }