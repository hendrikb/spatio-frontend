from django.contrib.gis.db import models


class State(models.Model):
    class Meta:
        db_table = 'states'
        managed = False
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at  = models.DateTimeField()
    area = models.GeometryField(null=True, srid=3785)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name


class Community(models.Model):
    class Meta:
        db_table = 'communities'
        managed = False
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State)
    created_at = models.DateTimeField()
    updated_at  = models.DateTimeField()
    area = models.GeometryField(srid=3785)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name


class District(models.Model):
    class Meta:
        db_table = 'districts'
        managed = False
    name = models.CharField(max_length=255)
    community = models.ForeignKey(Community)
    created_at = models.DateTimeField()
    updated_at  = models.DateTimeField()
    area = models.GeometryField(srid=3785)

    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

