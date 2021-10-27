class Review:
    

    all_reviews =[]
def __init__(self,movie_id,title,imageurl,review):
    self.movie.id = movie_id
    self.title = title
    self.imageurl = imageurl
    self.review= review
# method that append the review object into the empty object list-all_reviews list.
def save_review(self):
    Review.all_reviews.append(self)

@classmethod
def clear_reviews(cls): # method that clear all the items in te list.
      Review.all_reviews.clear()    
