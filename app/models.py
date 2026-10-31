#app/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

class User(AbstractUser):
	email = models.EmailField(unique=True, null=False, blank=False)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

	def __str__(self):
		return self.email

class Vulnerability(models.Model):
	# uuid4 = version 4, using cryptographic randomness to generate the uuid
	vuln_id = models.UUIDField(
		unique=True,
		blank=False,
		null=False,
		editable=False,
		default=uuid.uuid4
	)
	vuln_name = models.CharField(max_length=30, blank=False)
	vuln_description = models.TextField()
	vuln_known_cases = models.TextField()
	vuln_score = models.FloatField(
		blank=False, 
		default=1.0, 
		validators=[
			MinValueValidator(0.0),
			MaxValueValidator(10.0)
		]
	)
	vuln_known_fixes = models.TextField()
	vuln_solved_status = models.BooleanField(default=False, null=False, blank=False)
	# add datetime automatically the first time the vuln is saved
	vuln_date_created = models.DateTimeField(auto_now_add=True)
	# overwrite this datetime automatically every time the vuln is updated
	vuln_date_modified = models.DateTimeField(auto_now=True)
	vuln_is_active = models.BooleanField(default=True)