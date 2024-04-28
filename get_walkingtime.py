import googlemaps
from datetime import datetime


SECRET_KEY = 'AIzaSyBez5y5bvMrNfsuVqgrOHjXGgh7Xr2nxzA'

class Walking:
    def __init__(self,user_location,stop_location):
        """
        example:
        destination = "28.6100,77.2300"
        source = "28.7914217793474,77.2585030666252"
        """
        self.source = user_location
        self.destination = stop_location
        self.start_time = datetime.now()
        self.client = googlemaps.Client( key = SECRET_KEY)

    def time_distance(self):
        try:
            direction_result = self.client.directions\
                (self.source,self.destination,mode = "walking",\
                                            avoid = "ferries", \
                                                departure_time = self.start_time)
        except Exception as e:
            print(f"error {e}")
        self.distance,self.time = direction_result[0]\
            ['legs'][0]['distance']['text'],direction_result[0]\
                ['legs'][0]['duration']['text']


