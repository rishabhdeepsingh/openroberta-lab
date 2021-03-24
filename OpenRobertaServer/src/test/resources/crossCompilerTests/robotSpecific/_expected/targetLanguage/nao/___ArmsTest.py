#!/usr/bin/python

import math
import time
import random
from roberta import Hal
h = Hal()



def run():
    h.setAutonomousLife('ON')
    h.say("Begin hands test")
    h.setAutonomousLife('OFF')
    h.say("Setting hands to initial position")
    h.moveJoint("LElbowRoll", -2, 1)
    h.moveJoint("LShoulderRoll", 0, 1)
    h.moveJoint("LShoulderPitch", 0, 1)
    h.moveJoint("LWristYaw", 0, 1)
    h.moveJoint("LElbowYaw", 0, 1)
    h.moveJoint("RElbowRoll", 2, 1)
    h.moveJoint("RShoulderRoll", 0, 1)
    h.moveJoint("RShoulderPitch", 0, 1)
    h.moveJoint("RWristYaw", 0, 1)
    h.moveJoint("RElbowYaw", 0, 1)
    h.wait(5000)
    h.say("Shoulder roll test")
    h.moveJoint("LShoulderRoll", 40, 1)
    h.moveJoint("RShoulderRoll", -40, 1)
    h.wait(5000)
    h.say("Elbow roll test")
    h.moveJoint("LElbowRoll", -80, 1)
    h.moveJoint("RElbowRoll", 80, 1)
    h.wait(2000)
    h.moveJoint("LElbowRoll", 0, 1)
    h.moveJoint("RElbowRoll", 0, 1)
    h.wait(5000)
    h.say("Wrist yaw test")
    h.moveJoint("RWristYaw", 100, 1)
    h.moveJoint("LWristYaw", -100, 1)
    h.wait(2000)
    h.moveJoint("RWristYaw", -100, 1)
    h.moveJoint("LWristYaw", 100, 1)
    h.wait(5000)
    h.say("Shoulder pitch test")
    h.moveJoint("LShoulderPitch", -100, 1)
    h.moveJoint("RShoulderPitch", -100, 1)
    h.wait(5000)
    h.say("Resetting position")
    h.applyPosture("Stand")
    h.setAutonomousLife('ON')
    h.say("Hands test complete")

def main():
    try:
        run()
    except Exception as e:
        h.say("Error!" + str(e))
    finally:
        h.myBroker.shutdown()

if __name__ == "__main__":
    main()