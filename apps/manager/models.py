from __future__ import unicode_literals
from django.db import models

import re
import bcrypt

class UserManager(models.Manager):

	def create_user(self, name, alias, email, dob, pw_hash):
		user = self.create(name=name, alias=alias, email=email, dob=dob, pw_hash=pw_hash)
		return user

	def hash_password(self, password):
		password = password.encode()
		hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
		return hashed_pw

	def login_check(self, data):
		errors=[]
		email = data['email']
		password = data['password'].encode()
		try:
			user = self.get(email=email)
			hashed_pw = user.pw_hash.encode()
			if bcrypt.hashpw(password, hashed_pw) == hashed_pw:
				return (True, user)
		except:
			errors.append("Incorrect email or password")

		return (False, errors)

	def validate_registration(self, data):
		errors = []
		name = data['name']
		alias = data['alias']
		email = data['email']
		dob = data['dob']
		password = data['password']

		if len(name) < 2:
			errors.append("Please enter your name.")
		if len(alias) < 2:
			errors.append("Please enter an alias")
		if len(email) < 1:
			errors.append("Please enter an email address.")
		elif not re.match( r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
			errors.append("Please enter a valid email address")
		if len(password) < 8:
			errors.append("Password must have atleast 8 characters")

		if not errors:
			try:
				matches = self.get(email=email)
				errors.append("A user already exists with that email.")
				return (False, errors)
			except:
				pw_hash = self.hash_password(data['password'])
				user = self.create_user(data['name'], data['alias'], data['email'], data['dob'], pw_hash)
				return (True, user)
		else:
			return (False, errors)


class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	dob = models.DateTimeField(auto_now_add=False)
	friend = models.ManyToManyField("self", related_name="my_friend", null=True)
	pw_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
