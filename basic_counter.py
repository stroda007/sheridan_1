"""
Adds a new number every second until the user kills it.

To run: 'python basic_counter.py'
"""
import time

COUNTER = 0

try:
    while COUNTER < 101:    #Just in case they don't know how to exit
        time.sleep(1)
        print(f'{COUNTER}')
        COUNTER += 1
    print('Thanks for counting with me!')

except KeyboardInterrupt:
    print('Ok, Ok. See ya!')
    exit()
