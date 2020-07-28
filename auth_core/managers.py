from django.contrib.auth.models import UserManager

class UserClientManager(UserManager):
    
    def create_client(self, username, email=None, password=None, **extra_fields):
        user = super().create_user(username, email, password, **extra_fields)
        return user