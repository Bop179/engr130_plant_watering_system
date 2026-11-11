from microbit import *

import moisture as m
import pump as p

# Hold A = forward, hold B = reverse, release = stop
while True:
    if m.read_moisture() > 100:
        p.pump()
    sleep(50)
