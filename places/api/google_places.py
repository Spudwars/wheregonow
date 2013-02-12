from tastypie.resources import Resource, fields, Bundle, BadRequest
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication

from googleplaces import GooglePlaces, lang #types

GOOGLE_PLACES_API_KEY = 'AIzaSyDpMwpHy4TUigePgDvvHUToH8Ddb5yI5Yg' #https://code.google.com/apis/console


class VenueObject(object):
    def __init__(self, id=None, name=None, address=None):
        self.id = id
        self.name = name
        self.address = address
        
        
class VenuesResource(Resource):
    id = fields.CharField(attribute='id')
    name = fields.CharField(attribute='name')
    address = fields.CharField(attribute='address', null=True)

    class Meta:
        resource_name = 'venues'
        allowed_methods = ['get', 'post']
        object_class = VenueObject
        authorization = Authorization()
        authentication = BasicAuthentication()
    
    def _client(self):
        return GooglePlaces(GOOGLE_PLACES_API_KEY)

    def detail_uri_kwargs(self, bundle_or_obj):
        kwargs = {}
        if isinstance(bundle_or_obj, Bundle):
            kwargs['pk'] = bundle_or_obj.obj.id
        else:
            kwargs['pk'] = bundle_or_obj['id']
        return kwargs
    
    def obj_get(self, request=None, **kwargs):
        result = self._client().get_place(kwargs['pk'])
        result.get_details()
        return VenueObject(result.reference, result.name, result.formatted_address)
    
    def obj_create(self, bundle, request=None, **kwargs):
        result = self._client().add_place(name=str(bundle.data['name']),
            lat_lng={'lat':bundle.data['latitude'],'lng':bundle.data['longitude']},
            accuracy=bundle.data['accuracy'],
            types=str(bundle.data['type']),
            language=lang.ENGLISH,
            sensor=True)
        bundle.obj = VenueObject(result['reference'], bundle.data['name'])
        bundle = self.full_hydrate(bundle)
        return bundle
    
    
    def get_object_list(self, request):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')
    
        if latitude and longitude:
            location = "%s,%s" % (latitude, longitude)
        else:
            raise BadRequest("Need latitude and longitude")
    
        query_name = request.GET.get('query', "")
    
        query = self._client().query(radius=800, sensor=True, location=location, name=query_name)
    
        results = []
        for result in query.places:
            result.get_details()
            new_obj = VenueObject(result.reference, result.name, result.formatted_address)
            results.append(new_obj)
    
        return results
    
    def obj_get_list(self, request=None, **kwargs):
        return self.get_object_list(request)



