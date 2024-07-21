from website.models.event import Event
from flask import flash, redirect, url_for
from website.database import db
import googlemaps

def get_events():
    events = []
    for i in range(1,7):
        events.append(Event.query.filter_by(id=i).first())
    return events

def get_event_by_id(id):
    event = Event.query.filter_by(id=id).first()
    print(event)
    return event

def get_free_events():
    free_events = Event.query.filter_by(entry_fees='0').all()
    return free_events

def get_popular_events():
    pop_events = Event.query.filter_by(event_type='Popular').all()
    return pop_events

def get_recommended_events():
    rec_events = Event.query.filter_by(event_type='Recommended').all()
    return rec_events

def get_trending_events():
    trend_events = Event.query.filter_by(event_type='Trending').all()
    return trend_events

def get_searched_events(search):
    event = Event.query.filter(Event.event_name.like('%' + search + '%'))
    event = event.order_by(Event.event_name).all()
    return(event)


def get_nearby_events():
    client = googlemaps.Client('AIzaSyAtJ7llR6PgPC5skxCee2ao4umEAaXBfg8')
    result = client.geolocate()
    location = []
    location.append(result['location']['lat'])
    location.append(result['location']['lng'])
    print(location)
    near_me = []
    for event in Event.query.all():
        print(event.coordinates_lat)
        print(location[0])
        print(event.coordinates_long)
        print(location[1])
        distance = ((event.coordinates_lat - location[0])**2)+((event.coordinates_long - location[1])**2)
        print(distance)
        if abs(distance) <= 1:
            near_me.append(event)
    print(near_me)
    return near_me