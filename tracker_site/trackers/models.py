from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse



# Create your models here.
@python_2_unicode_compatible
class Tracker(models.Model):
    tracker_name = models.CharField(max_length=30)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    # objects = models.Manager()

    def __str__(self):
        return self.tracker_name

    def get_abs_url(self):
        return reverse('tracker-detail', kwargs={'pk': self.pk})
