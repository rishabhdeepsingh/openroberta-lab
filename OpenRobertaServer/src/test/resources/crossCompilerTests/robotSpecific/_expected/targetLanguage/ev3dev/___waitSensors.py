#!/usr/bin/python

from __future__ import absolute_import
from roberta.ev3 import Hal
from ev3dev import ev3 as ev3dev
import math
import os

class BreakOutOfALoop(Exception): pass
class ContinueLoop(Exception): pass

_brickConfiguration = {
    'wheel-diameter': 5.6,
    'track-width': 18.0,
    'actors': {
        'B':Hal.makeLargeMotor(ev3dev.OUTPUT_B, 'on', 'foreward'),
    },
    'sensors': {
        '1':Hal.makeTouchSensor(ev3dev.INPUT_1),
        '2':Hal.makeGyroSensor(ev3dev.INPUT_2),
        '3':Hal.makeColorSensor(ev3dev.INPUT_3),
        '4':Hal.makeUltrasonicSensor(ev3dev.INPUT_4),
    },
}
hal = Hal(_brickConfiguration)

def run():
    hal.playTone(float(261.626), float(500))
    for ___k0 in range(int(0), int(10), int(1)):
        while True:
            if hal.isPressed('1') == True:
                break
            if hal.getUltraSonicSensorDistance('4') < 30:
                break
            if hal.getUltraSonicSensorPresence('4') == True:
                break
            if hal.getColorSensorColour('3') == 'red':
                break
            if hal.getColorSensorRed('3') > 50:
                break
            if hal.getColorSensorAmbient('3') > 50:
                break
            if hal.getMotorTachoValue('B', 'rotation') > 2:
                hal.resetMotorTacho('B')
                break
            if hal.getMotorTachoValue('B', 'degree') > 180:
                hal.resetMotorTacho('B')
                break
            if hal.isKeyPressed('down') == True:
                break
            if hal.getGyroSensorValue('2', 'angle') > 90:
                hal.resetGyroSensor('2')
                break
            if hal.getGyroSensorValue('2', 'rate') > 90:
                hal.resetGyroSensor('2')
                break
            if hal.getTimerValue(1) > 50000:
                hal.resetTimer(1)
                break
            hal.waitFor(15)
        hal.playTone(float(130.813), float(2000))

def main():
    try:
        run()
    except Exception as e:
        hal.drawText('Fehler im EV3', 0, 0)
        hal.drawText(e.__class__.__name__, 0, 1)
        hal.drawText(str(e), 0, 2)
        hal.drawText('Press any key', 0, 4)
        while not hal.isKeyPressed('any'): hal.waitFor(500)
        raise

if __name__ == "__main__":
    main()