#define _GNU_SOURCE

#include "MicroBit.h"
#include "NEPODefs.h"
#include <list>
#include <array>
#include <stdlib.h>
MicroBit _uBit;

void aktionKontrolle();

void tastenKontrolle();

void sensoren();


int _initTime = _uBit.systemTime();
double ___winkel;

int main()
{
    _uBit.init();
    ___winkel = 0;
    _uBit.display.setDisplayMode(DISPLAY_MODE_GREYSCALE);
    _uBit.accelerometer.updateSample();
    aktionKontrolle();
    tastenKontrolle();
    sensoren();
    release_fiber();
}

void aktionKontrolle() {
    _uBit.display.setBrightness((9) * _SET_BRIGHTNESS_MULTIPLIER);
    _uBit.display.scroll(ManagedString("OX"));
    _uBit.display.print(MicroBitImage("0,0,255,0,0\n0,0,255,0,0\n255,255,255,255,255\n0,0,255,0,0\n0,0,255,0,0\n"));
    _uBit.sleep(500);
    _uBit.display.print(MicroBitImage("255,0,0,0,255\n0,255,0,255,0\n0,0,255,0,0\n0,255,0,255,0\n255,0,0,0,255\n"));
    _uBit.sleep(500);
    _uBit.display.setBrightness((3) * _SET_BRIGHTNESS_MULTIPLIER);
    _uBit.display.print(MicroBitImage("255,0,255,0,255\n0,0,0,0,0\n0,0,0,0,0\n0,0,0,0,0\n0,0,0,0,0\n"));
    _uBit.sleep(500);
    for (int ___i = 0; ___i < 5; ___i += 1) {
        if ( round(_uBit.display.image.getPixelValue(___i, 0) * _GET_BRIGHTNESS_MULTIPLIER) >= 2 ) {
            _uBit.display.image.setPixelValue(___i, 2, (9) * _SET_BRIGHTNESS_MULTIPLIER);
        } else {
            _uBit.display.image.setPixelValue(___i, 3, (9) * _SET_BRIGHTNESS_MULTIPLIER);
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.sleep(500);
    _uBit.display.clear();
    _uBit.rgb.setColour(MicroBitColor(255, 0, 0, 255));
    _uBit.sleep(500);
    _uBit.rgb.setColour(MicroBitColor(0, 153, 0, 255));
    _uBit.sleep(500);
    _uBit.rgb.off();
    _uBit.soundmotor.soundOn(300); _uBit.sleep(500); _uBit.soundmotor.soundOff();
    _uBit.soundmotor.soundOn(261.626); _uBit.sleep(1000); _uBit.soundmotor.soundOff();
}

void tastenKontrolle() {
    _uBit.rgb.setColour(MicroBitColor(255, 0, 0, 255));
    while (true) {
        if ( _uBit.buttonA.isPressed() ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.setColour(MicroBitColor(0, 153, 0, 255));
    while (true) {
        if ( _uBit.buttonA.isPressed() == false ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.off();
    while ( true ) {
        while (true) {
            if ( _uBit.buttonA.isPressed() == true ) {
                break;
            }
            _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
        }
        _uBit.rgb.setColour(MicroBitColor(0, 153, 0, 255));
        while (true) {
            if ( _uBit.buttonA.isPressed() == false ) {
                break;
            }
            _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
        }
        _uBit.rgb.setColour(MicroBitColor(255, 0, 0, 255));
        _uBit.sleep(1000);
        if ( _uBit.buttonB.isPressed() ) {
            break;
        } else {
            continue;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.off();
    while (true) {
        if ( ! _uBit.buttonB.isPressed() ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.setColour(MicroBitColor(255, 0, 0, 255));
    while ( true ) {
        while (true) {
            if ( _uBit.buttonA.isPressed() == true ) {
                _uBit.rgb.setColour(MicroBitColor(0, 153, 0, 255));
                while (true) {
                    if ( _uBit.buttonA.isPressed() == false ) {
                        break;
                    }
                    _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
                }
                _uBit.rgb.setColour(MicroBitColor(255, 0, 0, 255));
                break;
            }
            if ( _uBit.buttonB.isPressed() == true ) {
                goto break_loop3;
                break;
            }
            _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
        }
        continue_loop3:
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    break_loop3:
    
    _uBit.rgb.off();
    while (true) {
        if ( ! _uBit.buttonB.isPressed() ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.setColour(MicroBitColor(255, 0, 0, 255));
}

void sensoren() {
    while (true) {
        if ( (_uBit.accelerometer.getGesture() == MICROBIT_ACCELEROMETER_EVT_TILT_UP) ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.setColour(MicroBitColor(0, 153, 0, 255));
    while (true) {
        if ( (_uBit.accelerometer.getGesture() == MICROBIT_ACCELEROMETER_EVT_TILT_DOWN) ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.setColour(MicroBitColor(255, 0, 0, 255));
    while (true) {
        if ( (_uBit.accelerometer.getGesture() == MICROBIT_ACCELEROMETER_EVT_FACE_DOWN) ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.setColour(MicroBitColor(0, 153, 0, 255));
    while (true) {
        if ( (_uBit.accelerometer.getGesture() == MICROBIT_ACCELEROMETER_EVT_FACE_UP) ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.setColour(MicroBitColor(255, 0, 0, 255));
    while (true) {
        if ( round(_uBit.display.readLightLevel() * _GET_LIGHTLEVEL_MULTIPLIER) <= 50 ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.setColour(MicroBitColor(0, 153, 0, 255));
    while (true) {
        if ( round(_uBit.display.readLightLevel() * _GET_LIGHTLEVEL_MULTIPLIER) >= 50 ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.setColour(MicroBitColor(255, 0, 0, 255));
    _initTime = _uBit.systemTime();
    while (true) {
        if ( ( _uBit.systemTime() - _initTime ) >= 1000 ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.rgb.setColour(MicroBitColor(0, 153, 0, 255));
    ___winkel = _uBit.compass.heading();
    _uBit.display.scroll(ManagedString(___winkel));
    while ( true ) {
        _uBit.sleep(1000);
        if ( abs(___winkel - _uBit.compass.heading()) >= 90 ) {
            _uBit.rgb.off();
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
}

