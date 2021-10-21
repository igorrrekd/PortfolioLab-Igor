from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)


class Institution(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    TYPE_CHOICES = (
        ("fundacja", "fundacja"),
        ("organizacja pozarządowa", "organizacja pozarządowa"),
        ("zbiórka lokalna", "zbiórka lokalna"),
    )
    type = models.CharField(max_length=25, choices=TYPE_CHOICES, default="fundacja")
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField(default=0, null=False)
    # categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=9)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=5)
    pick_up_date = models.DateTimeField(auto_now_add=True)
    pick_up_time = models.DateTimeField(auto_now=True)
    pick_up_comment = models.TextField(max_length=1024)
    user = models.ForeignKey()
