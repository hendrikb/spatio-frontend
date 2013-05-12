from tastypie.api import Api
from tastypie.contrib.gis.resources import ModelResource
from tastypie.fields import ForeignKey
from spatio_main.models import State, Community, District


class StatesResource(ModelResource):
    class Meta:
        resource_name = 'states'
        queryset = State.objects.all()


class CommunitiesResource(ModelResource):
    state = ForeignKey(StatesResource, 'state')

    class Meta:
        resource_name = 'communities'
        queryset = Community.objects.all()


class DistrictsResource(ModelResource):
    community = ForeignKey(CommunitiesResource, 'community')

    class Meta:
        resource_name = 'districts'
        queryset = District.objects.all()


api = Api(api_name='v1')
api.register(DistrictsResource())
api.register(CommunitiesResource())
api.register(StatesResource())