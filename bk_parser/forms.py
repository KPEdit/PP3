from django import forms
from django.forms import models as Model
from . import models


class PasswordField(forms.CharField):
    def __init__(self, max_length=256, min_length=5, *args, **kwargs):
        super(PasswordField, self).__init__(
            max_length=max_length,
            min_length=min_length,
            widget=forms.PasswordInput,
            *args, **kwargs
        )

class BKUserLogForm(Model.ModelForm):
    class Meta:
        model = models.BKUser
        fields = ['username']

    password = PasswordField()


class BKUserRegisterForm(Model.ModelForm):

    password1 = PasswordField()
    password2 = PasswordField()

    class Meta:
        model = models.BKUser
        fields = model.REQUIRED_FIELDS + [model.USERNAME_FIELD]
        fields.remove('password')


