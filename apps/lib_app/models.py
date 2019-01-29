from __future__ import unicode_literals
from django.db import models, IntegrityError
import re

class Student(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.TextField(unique=True)
    password = models.CharField(max_length=45)
    objects = Validator()
    def __repr__(self):
        return f"{self.first_name, self.last_name, self.email, self.password}" 

class Admin(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.TextField(unique=True)
    password = models.CharField(max_length=45)
    objects = Validator()
    def __repr__(self):
        return f"{self.first_name, self.last_name, self.email, self.password}" 

class Book(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    description = models.TextField()
    posted_by = models.ForeignKey(User, related_name="messages")
    user_like = models.ManyToManyField(Student, related_name="likes")
    rent_at = models.DateTimeField(auto_now_add=True)
    return_at = models.DateTimeField(auto_now=True)
    objects = Validator()
    def __repr__(self):
        return f"{self.posted_by.first_name, self.user_author ,self.user_message, self.created_at}" 