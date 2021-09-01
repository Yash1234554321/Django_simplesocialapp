from django.contrib.auth import get_user_model#returns current model
from django.contrib.auth.forms import UserCreationForm#built in

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = {'username','email','password1','password2'}#comes from auth users models from models.py
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'#setting labe for fields
        self.fields['email'].label = 'Email Address'
