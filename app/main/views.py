from flask import render_template,request,redirect,url_for,abort
from . import main
from ..requests import get_movies,get_movie,search_movie
from .forms import ReviewForm,UpdateProfile
from ..models import Review,User
from flask_login import login_required,current_user#login required will intercept the request and check if the user is authenticated.
from .. import db,photos

#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = 'Home - Welcome to The best Movie Review Website Online'
    search_movie = request.args.get('movie_query') #getting the search query using te function request.args.get.

    if search_movie:
         return redirect(url_for('main.search',movie_name=search_movie))
    else:
     return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie )
#dynamic route for the profile pic and it is handled by the profile view function.
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404) #abort function that stops the request.
    form=UpdateProfile() # view function that takes in the username and instantiates the updateprofile form class.
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit() 
        
        return redirect(url_for('.profile',uname=user.username))
    return render_template("profile/profile.html", form=form)      

@main.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    reviews = Review.get_reviews(movie.id)

    return render_template('movie.html',title = title,movie = movie,reviews = reviews)

@main.route('/search/<movie_name>')
def search(movie_name): #search function that will display our search items form the Api
    '''
    View function to display the search results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies) 

@main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
@login_required # a decorator 
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        #updated the review instance.
        new_review = Review(movie_id=movie.id,movie_title=title,image_path=movie.poster,movie_review=review,user=current_user)
        #save review method.
        new_review.save_review()
        return redirect(url_for('main.movie',id = movie.id ))

    title = f'{movie.title} review'
    return render_template('new_review.html',title = title, review_form=form, movie=movie)

@main.route('/user/<uname>/update/pic',methods= ['POST']) # root that will process our form submission request.
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()#query the data to pick the username that same with one pass in.
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))