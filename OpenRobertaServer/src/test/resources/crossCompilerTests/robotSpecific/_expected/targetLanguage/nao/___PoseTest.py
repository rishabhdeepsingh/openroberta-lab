#!/usr/bin/python

import math
import time
import random
from roberta import Hal
h = Hal()



def run():
    h.setAutonomousLife('ON')
    h.say("Begin pose test")
    h.setAutonomousLife('OFF')
    h.say("Stand zero")
    h.applyPosture("StandZero")
    h.say("Stand initial")
    h.applyPosture("StandInit")
    h.say("Stand")
    h.applyPosture("Stand")
    h.say("Sit")
    h.applyPosture("Sit")
    h.say("Stand")
    h.applyPosture("Stand")
    h.say("Crouch")
    h.applyPosture("Crouch")
    h.say("Lying on belly")
    h.applyPosture("LyingBelly")
    h.say("Lying on back")
    h.applyPosture("LyingBack")
    h.say("Resetting pose")
    h.applyPosture("Stand")
    h.say("Pose test complete")

def main():
    try:
        run()
    except Exception as e:
        h.say("Error!" + str(e))
    finally:
        h.myBroker.shutdown()

if __name__ == "__main__":
    main()