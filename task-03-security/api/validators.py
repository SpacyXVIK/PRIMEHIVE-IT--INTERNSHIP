def validate_username(username):
    if username is None:
        return "username is required"
    username = username.strip()
    if len(username) < 3:
        return "username must be at least 3 characters long"
    if len(username) > 30:
        return "username must not exceed 30 characters"
    return None

def validate_password(password):
    if password is None:
        return "password is required"
    if len(password) < 8:
        return "password must be at least 8 characters long"
    return None