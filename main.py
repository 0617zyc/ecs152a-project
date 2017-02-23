from collections import deque
from math import log
from random import uniform

class Event:
    """Class for events."""
    def __init__(self, time, event_type, next_event = None, prev_event = None):
        self.time = time
        self.event_type = event_type
        self.next_event = next_event
        self.prev_event = prev_event

# Global variables (lel)
g_MAXBUFFER = 100
g_length = 0
g_time = 0
g_service_rate = 0
g_arrival_rate = 0
g_queue = deque(maxlen=g_MAXBUFFER)
GEL = []

def process_arrival_event(lamb, mu, event):
    # Update time, create new arrival event, and insert into GEL
    g_time = event.time
    new_arrival_event = Event(g_time + generate_time(lamb), 'a')
    packet_time = generate_time(mu)
    GEL.append(new_arrival_event)

    # Server is free
    if len(g_queue) == 0:
        new_departure_event = Event(g_time + packet_time, 'd')
        GEL.append(new_departure_event)
    else:
        if len(g_queue) == g_queue.maxlen:
            print("Packet dropped")
        new_packet = Event(g_time + generate_time(mu), 'd')

def generate_time(rate):
    u = uniform(0,1)
    return ((-1/rate)*log(1-u))

def initialize(lamb):
    # Generate first arrival event with some time
    event = Event(g_time + generate_time(lamb), 'a')
    GEL.append(event)

def main(lamb, mu):
    initialize(lamb)
    for i in range(0, 100000):

main(0.25, 1))
