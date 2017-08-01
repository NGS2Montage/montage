def get_token(request)
    profile = request.user.profile
    return profile.token or profile.generate_token()
