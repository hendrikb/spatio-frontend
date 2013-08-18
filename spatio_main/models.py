from django.contrib.gis.db import models


class State(models.Model):
    class Meta:
        db_table = 'states'
        managed = False
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at  = models.DateTimeField()
    area = models.GeometryField(null=True, srid=3785)

    @property
    def bbox(self):
        return self.area.envelope


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


class PoliceReport(models.Model):
    class Meta:
        db_table = 'fub_oscs'
        managed = False
    location = models.GeometryField(null=True, srid=3785)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    uuid = models.CharField(max_length=40, primary_key=True)

    objects = models.GeoManager()

class HistoricData(models.Model):
    class Meta:
        db_table = 'fub_historic_oscs'
        managed = False
    title = models.CharField(max_length=500)
    crime_count = models.IntegerField()
    uuid = models.CharField(max_length=40, primary_key=True)


class WlanHotspot(models.Model):
    class Meta:
        db_table = 'wlan_demos'
        managed = False
    location = models.GeometryField(null=True, srid=3785)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    uuid = models.CharField(max_length=40, primary_key=True)