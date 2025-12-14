from models.user import User

def login(username, password):
    user = User.authenticate(username, password)
    if user:
        return {"status": "success", "user": user}
    else:
        return {"status": "failure", "message": "Invalid credentials"}
    