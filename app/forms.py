#app/forms.py

"""
   Copyright 2026 Fabrizio.root

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

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

