# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=9)
    quantity = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category)
    choices = (('yes','yes'),('no','no'))
    hot = models.CharField(max_length=20,blank=False,choices=choices)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    number = models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.user.username


class Cart(models.Model):
    cart_id = models.CharField(max_length=20)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)
    by  =  models.ForeignKey('auth.User')
    def __str__(self):
        return self.product.name

    def total(self):
        return self.quantity * self.product.price

    def price(self):
        return self.product.price

    def augment_quatity(self,quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

