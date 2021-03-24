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
    },
    'sensors': {
        '3':Hal.makeHTColorSensorV2(ev3dev.INPUT_3),
    },
}
hal = Hal(_brickConfiguration)

___item = 'white'
___item2 = 0
___item3 = []
def run():
    global ___item, ___item2, ___item3
    ___item = hal.getHiTecColorSensorV2Colour('3')
    ___item2 = hal.getHiTecColorSensorV2Light('3')
    ___item2 = hal.getHiTecColorSensorV2Ambient('3')
    ___item3 = hal.getHiTecColorSensorV2Rgb('3')

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