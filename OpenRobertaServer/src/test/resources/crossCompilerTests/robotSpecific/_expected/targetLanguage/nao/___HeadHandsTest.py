#!/usr/bin/python

import math
import time
import random
from roberta import Hal
h = Hal()

class BreakOutOfALoop(Exception): pass
class ContinueLoop(Exception): pass



___headPitch = 28
___headYaw = 115

def run():
    h.setAutonomousLife('ON')
    global ___headPitch, ___headYaw
    h.say("Begin hands test")
    h.say("Right hand opened")
    h.hand("RHand", 1)
    h.wait(2000)
    h.say("Right hand closed")
    h.hand("RHand", 2)
    h.wait(2000)
    h.say("Left hand opened")
    h.hand("LHand", 1)
    h.wait(2000)
    h.say("Left hand closed")
    h.hand("LHand", 2)
    h.wait(2000)
    h.say("Hands test complete")
    h.moveJoint("HeadYaw", 10, 1)
    h.say("Begin head test")
    h.setAutonomousLife('OFF')
    h.say("Resetting head position")
    h.moveJoint("HeadYaw", 0, 1)
    h.moveJoint("HeadPitch", 0, 1)
    for ___k0 in range(int(0), int(6), int(1)):
        h.say(str("".join(str(arg) for arg in ["Moving head to pitch", ___headPitch])))
        h.moveJoint("HeadPitch", ___headPitch, 1)
        ___headPitch = ___headPitch - 10
    h.moveJoint("HeadPitch", 0, 1)
    for ___k1 in range(int(0), int(12), int(1)):
        h.say(str("".join(str(arg) for arg in ["Moving head to yaw", ___headYaw])))
        h.moveJoint("HeadYaw", ___headYaw, 1)
        ___headYaw = ___headYaw - 20
    h.say("Resetting head position")
    h.moveJoint("HeadYaw", 0, 1)
    h.moveJoint("HeadPitch", 0, 1)
    h.say("Head test complete")

def main():
    try:
        run()
    except Exception as e:
        h.say("Error!" + str(e))
    finally:
        h.myBroker.shutdown()

if __name__ == "__main__":
    main()