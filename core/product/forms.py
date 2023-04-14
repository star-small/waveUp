from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean_username(self):
        data = self.cleaned_data["username"]
        if User.objects.filter(username=data).exists():
            ValidationError("wefew")
        return data
