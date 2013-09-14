#encoding: utf-8
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.contrib.gis.geos import Polygon

from django.test import TestCase
from spatio_main.api import SerializerWithASCII
from spatio_main.models import District, Community, State


class SerializerTest(TestCase):
    def test_to_json(self):
        test_data = {'test': 453, 'tütü': 45, 'rm': 'ü43'}
        serializer = SerializerWithASCII()
        result = serializer.to_json(test_data)
        self.assertEquals('{"rm": "\\u00fc43", "test": 453, "t\\u00fct\\u00fc": 45}',result)


class ModelTests(TestCase):
    def test_district_unicode(self):
        test_name = "Kreuzberg-Friedrichshain"
        district = District()
        district.name = test_name
        self.assertEqual(test_name, unicode(district))

    def test_community_unicode(self):
        test_name = "Kreuzberg"
        community = Community()
        community.name = test_name
        self.assertEqual(test_name, unicode(community))

    def test_state_unicode(self):
        test_name = "Berlin"
        state = State()
        state.name = test_name
        self.assertEqual(test_name, unicode(state))

    def test_state_bbox(self):
        test_box = [(0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0), (0.0, 0.0)]
        state = State()
        state.area = Polygon(test_box)
        self.assertEqual(Polygon(test_box), state.bbox)


