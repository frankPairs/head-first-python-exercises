from datetime import datetime
import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}

    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

fts = {convert2ampm(arrival_time): destination.title() for arrival_time, destination in flights.items()}

pprint.pprint(fts)
print()

when = {dest: [arrival_time for arrival_time, destination in fts.items() if dest == destination]
        for dest in set(fts.values())}

pprint.pprint(when)
print()
