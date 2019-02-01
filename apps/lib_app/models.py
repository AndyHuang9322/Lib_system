from __future__ import unicode_literals
from django.db import models, IntegrityError
import re

class Validator(models.Manager):
    def registration_validator(self, postData):
        errors = []
        if len(postData['fname']) < 2:
            errors.append("First name should be at least 2 characters")
        if len(postData['lname']) < 2:
            errors.append("Last name should be at least 2 characters")
        if not re.match(r'[^@]+@[^@]+\.[^@]+', postData['email']):
            errors.append("Email format invalid")
        if len(postData['pw']) < 8:
            errors.append("Password should be at least 8 characters")
        if postData['cpw']!=postData['pw']:
            errors.append("Confirm password should be the same as password")
        response = {
            'errors': errors,
            'valid': True,
            'user': None
        }
        if len(errors)>0:
            response['valid'] = False
        else:
            try: 
                response['user'] = User.objects.create(first_name=postData['fname'], last_name=postData['lname'], email=postData['email'], password=postData['pw'])
            except IntegrityError:
                response['errors'].append('This email already exists.')
                response['valid'] = False
        return response
    
    def book_validator(self, postData,id):
        errors = []
        if len(postData['author']) < 3:
            errors.append("Author name should be at least 3 characters")
        if len(postData['title']) < 2:
            errors.append("Author name should be at least 2 characters")
        if len(postData['description']) < 10:
            errors.append("Descriptions should be at least 10 characters")
         
        response = {
            'errors': errors,
            'valid': True,
            'user': None
        }
        if len(errors)>0:
            response['valid'] = False
        else:
                response['user'] = Book.objects.create(author=postData['author'], title=postData['title'], description=postData['description'] )
        return response

class User(models.Model):
    permissions = models.CharField(max_length=10, default='student')
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
    user_like = models.ManyToManyField(User, related_name="likes")
    rented_by = models.ForeignKey(User, related_name="user", null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validator()
    def __repr__(self):
        return f"{self.user_author, self.titile ,self.description, self.rented_by.first_name, self.created_at}" 

class Review(models.Model):
    review = models.CharField(max_length=255)
    book = models.ForeignKey(Book, related_name="reviews")
    posted_by = models.ForeignKey(User, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Validator()
    def __repr__(self):
        return f"{self.book.title, self.review, self.posted_by.first_name, self.created_at}" 