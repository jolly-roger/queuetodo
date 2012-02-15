import layout


from facebook import authorization


def isAuthorized(f):
    def _isAuthorized(*args, **kwargs):
        if not authorization.isAuthorized():
            return layout.getIndex()
        else:
            authorization.checkAuthorization()
            
            return f(*args, **kwargs)
            
    return _isAuthorized