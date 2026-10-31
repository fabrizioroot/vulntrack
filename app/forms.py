#app/forms.py

from django import forms
from .models import Vulnerability
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import User
# prevents circular import crashes for larger apps
# from django.contrib.auth import get_user_model


class CreateUserForm(UserCreationForm):
    class Meta:
        # can be replaced with model = get_user_model()
        model = User
        fields = [
            'email',
            'first_name',
            'last_name'
        ]

class UpdateUserForm(UserChangeForm):
    class Meta:
        # can be replaced with model = get_user_model()
        model = User
        fields = [
            'email',
            'first_name',
            'last_name'
        ]


class VulnForm(forms.ModelForm):
    class Meta:
        model = Vulnerability
        fields = [
            'vuln_name', 
            'vuln_description', 
            'vuln_known_cases', 
            'vuln_score', 
            'vuln_known_fixes', 
            'vuln_solved_status'
        ]

