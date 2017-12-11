from django.db import models
from django.contrib.auth.models import User


class BeastModel(models.Model):
    """ Basic metadata for Bestiary objects """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True


# Create your models here.
class DataSourceType(BeastModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Repository(BeastModel):
    name = models.CharField(max_length=200)
    # Relations
    data_source_type = models.ForeignKey(DataSourceType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'data_source_type')

    def __str__(self):
        return "%s (%s)" % (self.name, self.data_source_type)


class DataSource(BeastModel):
    params = models.CharField(max_length=400)
    # Relations
    # Base Repository from which to create the View
    rep = models.ForeignKey(Repository, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('rep', 'params')

    def __str__(self):
        return self.rep.name + " " + self.params


class Project(BeastModel):
    name = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=200)
    # Relations
    data_sources = models.ManyToManyField(DataSource)
    # https://docs.djangoproject.com/en/1.11/ref/models/fields/#foreignkey
    subprojects = models.ManyToManyField("Project")
    eco = models.ForeignKey("Ecosystem", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'eco')

    def __str__(self):
        return self.name


class Ecosystem(BeastModel):
    name = models.CharField(max_length=200, unique=True)
    # Relations
    projects = models.ManyToManyField(Project)
    subecos = models.ManyToManyField("Ecosystem")

    def __str__(self):
        return self.name
