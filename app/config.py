class config: # class that contains configurations that are used in both dev and prod.
    """
    General configuration parent class 
    """
    pass
class prodconfig(config):
    """
     Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    pass
class Devconfig(config): 
    """
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    pass


    DEBUG=True