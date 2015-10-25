from django.db import models

class MyModel(models.Model):
    categories = models.ManyToManyField(
        'category.Category',
        help_text='Categorize this item.'
    )
    tags = models.ManyToManyField(
        'category.Tag',
        help_text='Tag this item.'
    )