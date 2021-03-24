#include "bob3.h" 
Bob3 rob;


unsigned long __time_1 = millis();

void setup()
{
    
}

void loop()
{
    rob.setLed(EYE_2, RGB(0x00, 0x00, 0xff));
    rob.setLed(EYE_1, RGB(0xFF, 0x00, 0x00));
    __time_1 = millis();
    while (true) {
        if ( ( rob.getArm(1) > 0 ) == true ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( ( rob.getArm(1) == 3 ) == true ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( ( rob.getArm(1) == 2 ) == true ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( ( rob.getArm(1) == 1 ) == true ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( ( rob.getArm(2) > 0 ) == true ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( ( rob.getArm(2) == 3 ) == true ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( ( rob.getArm(2) == 2 ) == true ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( ( rob.getArm(2) == 1 ) == true ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( rob.getIRLight() < 30 ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( rob.getIRSensor() < 30 ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( rob.getTemperature() < 20 ) {
            break;
        }
        delay(1);
    }
    while (true) {
        if ( (int) (millis() - __time_1) > 500 ) {
            break;
        }
        delay(1);
    }
}