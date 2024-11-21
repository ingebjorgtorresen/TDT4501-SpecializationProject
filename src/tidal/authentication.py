import tidalapi

def authenticate_tidal():
    session = tidalapi.Session()
    session.login_oauth_simple()
    if session.check_login():
        print("TIDAL authentication successful.")
        return session
    else:
        print("TIDAL authentication failed.")
        return None
