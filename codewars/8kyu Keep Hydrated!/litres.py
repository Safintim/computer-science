import math

LITRES_PER_HOUR = 0.5

def litres(time):
    # time // LITRES_PER_HOUR
    return math.floor(LITRES_PER_HOUR * time)