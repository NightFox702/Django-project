from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title

class Card(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class History(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class EndSection(models.Model):
    whatsapp_link = models.URLField()
    instagram_link = models.URLField()
    tiktok_link = models.URLField()
    map_link = models.URLField()
    reservation_number = models.CharField(max_length=20)

    def __str__(self):
        return f'End Section'

class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
