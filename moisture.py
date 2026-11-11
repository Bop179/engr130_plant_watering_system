# Imports go at the top
import robotbit_library as r
from microbit import *

r.setup()


def read_moisture():
    return pin0.read_analog()  # 0–1023
