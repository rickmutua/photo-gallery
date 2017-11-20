from django.db import models

# Create your models here.


class Editor (models.Model):

    name = models.CharField(max_length=65)
    username = models.CharField(max_length=65, blank=True)

    email = models.EmailField()

    def __str__(self):

        return self.name


class Tags(models.Model):

    name = models.CharField(max_length=100)


    def __str__(self):

        return self.name


class Post(models.Model):

    description = models.CharField(max_length=250)

    image = models.ImageField(upload_to= 'post/')

    editor = models.ForeignKey(Editor)

    tags = models.ManyToManyField(Tags)

    pub_date = models.DateTimeField(auto_now_add=True)