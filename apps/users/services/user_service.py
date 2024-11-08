from users.models import User

def get_list():
    return User.objects.all().order_by('username')

def get(id):
    return User.objects.filter(id=id).first()

def get_by_email(email):
    return User.objects.filter(email = email).first()