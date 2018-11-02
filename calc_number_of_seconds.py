def calc_number_of_seconds(time_period, unit):
    if unit == "second":
        return time_period
    elif unit == "minute":
        return time_period*60
    elif unit == "hour":
        return time_period*360
    elif unit == "day":
        return time_period*86400
    elif unit == "week":
        return time_period*604800
    elif unit == "month":
        return time_period*30*86400
    elif unit =="year":
        return time_period*365*86400