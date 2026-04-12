from django.contrib.auth.hashers import make_password

def build_health_response():
    return {
        "status": "success",
        "message": "Security module is running successfully"
    }

def build_signup_payload(username, password):
    return {
        "username": username.strip(),
        "password_hash": make_password(password)
    }