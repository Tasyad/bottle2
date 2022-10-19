from datetime import datetime
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model
from django.urls import reverse


class Post(Model):
    title = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(default='default.jpg', upload_to='post_image/')

    # def __str__(self):
    #     return f'title: {self.title}\ author: {self.author}'

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})



