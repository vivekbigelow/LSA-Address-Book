from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
  firstName = models.CharField(max_length=120)
  lastName = models.CharField(max_length=120)
  phoneNumber = models.CharField(max_length=10)
  email = models.EmailField()
  address = models.TextField()
  user = models.ForeignKey(User, default=None,on_delete=models.CASCADE)

  def get_absolute_url(self):
    return reverse("contact-details",kwargs={"id": self.id})

  def get_delete_url(self):
    return reverse("delete",kwargs={"id": self.id})
  
  def get_edit_url(self):
    return reverse("edit",kwargs={"id": self.id})