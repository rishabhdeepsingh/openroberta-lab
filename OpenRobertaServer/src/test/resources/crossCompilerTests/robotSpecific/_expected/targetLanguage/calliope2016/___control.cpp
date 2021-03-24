#define _GNU_SOURCE

#include "MicroBit.h"
#include "NEPODefs.h"
#include <list>
#include <array>
#include <stdlib.h>
MicroBit _uBit;

int _initTime = _uBit.systemTime();
double ___r1;
double ___r2;
bool ___b1;
MicroBitColor ___c1;
double ___i;

int main()
{
    _uBit.init();
    ___r1 = 0;
    ___r2 = 0;
    ___b1 = true;
    ___c1 = MicroBitColor(204, 204, 204, 255);
    ___i = 0;
    
    if ( !( ___r1 == 0 ) ) {
        ___b1 = ___b1 && false;
    }
    if ( ___r1 == 1 ) {
        ___b1 = ___b1 && false;
    } else {
        ___r2 += 1;
    }
    if ( !( ___r1 == 1 ) ) {
        ___r2 += 1;
    } else {
        ___b1 = ___b1 && false;
    }
    if ( ___r1 == 1 ) {
        ___b1 = ___b1 && false;
    } else if ( ___r1 == 2 ) {
        ___b1 = ___b1 && false;
    } else {
        ___r2 += 1;
    }
    ___i = 0;
    while ( true ) {
        ___i += 1;
        if ( ___i == 2 ) {
            continue;
        }
        ___r2 += 1;
        if ( ___i >= 4 ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    ___i = 0;
    for (int ___k0 = 0; ___k0 < 4; ___k0 += 1) {
        ___i += 1;
        if ( ___i >= 2 ) {
            continue;
        }
        ___r2 += 1;
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    ___i = 0;
    while ( ___i < 4 ) {
        ___i += 1;
        if ( ___i > 2 ) {
            continue;
        }
        ___r2 += 1;
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    for (int ___j = 0; ___j < 6; ___j += 2) {
        ___r2 += 1;
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    while ( true ) {
        ___r2 += 1;
        while ( true ) {
            break;
            _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
        }
        ___r2 += 1;
        break;
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    _uBit.sleep(500);
    while (true) {
        if ( ( _uBit.systemTime() - _initTime ) > 500 ) {
            break;
        }
        _uBit.sleep(_ITERATION_SLEEP_TIMEOUT);
    }
    ___c1 = ( ( ___b1 && ( ___r2 == 14 ) ) ? ( MicroBitColor(0, 102, 0, 255) ) : ( MicroBitColor(255, 0, 0, 255)) );
    _uBit.rgb.setColour(___c1);
    release_fiber();
}
