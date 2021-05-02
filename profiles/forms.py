from django.contrib.auth import get_user_model

from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):  
        class Meta: 
            model = User
            fields = ('email', 'first_name', 'last_name', 'username')
