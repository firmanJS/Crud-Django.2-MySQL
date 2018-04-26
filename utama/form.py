from django.forms import ModelForm
from utama.models import Tbl_user

class UserForm(ModelForm):

    class Meta:
        model = Tbl_user
        fields = ['username', 'email', 'password']
