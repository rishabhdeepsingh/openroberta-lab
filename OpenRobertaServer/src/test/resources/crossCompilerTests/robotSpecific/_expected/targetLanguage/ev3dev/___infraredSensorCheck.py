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
        '1':Hal.makeIRSeekerSensor(ev3dev.INPUT_1),
        '4':Hal.makeInfraredSensor(ev3dev.INPUT_4),
    },
}
hal = Hal(_brickConfiguration)

___item = hal.getInfraredSensorDistance('4')
___item2 = hal.getInfraredSensorSeek('4')
___item3 = hal.getHiTecIRSeekerSensorValue('1', 'AC')
___item4 = hal.getHiTecIRSeekerSensorValue('1', 'DC')
def run():
    global ___item, ___item2, ___item3, ___item4
    hal.playTone(float(261.626), float(2000))
    hal.turnOnRegulatedMotor('B', 30)
    for ___k0 in range(int(0), int(10), int(1)):
        hal.drawText(str(hal.getInfraredSensorDistance('4')), 0, 1)
        hal.drawText(str(hal.getInfraredSensorSeek('4')), 0, 2)
        hal.drawText(str(hal.getHiTecIRSeekerSensorValue('1', 'AC')), 0, 3)
        hal.drawText(str(hal.getHiTecIRSeekerSensorValue('1', 'DC')), 0, 4)
        hal.clearDisplay()
        hal.waitFor(500)
        hal.drawText(str(___item), 0, 1)
        hal.drawText(str(___item2), 0, 2)
        hal.drawText(str(___item3), 0, 3)
        hal.drawText(str(___item4), 0, 4)

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