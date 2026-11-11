from microbit import *

import moisture as m
import pump as p

while True:
    if m.read_moisture() > 100:
        p.pump()
    sleep(50)
