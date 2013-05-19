from tastypie.api import Api
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.contrib.gis.resources import ModelResource
from tastypie.fields import ForeignKey
from spatio_main.models import State, Community, District


class StatesResource(ModelResource):
    class Meta:
        resource_name = 'states'
        queryset = State.objects.all()
        filtering = {
            'name' : ('exact',)
        }


class CommunitiesResource(ModelResource):
    state = ForeignKey(StatesResource, 'state')

    class Meta:
        resource_name = 'communities'
        queryset = Community.objects.all()
        filtering = {
            'name' : ('exact',),
            'state' : ALL_WITH_RELATIONS
        }


class DistrictsResource(ModelResource):
    community = ForeignKey(CommunitiesResource, 'community')

    class Meta:
        resource_name = 'districts'
        queryset = District.objects.all()
        filtering = {
            'name' : ('exact',),
            'community' : ALL_WITH_RELATIONS
        }


api = Api(api_name='v1')
api.register(DistrictsResource())
api.register(CommunitiesResource())
api.register(StatesResource())