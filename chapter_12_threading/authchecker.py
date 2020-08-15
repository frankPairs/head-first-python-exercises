from flask import session

from functools import wraps


def check_logged_in(fn: object) -> object:
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return fn(*args, **kwargs)

        return 'You are not logged'

    return wrapper
