from datetime import datetime, timedelta

def add(moment):
    gigasecond = 10 ** 9
    return moment + timedelta(seconds=gigasecond)
