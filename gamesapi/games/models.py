from django.db import models

# Create your models here.


class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    # note auto_now_true is false as release date is non editable column , while inserting or updating
    release_date = models.DateTimeField()
    game_category = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)

    class Meta:
        # check : https://docs.djangoproject.com/en/dev/topics/db/models/#meta-options
        # make gemes taable ordered by name
        ordering = ('name',)
