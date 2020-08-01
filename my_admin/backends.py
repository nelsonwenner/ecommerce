from django.contrib.auth.backends import ModelBackend

class AdminBackend(ModelBackend):
    """
    Overrider form authentication
    """
    def user_can_authenticate(self, user):
        can_authenticate = super().user_can_authenticate(user)
        return can_authenticate