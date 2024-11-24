from django.contrib.auth import get_user_model

class EmailAuthBackend:
    model_user = get_user_model()

    def authenticate(self, request, username=None, password=None):
        try:
            user = self.model_user.objects.get(email=username)
            if user.check_password(password):
                return user
            
            return None
        except (self.model_user.DoesNotExist, self.model_user.MultipleObjectsReturned):
            return None
    
    def get_user(self, user_id):
        try:
            return self.model_user.objects.get(pk=user_id)
        except self.model_user.DoesNotExist:
            return None