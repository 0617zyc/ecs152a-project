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
g_MAXBUFFER = 0
g_length = 0
g_time = 0
g_service_rate = 0
g_arrival_rate = 0
g_queue = deque()
GEL = []

def process_arrival_event(lamb, mu, event):
    """Process arrival events."""
    global g_time, g_length

    # Update time, create new arrival event, and insert into GEL
    g_time = event.time
    new_arrival_event = Event(g_time + generate_time(lamb), 'a')
    packet_service_time = generate_time(mu)
    GEL.append(new_arrival_event)
    # FIXME
    GEL.sort(key=lambda x: x.time)
    print("Printing GEL:")
    for item in GEL:
        print(item.time)

    # Server is free
    if g_length == 0:
        new_departure_event = Event(g_time + packet_service_time, 'd')
        GEL.append(new_departure_event)
        # FIXME
        GEL.sort(key=lambda x: x.time)
        print("Printing GEL:")
        for item in GEL:
            print(item.time)
    else:
        # Buffer is currently full
        if (g_length - 1) >= g_MAXBUFFER:
            print("Packet dropped")
        else:
            g_queue.append(generate_time(mu))
            g_length += 1

def process_departure_event(event):
    """Process departure events."""
    global g_time, g_length

    # Update time and length of buffer
    g_time = event.time
    g_length -= 1

    if g_length > 0:
        packet = g_queue.popleft()
        departure_packet = Event(g_time + packet, 'd')
        GEL.append(departure_packet)
        # FIXME
        print("Printing GEL:")
        GEL.sort(key=lambda x: x.time)
        for item in GEL:
            print(item.time)

def generate_time(rate):
    """Generate a inter-arrival/transmit time based on the rate."""
    u = uniform(0,1)
    return ((-1/rate)*log(1-u))

def initialize(lamb):
    """Initialize the process."""
    # Generate first arrival event with some time
    event = Event(g_time + generate_time(lamb), 'a')
    GEL.append(event)

def main(lamb, mu):
    initialize(lamb)
    for i in range(0, 10):
        event = GEL.pop(0)
        if event.event_type == 'a':
            process_arrival_event(lamb, mu, event)
        else:
            process_departure_event(event)

main(0.25, 1)
