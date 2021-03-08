from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from authapp.models import User

class UserLoginFrom(AuthenticationForm):
    class Meta:
        model =User
        fields = ('username', 'password')


    def __init__(self, *args, **kwargs):
        super(UserLoginFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'