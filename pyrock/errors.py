class PyrockException(Exception):
    """
    The base class for all Pyrock exceptions.
    """
    pass

class RequestFailed(PyrockException):
    """
    Is raised if a request fails.
    """
    pass

class APIException(PyrockException):
    """
    Is raised if Rock API returns an error.
    """