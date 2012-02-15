import layout


from facebook import authorization


class isAuthorized(object):
    def __init__(self, f):
        self.f = f
        
    def __call__(self, *args):
        if not authorization.isAuthorized():
            return layout.getIndex()
        else:
            authorization.checkAuthorization()
            
            self.f(*args)