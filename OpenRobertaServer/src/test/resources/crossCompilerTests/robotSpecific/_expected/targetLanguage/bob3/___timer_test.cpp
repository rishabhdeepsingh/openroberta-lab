#include "bob3.h" 
Bob3 rob;


double ___x;
unsigned long __time_1 = millis();

void setup()
{
    ___x = 0;
    
}

void loop()
{
    rob.setLed(EYE_2, RGB(0xFF, 0x00, 0x00));
    rob.setLed(EYE_1, RGB(0xFF, 0x00, 0x00));
    __time_1 = millis();
    while ( true ) {
        delay(500);
        if ( (int) (millis() - __time_1) >= 4000 ) {
            rob.setLed(EYE_2, RGB(0x55, 0xff, 0x99));
            rob.setLed(EYE_1, RGB(0x00, 0xff, 0x00));
            break;
        } else {
            continue;
        }
        delay(1);
    }
    delay(2000);
}