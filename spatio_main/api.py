from tastypie.api import Api
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.contrib.gis.resources import ModelResource, GeometryApiField
from tastypie.fields import ForeignKey
from spatio_main.models import State, Community, District, PoliceReport, HistoricData

import django
import simplejson
from django.core.serializers import json
from tastypie.cache import SimpleCache

from tastypie.serializers import Serializer


class SerializerWithASCII(Serializer):

    def to_json(self, data, options=None):
        """
        Given some Python data, produces JSON output.
        """
        options = options or {}
        data = self.to_simple(data, options)

        if django.get_version() >= '1.5':
            return json.json.dumps(data, cls=json.DjangoJSONEncoder,
                                   sort_keys=True, ensure_ascii=True)
        else:
            return simplejson.dumps(data, cls=json.DjangoJSONEncoder,
                                    sort_keys=True, ensure_ascii=True)


class StatesResource(ModelResource):
    bbox = GeometryApiField('bbox', readonly=True, null=True)

    class Meta:
        resource_name = 'states'
        queryset = State.objects.all()
        filtering = {
            'name' : ('exact',),
            'area' : ALL

        }
        serializer = SerializerWithASCII()
        cache = SimpleCache()


class CommunitiesResource(ModelResource):
    state = ForeignKey(StatesResource, 'state')

    class Meta:
        resource_name = 'communities'
        queryset = Community.objects.all()
        filtering = {
            'name' : ('exact',),
            'state' : ALL_WITH_RELATIONS,
            'area' : ALL
        }
        serializer = SerializerWithASCII()
        cache = SimpleCache()


class DistrictsResource(ModelResource):
    community = ForeignKey(CommunitiesResource, 'community')

    class Meta:
        resource_name = 'districts'
        queryset = District.objects.all()
        filtering = {
            'name' : ('exact',),
            'community' : ALL_WITH_RELATIONS,
            'area' : ALL
        }
        serializer = SerializerWithASCII()
        cache = SimpleCache()

class PoliceReportResource(ModelResource):
    class Meta:
        resource_name = 'reports'
        queryset = PoliceReport.objects.all()
        filtering = {
            'location' : ALL
        }
        serializer = SerializerWithASCII()
        cache = SimpleCache()

class HistoricDataResource(ModelResource):
    class Meta:
        resource_name = "history"
        queryset = HistoricData.objects.all()
        serializer = SerializerWithASCII()
        cache = SimpleCache()


api = Api(api_name='v1')
api.register(DistrictsResource())
api.register(CommunitiesResource())
api.register(StatesResource())
api.register(PoliceReportResource())
api.register(HistoricDataResource())