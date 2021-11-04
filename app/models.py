from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id): # call back function that retrieves a user when a unique identifier is passed.
    return User.query.get(int(user_id))
class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = "https://image.tmdb.org/t/p/w500/" + poster
        self.vote_average = vote_average
        self.vote_count = vote_count



class Review:

    all_reviews = []

    def __init__(self,movie_id,title,imageurl,review):
        self.movie_id = movie_id
        self.title = title
        self.imageurl = imageurl
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response
class User(UserMixin,db.Model): #db.model connect class to the database and allow communication.
    __tablename__ = 'users'# tablename gives allows us to give the tables proper names. 
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    reviews=db.relationship('Review',backref='user',lazy="dynamic")
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255)) #column for bio 
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)    
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)



    def __repr__(self):
        return f'User {self.username}'     

                

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

class Review(db.Model): #db.model creates the connection to our database.
    __tablename__ = 'reviews'

    
    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted=db.Column(db.DateTime,default=datetime.utcnow) # gets the current time  and saves it to our database.    
    user_id=db.Column(db.Integer,db.ForeignKey("users.id")) # we use the foreign key column to store the id of the users they wrote the review.

    def save_review(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(movie_id=id).all()
        return reviews    
# class User(db.Model):
#     __tablename__ = 'users'

#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255))
    


#     def __repr__(self):
#         return f'User {self.username}'


# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer,primary_key = True)
#     name = db.Column(db.String(255))
   


    # def __repr__(self):
    #     return f'User {self.name}'   









        
                             