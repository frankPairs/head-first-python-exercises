import datetime
import time
import random

odds = [
    1, 3, 5, 7, 9,
    11, 13, 15, 17, 19,
    21, 23, 25, 27, 29,
    31, 33, 35, 37, 39,
    41, 43, 45, 47, 49,
    51, 53, 55, 57, 59
]

for n in range(5):
    right_this_minute = datetime.datetime.today().minute

    if right_this_minute in odds:
        print('this minute seems a little odd')
    else:
        print('not an odd minute')

    wait_time = random.randint(1, 60)

    print(wait_time)

    time.sleep(wait_time)