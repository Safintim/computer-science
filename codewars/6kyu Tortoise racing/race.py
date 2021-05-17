def race(v1, v2, g):
    if 0 < v1 < v2:
        time = g * 3600 // (v2 - v1)
        hours = time // 3600
        minutes = time % 3600 // 60
        seconds = time % 60
        return [hours, minutes, seconds]
