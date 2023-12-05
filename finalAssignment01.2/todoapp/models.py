from django.db import models

# Create your models here.
class Task(models.Model):
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

#added code
class SearchBar(models.Model):
    search_nav = models.CharField(max_length=255)

    def __str__(self):
        return self.search_nav


class SearchQuery(models.Model):
    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query

