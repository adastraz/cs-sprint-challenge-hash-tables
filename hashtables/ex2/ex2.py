#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    route = [None] * length

    for x in tickets:
        if x.source == "NONE":
            route[0] = x.destination
        cache[x.source] = x.destination

    for y in range(1, length):
        route[y] = cache[route[y - 1]] 

    return route
