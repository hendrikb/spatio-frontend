from tastypie.api import Api
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.contrib.gis.resources import ModelResource, GeometryApiField
from tastypie.fields import ForeignKey
from spatio_main.models import State, Community, District, PoliceReport


class StatesResource(ModelResource):
    bbox = GeometryApiField('bbox', readonly=True)

    class Meta:
        resource_name = 'states'
        queryset = State.objects.all()
        filtering = {
            'name' : ('exact',),
            'area' : ALL

        }


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

class PoliceReportResource(ModelResource):
    class Meta:
        resource_name = 'reports'
        queryset = PoliceReport.objects.all()
        filtering = {
            'point' : ALL
        }


api = Api(api_name='v1')
api.register(DistrictsResource())
api.register(CommunitiesResource())
api.register(StatesResource())
api.register(PoliceReportResource())