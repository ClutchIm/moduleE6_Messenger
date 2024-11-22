from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='core/images/')


class Chat(models.Model):
    name = models.CharField(max_length=50)
    members = models.ForeignKey(Member, on_delete=models.CASCADE)


class Message(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    message = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)