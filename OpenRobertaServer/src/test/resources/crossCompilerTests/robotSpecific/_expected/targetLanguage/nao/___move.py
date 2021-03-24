#!/usr/bin/python

import math
import time
import random
from roberta import Hal
h = Hal()



def run():
    h.setAutonomousLife('ON')
    h.applyPosture("Stand")
    h.applyPosture("LyingBack")

def main():
    try:
        run()
    except Exception as e:
        h.say("Error!" + str(e))
    finally:
        h.myBroker.shutdown()

if __name__ == "__main__":
    main()