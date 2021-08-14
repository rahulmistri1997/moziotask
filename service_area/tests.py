# Create your tests here.
from django.test import TestCase

from django.urls import reverse

from rest_framework import status

from service_area.models import Provider, ServiceArea
import json

class TestProviders(TestCase):
    def setUp(self):
        """ Creating a setup for ProviderTestCase """
        self.providerlink = reverse('provider-list')

    def test_get_providers(self):
        """ 
        Testing GET on provider 
        """
        response = self.client.get(self.providerlink)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_providers(self):
        """
        Testing POST on provider
        """
        self.assertEqual(Provider.objects.count(), 0)
        data = {
            "name": "rahulTest",
            "email": "rahulTest@Testmail.com",
            "phone_number": "986462351",
            "language": "EN",
            "currency": "INR"
        }
        response = self.client.post(self.providerlink, data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 1)

    def test_provider_delete(self):
        """
        Testing Delete on provider
        """
        self.assertEqual(Provider.objects.count(), 0)

        provider = Provider(name="Test", email="test@mail.com",
                           phone_number="1234")
        provider.save()

        self.assertEqual(Provider.objects.count(), 1)

        object_url = reverse('provider-detail', args=[provider.id])
        response = self.client.delete(object_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Provider.objects.count(), 0)


class TestServiceArea(TestCase):
    def setUp(self):
        """ Creating a setup for ServiceAreaTestCase """
        self.service_areas = reverse('service-area-list')
        provider = Provider(name="rahulTest", 
                            email="rahultest@Testmail.com",
                            phone_number="894651355")
        provider.save()
        self.provider = provider

    def test_get_service_areas(self):
        """
        Testing GET on service-areas
        """
        response = self.client.get(self.service_areas)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_service_area(self):
        """
        Testing POST on service-areas
        """
        self.assertEqual(ServiceArea.objects.count(), 0)
        data = {
            "name": "TestingAREA",
            "price": "12554",
            "area": {
                "type": "Polygon",
                "coordinates": [
                [
                    [
                        134.92830937524124,
                        -9.402493330384745
                    ],
                    [
                        112.89001884395184,
                        -18.98260689698227
                    ],
                    [
                        114.68906296895506,
                        -36.037456344865284
                    ],
                    [
                        130.880460093984,
                        -34.93885603739247
                    ],
                    [
                        146.62209618776217,
                        -39.58936566921309
                    ],
                    [
                        155.16755578152743,
                        -26.44335915998236
                    ],
                    [
                        134.92830937524124,
                        -9.402493330384745
                    ]
                ]
            ]
            },
            "provider": self.provider.id
        }
        response = self.client.post(self.service_areas, data=json.dumps(data),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)

    def test_service_area_search(self):
        """
        Testing Search on service-areas
        """
        # NOTE: this can be improved using factoryboy.
        service_area = ServiceArea(
            name="Test For Search",
            price="5648",
            provider=self.provider,
            area=json.dumps({
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        75.5419921875,
                        32.47269502206151
                    ],
                    [
                        65.7861328125,
                        25.24469595130604
                    ],
                    [
                        76.9921875,
                        7.144498849647335
                    ],
                    [
                        90.9228515625,
                        21.3303150734318
                    ],
                    [
                        95.44921875,
                        15.072123545811683
                    ],
                    [
                        95.2294921875,
                        27.332735136859146
                    ],
                    [
                        75.5419921875,
                        32.47269502206151
                    ]
                ]
            ]
        })
        )
        service_area.save()
        lat, lng = 74, 20
        query_url = self.service_areas + f'?lat={lat}&lng={lng}'
        response = self.client.get(query_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], service_area.id)

    def test_service_areas_delete(self):
        """
        Testing DELETE on service-areas
        """
        self.assertEqual(ServiceArea.objects.count(), 0)
        service_area = ServiceArea(
            name="Test",
            price="10",
            provider=self.provider,
            area=json.dumps({
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        75.5419921875,
                        32.47269502206151
                    ],
                    [
                        65.7861328125,
                        25.24469595130604
                    ],
                    [
                        76.9921875,
                        7.144498849647335
                    ],
                    [
                        90.9228515625,
                        21.3303150734318
                    ],
                    [
                        95.44921875,
                        15.072123545811683
                    ],
                    [
                        95.2294921875,
                        27.332735136859146
                    ],
                    [
                        75.5419921875,
                        32.47269502206151
                    ]
                ]
            ]
        })
        )
        service_area.save()

        self.assertEqual(ServiceArea.objects.count(), 1)

        object_url = reverse('service-area-detail', args=[service_area.id])
        response = self.client.delete(object_url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ServiceArea.objects.count(), 0)
