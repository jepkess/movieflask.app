from app import app
import urllib.request,json #(urllib )help us create a connection to our API URL and send a request.
from .models import movie

Movie = movie.Movie
 # getting api key 
api_key = app.config['MOVIE_API_KEY']
# Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]

def get_movies(category): # a function that takes in a movie category as an argument.
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key) #  the final URL for our API request(get_movies_url)

    with urllib.request.urlopen(get_movies_url) as url:# function that takes in get_movies_url as an argument and send request as the url.
        get_movies_data = url.read() #read() read the response and store in the get_movies_data.
        get_movies_response = json.loads(get_movies_data)# json.load method convert the json responses to the python dictionary

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)


    return movie_results

def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    movie_results = [] #empty list that in the newly created movie 
    #looping through the list of dictionaries using the get() method.s
    for movie_item in movie_list:
        id = movie_item.get('id')
        title = movie_item.get('original_title')
        overview = movie_item.get('overview')
        poster = movie_item.get('poster_path')
        vote_average = movie_item.get('vote_average')
        vote_count = movie_item.get('vote_count')

        if poster:
            movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
            movie_results.append(movie_object)

    return movie_results    