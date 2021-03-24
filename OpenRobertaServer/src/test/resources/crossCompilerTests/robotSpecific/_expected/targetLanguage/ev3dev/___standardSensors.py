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
    hal.turnOnRegulatedMotor('B', 3)
    for ___k0 in range(int(0), int(10), int(1)):
        hal.drawText(str(hal.isPressed('1')), 0, 0)
        hal.drawText(str(hal.getUltraSonicSensorDistance('4')), 10, 0)
        hal.drawText(str(hal.getUltraSonicSensorPresence('4')), 0, 1)
        hal.drawText(str(hal.getColorSensorColour('3')), 10, 1)
        hal.drawText(str(hal.getColorSensorRed('3')), 0, 2)
        hal.drawText(str(hal.getColorSensorRgb('3')), 10, 2)
        hal.drawText(str(hal.getColorSensorAmbient('3')), 0, 3)
        hal.drawText(str(hal.getMotorTachoValue('B', 'rotation')), 0, 3)
        hal.drawText(str(hal.getMotorTachoValue('B', 'degree')), 10, 3)
        hal.drawText(str(hal.getMotorTachoValue('B', 'distance')), 0, 4)
        hal.resetMotorTacho('B')
        hal.drawText(str(hal.isKeyPressed('down')), 10, 4)
        hal.drawText(str(hal.getGyroSensorValue('2', 'angle')), 0, 5)
        hal.drawText(str(hal.getGyroSensorValue('2', 'rate')), 10, 5)
        hal.resetGyroSensor('2')
        hal.drawText(str(hal.getTimerValue(3)), 0, 6)
        hal.resetTimer(3)
        while True:
            if hal.isPressed('1') == True:
                break
            hal.waitFor(15)
        while True:
            if hal.isPressed('1') == False:
                break
            hal.waitFor(15)
        hal.clearDisplay()

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