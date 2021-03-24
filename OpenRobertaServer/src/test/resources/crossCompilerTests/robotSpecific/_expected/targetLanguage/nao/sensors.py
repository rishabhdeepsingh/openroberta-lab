#!/usr/bin/python

import math
import time
import random
from roberta import Hal
h = Hal()
h.sonar.subscribe("OpenRobertaApp")
h.mark.subscribe("RobertaLab", 500, 0.0)

from roberta import FaceRecognitionModule
faceRecognitionModule = FaceRecognitionModule("faceRecognitionModule")

from roberta import SpeechRecognitionModule
speechRecognitionModule = SpeechRecognitionModule("speechRecognitionModule")
speechRecognitionModule.pauseASR()


___numberVar = 0
___booleanVar = True
___stringVar = ""
___colourVar = 0xff0000
___numberList = [0, 0]
___booleanList = [True, True]
___stringList = ["", ""]
___colourList = [0xff0000, 0xff0000]
def sensors():
    global ___numberVar, ___booleanVar, ___stringVar, ___colourVar, ___numberList, ___booleanList, ___stringList, ___colourList
    h.say(str(h.touchsensors('head', 'front')))
    h.say(str(h.touchsensors('head', 'middle')))
    h.say(str(h.touchsensors('head', 'rear')))
    h.say(str(h.touchsensors('hand', 'left')))
    h.say(str(h.touchsensors('hand', 'right')))
    h.say(str(h.touchsensors('bumper', 'left')))
    h.say(str(h.touchsensors('bumper', 'right')))
    h.say(str(h.ultrasonic()))
    h.say(str(h.getDetectedMark()))
    h.say(str(h.getDetectedMarks()))
    h.say(str(h.getNaoMarkInformation(___numberVar)))
    h.say(str(faceRecognitionModule.detectFace()))
    h.say(str(faceRecognitionModule.detectFace()))
    h.say(str(faceRecognitionModule.getFaceInformation(___stringVar)))
    h.say(str(speechRecognitionModule.recognizeWordFromDictionary(___stringVar)))
    h.say(str(h.gyrometer('x')))
    h.say(str(h.gyrometer('y')))
    h.say(str(h.accelerometer('x')))
    h.say(str(h.accelerometer('y')))
    h.say(str(h.accelerometer('z')))
    h.say(str(h.fsr('left')))
    h.say(str(h.fsr('right')))
    h.say(str(h.getElectricCurrent('HeadYaw')))
    h.say(str(h.getElectricCurrent('HeadPitch')))
    h.say(str(h.getElectricCurrent('LShoulderPitch')))
    h.say(str(h.getElectricCurrent('LShoulderRoll')))
    h.say(str(h.getElectricCurrent('RShoulderPitch')))
    h.say(str(h.getElectricCurrent('RShoulderRoll')))
    h.say(str(h.getElectricCurrent('LElbowYaw')))
    h.say(str(h.getElectricCurrent('LElbowRoll')))
    h.say(str(h.getElectricCurrent('RElbowYaw')))
    h.say(str(h.getElectricCurrent('RElbowRoll')))
    h.say(str(h.getElectricCurrent('LWristYaw')))
    h.say(str(h.getElectricCurrent('RWristYaw')))
    h.say(str(h.getElectricCurrent('LHand')))
    h.say(str(h.getElectricCurrent('RHand')))
    h.say(str(h.getElectricCurrent('LHipYawPitch')))
    h.say(str(h.getElectricCurrent('LHipRoll')))
    h.say(str(h.getElectricCurrent('LHipPitch')))
    h.say(str(h.getElectricCurrent('RHipYawPitch')))
    h.say(str(h.getElectricCurrent('RHipRoll')))
    h.say(str(h.getElectricCurrent('RHipPitch')))
    h.say(str(h.getElectricCurrent('LKneePitch')))
    h.say(str(h.getElectricCurrent('RKneePitch')))
    h.say(str(h.getElectricCurrent('LAnklePitch')))
    h.say(str(h.getElectricCurrent('LAnkleRoll')))
    h.say(str(h.getElectricCurrent('RAnklePitch')))
    h.say(str(h.getElectricCurrent('RAnkleRoll')))


def run():
    h.setAutonomousLife('ON')
    global ___numberVar, ___booleanVar, ___stringVar, ___colourVar, ___numberList, ___booleanList, ___stringList, ___colourList
    sensors()

def main():
    try:
        run()
    except Exception as e:
        h.say("Error!" + str(e))
    finally:
        h.sonar.unsubscribe("OpenRobertaApp")
        h.mark.unsubscribe("RobertaLab")
        faceRecognitionModule.unsubscribe()
        speechRecognitionModule.unsubscribe()
        h.myBroker.shutdown()

if __name__ == "__main__":
    main()