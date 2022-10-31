from django.db import models

# Create your models here.
'''class Collection(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500)

    def __str__(self):
        return self.title
'''


class Image(models.Model):
    #collection = models.ForeignKey(Collection)

    image = models.ImageField(upload_to = 'images')
    title = models.CharField(max_length = 200)
    description = models.TextField(max_length = 500, null=False, blank=True)

    def __str__(self):
        return self.title

