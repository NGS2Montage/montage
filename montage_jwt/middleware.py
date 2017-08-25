from .models import JWT
from .util import make_login_token, refresh
from datetime import datetime
from django.utils import timezone
import jwt

def _refresh_token(request):
    token = request.session['JWT']

    claims = jwt.decode(
        token,
        verify=False,
    )

    exp = datetime.fromtimestamp(claims['exp'])
    exp = timezone.make_aware(exp)
    now = timezone.now()

    if now > exp:
        # Here we check if the token has completely expired, because if
        # the user is currently authenticated, it doesn't matter if the
        # token is expired or about to expire, the user will still need
        # a token.
        #
        # Better explanation in worse English:
        #
        # for the token refreshing in the session, i am not going to
        # check if the token is about to expire, i'm only going to
        # check if it has expired.  this allows me to delete the token
        # from the database when the refresh happens.  and it should be
        # okay because if a user is logged in, he should always have a
        # token in the session. ie, it's okay if for the time between
        # requests, that that user has an expired token since you are
        # also going to check for expiration on the front end

        # Delete the old token object
        JWT.objects.get_model_from_token(token).delete()
        
        # Make a new token
        new_jwt = refresh(claims)
        request.session['JWT'] = new_jwt.token

class TokenMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # NOTE: Depends on session middleware.

        if request.user.is_authenticated:
            if 'JWT' in request.session:
                _refresh_token(request)
            else:
                new_jwt = make_login_token(request.user)
                request.session['JWT'] = new_jwt.token

        response = self.get_response(request)
        return response
