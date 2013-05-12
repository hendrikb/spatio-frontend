from django.contrib.gis.db import models


class State(models.Model):
    class Meta:
        db_table = 'states'
        managed = False
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at  = models.DateTimeField()
    area = models.GeometryField()

    objects = models.GeoManager()


class Community(models.Model):
    class Meta:
        db_table = 'communities'
        managed = False
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State)
    created_at = models.DateTimeField()
    updated_at  = models.DateTimeField()
    area = models.GeometryField()

    objects = models.GeoManager()


class District(models.Model):
    class Meta:
        db_table = 'districts'
        managed = False
    name = models.CharField(max_length=255)
    community = models.ForeignKey(Community)
    created_at = models.DateTimeField()
    updated_at  = models.DateTimeField()
    area = models.GeometryField()

    objects = models.GeoManager()
