from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.exceptions import ValidationError
from . import models


class BKUserCreationForm(UserCreationForm):

    class Meta:
        model = models.BKUser

        fields = (
            'password1',
            'password2',
            'username',
            'name',
            'last_name',
            'email',
            'password'
        )
        widgets = {
            'password': forms.PasswordInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }


class BKUserChangeForm(UserChangeForm):

    class Meta:
        model = models.BKUser
        fields = '__all__'


class UserAdmin(BaseUserAdmin):
    form = BKUserChangeForm
    add_form = BKUserCreationForm

    list_display = ('email', 'last_name', 'name', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', )}),
        ('Personal info', {'fields': ('name', 'last_name')}),
        ('Money', {'fields': ('balance',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'name', 'last_name'),
        }),
    )
    search_fields = ('username', 'last_name', 'name', 'email')
    ordering = ('last_name', 'name',)
    filter_horizontal = ()


@admin.register(models.Sport)
class SportAdmin(admin.ModelAdmin):
    pass


@admin.register(models.BetType)
class BetTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.SureBet)
class SureBetAdmin(admin.ModelAdmin):
    pass



admin.site.unregister(Group)
admin.site.register(models.BKUser, UserAdmin)

