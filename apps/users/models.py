from __future__ import unicode_literals

from django.db import models
import re
NAME_REGEX = re.compile(r"^[-a-zA-Z']+$")
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

class BlogManager(models.Manager):
	def validator(self, postData):
		errors = {}
		if len(postData["first_name"]) < 1:
			errors["first_name"] = "Must enter a first name."
		elif not NAME_REGEX.match(postData["first_name"]):
			errors["first_name"] = "First name contains invalid characters."
		if len(postData["last_name"]) < 1:
			errors["last_name"] = "Must enter a last name."
		elif not NAME_REGEX.match(postData["last_name"]):
			errors["last_name"] = "Last name contains invalid characters."
		if len(postData["email"]) < 1:
			errors["email"] = "Must enter an email address."
		elif not EMAIL_REGEX.match(postData["email"]):
			errors["email"] = "Email address not valid."
		if User.objects.filter(email=postData["email"]):
			errors["email"] = "Email address is already in use."
		return errors

class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = BlogManager()