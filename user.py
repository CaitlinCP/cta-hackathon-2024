from geopy.geocoders import Nominatim
from pygris.geocode import geolookup, geocode
from stop import Stop
from routes import Route

class User:
    def __init__(self):
        self.lat = None
        self.long = None
        self.stop = None #lat/long/stop id etc
        self.route = None #route: str, direction: str (as tuple?)
        self.preferred_stops = []
        self.preferred_routes = []
        self.address = None
        self.autodetect = None
        # self.home_address = None
        # self.school_address = None

    def find_lat_long(self):
        geolocator = Nominatim(user_agent = "cta-hackathon-2024")

        location = geolocator.geocode(self.address)

        if location:
            self.lat = location.latitude
            self.long = location.longitude

    def find_closest_stop(self):
        route = Route(self.route)
        route.get_stops()
        #print("Route initiated")
        #print("Route_id",route.route_id)
        given_stops = route.stops
        #print(given_stops,'printing stop data')
        distances = []
        for given_stop in given_stops:
            given_stop_obj = Stop(given_stop['stpid'],given_stop['stpnm'],(given_stop['lat'],given_stop['lon']) )
            distance = given_stop_obj.get_distance((self.lat, self.long))
            distances.append(distance)
        min_distance = min(distances)
        stop_ind = distances.index(min_distance) #if multiple stops within a thresh, implement later
        closest_stop = given_stops[stop_ind]
        return closest_stop

    def set_inputs(self,lat=None, long=None, route=None,stop=None, autodetect=None,
                   address=None):
        if route:
            self.route = route
        if stop:
            self.stop = stop
        if autodetect and address:
            self.address = address
            self.autodetect = autodetect
            self.find_lat_long()
            if not self.lat or not self.long:
                raise Exception("No valid address") #no valid address
            else:
                stop = self.find_closest_stop()

    def set_preferences(self, stop, route):
        if route:
            self.preferred_routes.append(route)
        if stop:
            self.preferred_stops(stop)

    