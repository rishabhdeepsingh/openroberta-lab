#!/usr/bin/python

import math
import time
import random
from roberta import Hal
h = Hal()

from roberta import FaceRecognitionModule
faceRecognitionModule = FaceRecognitionModule("faceRecognitionModule")


___item = 0
___item2 = ""
___item3 = True

def run():
    h.setAutonomousLife('OFF')
    global ___item, ___item2, ___item3
    h.applyPosture("Rest")
    h.stiffness("Body", 1)
    h.setAutonomousLife('ON')
    h.hand("RHand", 1)
    h.moveJoint("HeadYaw", 10, 1)
    h.walk(20, 0, 0)
    h.walk(0, 0,20)
    h.walk(0,0,0)
    h.walkAsync(0, 0, 0)
    h.stop()
    h.taiChi()
    h.pointLookAt('point', 0, 0, 0, 0, 0)
    h.setVolume(50)
    ___item = h.getVolume()
    h.setLanguage("German")
    ___item2 = h.getLanguage()
    h.say("Hallo")
    h.say("Hallo",30,30)
    h.playFile("Roberta")
    h.takePicture("Top", "RobertaPicture")
    h.recordVideo(0, "Top", 5, "RobertaVideo")
    ___item3 = faceRecognitionModule.learnFace("Roberta")
    ___item3 = faceRecognitionModule.forgetFace("Roberta")
    h.setLeds("FaceLeds", 0xff0000, 0.1)
    h.setIntensity("EarLeds", 50)
    h.ledOff("FaceLeds")
    h.ledReset("FaceLeds")
    h.randomEyes(2000)
    h.rasta(2000)

def main():
    try:
        run()
    except Exception as e:
        h.say("Error!" + str(e))
    finally:
        faceRecognitionModule.unsubscribe()
        h.myBroker.shutdown()

if __name__ == "__main__":
    main()