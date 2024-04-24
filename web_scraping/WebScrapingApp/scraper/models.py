from django.db import models

class ScrapedData(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title