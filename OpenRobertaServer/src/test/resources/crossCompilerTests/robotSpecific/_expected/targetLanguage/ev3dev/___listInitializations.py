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

___numbers = [0, hal.getUltraSonicSensorDistance('4'), hal.getMotorTachoValue('B', 'degree'), hal.getMotorTachoValue('B', 'rotation'), hal.getMotorTachoValue('B', 'distance'), hal.getGyroSensorValue('2', 'angle'), hal.getGyroSensorValue('2', 'rate'), hal.getTimerValue(1)]
___strings = [True, False, hal.isPressed('1'), hal.isKeyPressed('enter'), hal.getUltraSonicSensorPresence('4'), True == hal.isKeyPressed('enter'), True != hal.isKeyPressed('enter'), hal.getUltraSonicSensorDistance('4') < 0, hal.getUltraSonicSensorDistance('4') <= 0, hal.getUltraSonicSensorDistance('4') > 0, hal.getUltraSonicSensorDistance('4') >= 0, True and hal.isKeyPressed('enter'), True or hal.isKeyPressed('enter')]
___booleans = ["", "".join(str(arg) for arg in ["", hal.getColorSensorColour('3'), [""], True, 0, 'white'])]
___colors = ['white', hal.getColorSensorColour('3')]
___connections = [hal.waitForConnection(), hal.establishConnectionTo("")]
___item = [5] * 5
___item2 = [True] * 5
___item3 = [""] * 5
___item4 = ['blue'] * 5
___item5 = [hal.waitForConnection()] * 5
___item6 = [5 + float(1.2)] * 5
___item7 = [True] * 5
___item8 = ["".join(str(arg) for arg in ["", hal.getColorSensorColour('3')])] * 5
___item9 = [hal.getColorSensorColour('3')] * 5
def run():
    global ___numbers, ___strings, ___booleans, ___colors, ___connections, ___item, ___item2, ___item3, ___item4, ___item5, ___item6, ___item7, ___item8, ___item9

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