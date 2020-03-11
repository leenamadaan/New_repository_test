from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# first commit
#<<<<<<< HEAD
# second commit
<<<<<<< HEAD
<<<<<<< HEAD
# third commit
# fourth commit

=======
>>>>>>> parent of c28554c... Third commit
=======
>>>>>>> parent of c28554c... Third commit


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #sixth commit
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)#Nineth comment
    # seventh comment

    def __str__(self):
        return self.title

    def get_absolute_url(self): # sixth commit
        return reverse('post-detail', kwargs={'pk': self.pk}) # seventh comment