class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_KEY='1ae99d3bc681cc606e31ddc9de6be3bb'
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True