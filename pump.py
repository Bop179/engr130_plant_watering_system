# Imports go at the top
import robotbit_library as r
from microbit import *

M1A = 0x1
M1B = 0x2

r.setup()


def pump():
    r.motor(M1A, 90)
    sleep(3000)
    r.all_stop()
