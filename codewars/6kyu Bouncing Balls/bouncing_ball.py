def bouncing_ball(h, bounce, window):
    if (h > 0) and (h > window) and (0 < bounce < 1):
        count = 0
        
        while h > window:
            count += 1
            h = h * bounce
            if h > window:
                count += 1
        return count
        
    return -1
