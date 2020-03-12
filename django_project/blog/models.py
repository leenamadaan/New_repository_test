from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
<<<<<<< HEAD
        return reverse('post-detail', kwargs={'pk': self.pk})

<<<<<<< HEAD
=======

# Third
#four
#five
=======
        return reverse('post-detail', kwargs={'pk': self.pk})
>>>>>>> parent of c1e3c12... Third Third Third
>>>>>>> parent of d6dbf8f... Today's first msg
