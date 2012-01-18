import constants


def get(req):
    if len(req.cookie) > 0 and req.cookie[constants.FACEBOOK_CODE]:
        return '&nbsp;<a href="/addtodo">add todo</a>' \
            '&nbsp;<a href="/listtodo">list todo</a>' \
            '&nbsp;<a href="/logout">logout</a>'
    else:
        return '&nbsp;<a href="/signin">signin</a>' 