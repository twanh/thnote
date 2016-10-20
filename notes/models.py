from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone

# Model for the notes
class Note(models.Model):

    COLOR_CHOISES = (
    ('teal', 'Teal'),
    ('grey lighten-2', 'Grey'),
    ('red lighten-1', 'Red'),
    )

    title = models.CharField(max_length=500)
    note = models.TextField()
    done = models.BooleanField(default=False)
    # color = models.CharField(max_length=60, default='grey lighten-2')
    color = models.CharField(max_length=50, choices=COLOR_CHOISES, default='Grey')
    created_on = models.DateTimeField(default=timezone.now)
    is_favorite = models.BooleanField(default=False)
    def get_absolute_url(self):
        return reverse('notes:note-detail', kwargs={'pk': self.pk})

    def __str__(self): 
        return self.title