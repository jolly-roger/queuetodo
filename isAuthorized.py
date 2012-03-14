from facebook import authorization

from layout import layout


def isAuthorized(f):
    def _isAuthorized(*args, **kwargs):
        isSignedRequest = False
        
        for kw in kwargs:
            if kw == "signed_request":
                isSignedRequest = True
                break
        
        if isSignedRequest:
            return f(*args, **kwargs)
        else:
            if not authorization.isAuthorized():
                return layout.getSignin()
            else:
                authorization.checkAuthorization()
                
                return f(*args, **kwargs)
            
    return _isAuthorized