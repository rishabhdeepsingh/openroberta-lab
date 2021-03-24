#!/usr/bin/python

import math
import time
import random
from roberta import Hal
h = Hal()

class BreakOutOfALoop(Exception): pass
class ContinueLoop(Exception): pass



___speed = 0
___pitch = 0
___volume = 0

def run():
    h.setAutonomousLife('ON')
    global ___speed, ___pitch, ___volume
    h.say("Hi")
    h.say("Begin volume test")
    for ___k0 in range(int(0), int(10), int(1)):
        h.setVolume(___volume)
        ___volume = ___volume + 10
        h.say(str("".join(str(arg) for arg in ["Setting volume to", ___volume])))
    h.say("Volume test complete")
    h.say("Begin speed and pitch test")
    for ___k1 in range(int(0), int(4), int(1)):
        ___speed = ___speed + 25
        h.say(str("".join(str(arg) for arg in ["Setting speed to", ___speed])))
        for ___k2 in range(int(0), int(4), int(1)):
            ___pitch = ___pitch + 25
            h.say(str("".join(str(arg) for arg in ["Setting pitch to", ___pitch])))
            h.say("Text sample with variable speed and pitch",___speed,___pitch)
        ___pitch = 0
    h.say("Speech test complete")

def main():
    try:
        run()
    except Exception as e:
        h.say("Error!" + str(e))
    finally:
        h.myBroker.shutdown()

if __name__ == "__main__":
    main()