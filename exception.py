

class APIException(Exception):
    """
    Raise Exception for Unknown Exception in API
    
    """
    status_code = 500

    def __init__(self, message, status_code=None, body=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.body = body

    def to_dict(self):
        out = dict(self.body or ())
        out['message'] = self.message
        out['status_code']=self.status_code
        return out

class AuthenticationError(Exception):
    """
    Raise Exception for Authentication Errors
    
    """
    status_code = 401

    def __init__(self, message, status_code=None, body=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.body = body

    def to_dict(self):
        out = dict(self.body or ())
        out['message'] = self.message
        out['status_code']=self.status_code
        return out
