from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
<<<<<<< HEAD
=======
# first commit

>>>>>>> parent of 91fc787... Second commit

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #sixth commit
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # seventh comment

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})