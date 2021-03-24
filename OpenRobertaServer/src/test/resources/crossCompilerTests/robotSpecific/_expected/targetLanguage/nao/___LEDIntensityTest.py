#!/usr/bin/python

import math
import time
import random
from roberta import Hal
h = Hal()

class BreakOutOfALoop(Exception): pass
class ContinueLoop(Exception): pass



___intensity = 0

def run():
    h.setAutonomousLife('ON')
    global ___intensity
    h.say("Begin eyes L.E.D. test")
    h.say("Setting eyes to red")
    h.setLeds("FaceLeds", 0xff0000, 0.1)
    h.wait(2000)
    h.say("Setting eyes to blue")
    h.setLeds("FaceLeds", 0x3366ff, 0.1)
    h.wait(2000)
    h.say("Setting eyes to black")
    h.setLeds("FaceLeds", 0x000000, 0.1)
    h.wait(2000)
    h.say("Setting eyes to white")
    h.setLeds("FaceLeds", 0xffffff, 0.1)
    h.wait(2000)
    h.say("Eyes L.E.D. test complete")
    h.say("Begin ears, chest and head L.E.D. intensity test")
    for ___k0 in range(int(0), int(6), int(1)):
        h.say(str("".join(str(arg) for arg in ["Setting intensity to", ___intensity])))
        h.setIntensity("EarLeds", ___intensity)
        h.setIntensity("ChestLeds", ___intensity)
        h.setIntensity("BrainLeds", ___intensity)
        ___intensity = ___intensity + 20
    h.say("Ears, chest and head intensity test complete")

def main():
    try:
        run()
    except Exception as e:
        h.say("Error!" + str(e))
    finally:
        h.myBroker.shutdown()

if __name__ == "__main__":
    main()