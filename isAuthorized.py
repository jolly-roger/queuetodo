from facebook import authorization

from layout import layout


def isAuthorized(f):
    def _isAuthorized(*args, **kwargs):
        if not authorization.isAuthorized():
            return layout.getSignin()
        else:
            authorization.checkAuthorization()
            
            return f(*args, **kwargs)
            
    return _isAuthorized