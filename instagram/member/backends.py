from django.contrib.auth import get_user_model

User = get_user_model()

class FacebookBackend():
    def authenticate(self, request, facebook_user_id):
        try:
            return User.objects.get(username=f'fb_{facebook_user_id}')
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
