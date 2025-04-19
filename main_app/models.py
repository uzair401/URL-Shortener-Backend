from django.db import models
import uuid

# Create your models here.
class ShortURL(models.Model):
    short_url = models.CharField(max_length=10, unique=True)
    original_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hit_count = models.IntegerField(default=0)

    #in case the user didn't provide shortcode 
    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.short_url} -> {self.original_url} ({self.hit_count} hits)"
    
    
    