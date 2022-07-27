class PyrockException(Exception):
    """
    The base class for all Pyrock exceptions.
    """
    pass

class RequestFailed(PyrockException):
    """
    Is called if a request fails.
    """
    pass

class APIException(PyrockException):
    """
    Is called if the API returns an error.
    """