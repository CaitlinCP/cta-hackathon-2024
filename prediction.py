import bus
#im not sure if this is the right approach.
def predict_time(stop_id,bus_route_id):
    prediction = bus.get_route_stops(stop_id,bus_route_id)
    return prediction['prdctdn']