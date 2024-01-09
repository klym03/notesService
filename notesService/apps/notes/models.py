from django.db import models

# Create your models here.
# notes/models.py
from django.db import models

# notes/models.py

class Note1(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'notes'



