from .util import refresh_token

def refresh_token_middleware(get_response):

    def middleware(request):
        # NOTE: Depends on session middleware.

        if request.user.is_authenticated:
            token = request.session['JWT']
            request.session['JWT'] = refresh_token(token)

        response = get_response(request)

        return response

    return middleware
