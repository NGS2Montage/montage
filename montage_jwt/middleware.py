from .util import is_token_about_to_expire, refresh_token

def refresh_token_middleware(get_response):

    def middleware(request):
        # NOTE: Depends on session middleware.

        if request.user.is_authenticated:
            token = request.session['JWT']
            if is_token_about_to_expire(token): # or is_token_expired(token):
                request.session['JWT'] = refresh_token(token)

        response = get_response(request)

        return response

    return middleware
