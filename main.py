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
g_MAXBUFFER = 1
g_length = 0
g_time = 0
g_service_rate = 0
g_arrival_rate = 0
g_queue = deque()
GEL = []

# Global variables for collecting statistics
g_utilization = 0
g_mean_queue_length = 0
g_packets_dropped = 0

def process_arrival_event(lamb, mu, event):
    """Process arrival events."""
    global g_time, g_length, g_packets_dropped, g_utilization

    # Update time, create new arrival event, and insert into GEL
    # Save the previous time for utilization calculation
    prev_time = g_time
    g_time = event.time
    next_arrival_event = Event(g_time + generate_time(lamb), 'a')
    packet_service_time = generate_time(mu)
    GEL.append(next_arrival_event)

    # FIXME
    #print("Next arrival event added")
    print_GEL()

    # Server is free
    if g_length == 0:
        g_length += 1
        new_departure_event = Event(g_time + packet_service_time, 'd')
        GEL.append(new_departure_event)

        # FIXME
        #print("Next departure event added")
        print_GEL()

    else:
        # Utilization calculation
        g_utilization += event.time - prev_time

        # Buffer is currently full
        if (g_length - 1) >= g_MAXBUFFER:
            print("Packet dropped")
            g_packets_dropped += 1
        else:
            print("Adding to queue")
            g_queue.append(packet_service_time)
            g_length += 1

def process_departure_event(event):
    """Process departure events."""
    global g_time, g_length, g_utilization

    # Update total utilization time
    g_utilization += event.time - g_time

    # Update time and length of buffer
    g_time = event.time
    g_length -= 1

    if g_length > 0:
        packet = g_queue.popleft()
        departure_packet = Event(g_time + packet, 'd')
        GEL.append(departure_packet)

        # FIXME
        print_GEL()

def generate_time(rate):
    """Generate a inter-arrival/transmit time based on the rate."""
    u = uniform(0,1)
    return ((-1/rate)*log(1-u))

def initialize(lamb):
    """Initialize the process."""
    # Generate first arrival event with some time
    event = Event(g_time + generate_time(lamb), 'a')
    GEL.append(event)

def print_GEL():
    """Print GEL for debugging purposes."""
    GEL.sort(key=lambda x: x.time)
    print("Printing GEL:")
    for event in GEL:
        print("Event: " + event.event_type + " " + str(event.time))

def process_statistics():
    global g_time, g_utilization, g_packets_dropped

    print("Total time: " + str(g_time))
    print("Total utilization time: " + str(g_utilization))
    print("Total utilization percentage: " + str(g_utilization / g_time))
    print("Total packets dropped: " + str(g_packets_dropped))

def main(lamb, mu):
    initialize(lamb)
    for i in range(0, 1000):
        print("Current time: " + str(g_time))
        print("Buffer length: " + str(g_length))
        event = GEL.pop(0)
        print("Processing event: " + event.event_type + " " + str(event.time))
        if event.event_type == 'a':
            process_arrival_event(lamb, mu, event)
        else:
            process_departure_event(event)
    process_statistics()

main(0.75, 1)
