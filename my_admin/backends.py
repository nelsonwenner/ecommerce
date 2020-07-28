from django.contrib.auth.backends import ModelBackend

class AdminBackend(ModelBackend):
    """
    Overrider form authentication from admin
    """
    def user_can_authenticate(self, user):
        can_authenticate = super().user_can_authenticate(user)
        return True if can_authenticate and user.is_staff else False