from geopy.geocoders import Nominatim
from pygris.geocode import geolookup, geocode
import Stop, Route

class User:
    def __init__(self):
        self.lat = None
        self.long = None
        self.stop = None #lat/long/stop id etc
        self.route = None #route: str, direction: str (as tuple?)
        self.preferred_stops = []
        self.preferred_routes = []
        # self.home_address = None
        # self.school_address = None

    def find_lat_long(self, address):
        geolocator = Nominatim(user_agent = "cta-hackathon-2024")

        location = geolocator.geocode(address)

        if location:
            self.lat = location.latitude
            self.long = location.longitude

    def find_closest_stop(self):
        route = Route(self.route)
        stops = route.get_route_stops()
        distances = []
        for given_stop in given_stops:
            given_stop = Stop(self.stop)
            distance = given_stop.get_distance(self.lat, self.long)
            distances.append(distance)
        min_distance = min(distances)
        stop_ind = distances.index(min_distance) #if multiple stops within a thresh, implement later
        closest_stop = stops[stop_ind]
        return closest_stop

    def set_inputs(self,lat=None, long=None, route=None,stop=None, autodetect=None,
                   address=None):
        if route:
            self.route = route
        if stop:
            self.stop = stop
        if autodetect and address:
            self.find_lat_long(address)
            if not self.lat or not self.long:
                raise Exception("No valid address") #no valid address
            else:
                stop = self.find_closest_stop()

    def set_preferences(self, stop, route):
        if route:
            self.preferred_routes.append(route)
        if stop:
            self.preferred_stops(stop)
