import math

EARTH_R_MI = 3963


def haversine_distance(location1,location2):
    """
    Calculate the distance between two points on a sphere (like Earth) in miles.

    https://en.wikipedia.org/wiki/Haversine_formula

    :param lat1: latitude of first point
    :param lon1: longitude of first point
    :param lat2: latitude of second point
    :param lon2: longitude of second point

    :return: distance in miles
    """
    #print(location1,location2,'printing out locay')
    lat1, lon1= location1
    lat2, lon2 =location2
    def deg_to_rad(deg):
        return deg * math.pi / 180
    
    #Using MAP to apply deg_to_rad to each argument
    lat1, lon1, lat2, lon2 = map(deg_to_rad, [lat1, lon1, lat2, lon2])

    #Haversine_formula
    distance = 2 * EARTH_R_MI * math.asin(
        math.sqrt(
            (math.sin((lat2 - lat1) / 2)**2) +
            (math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2)**2)))

    return distance



class Stop:
    def __init__(self,id,name,stop_location):
        self.stop_id = id
        self.stop_name = name 
        self.stop_location = stop_location
        
    def get_distance(self,dist_location):
        distance = haversine_distance(self.stop_location,dist_location)
        return distance
