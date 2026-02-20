import random as hikaru
import time as bobby



def tha_loop(queue):
    wait = hikaru.random()
    for num in range(3):
        msg = f'{num} The time is now {bobby.ctime()}'
        queue.put(msg) # I am putting this message in a queue so that it will still work in a jupyter notebook.
        bobby.sleep(wait)

