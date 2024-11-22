from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='core/images/')

    def __str__(self):
        return self.username


class Chat(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(Member)

    def __str__(self):
        return self.name


class Message(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    text = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20] + '...'