#include "bob3.h" 
Bob3 rob;



void setup()
{
    
}

void loop()
{
    rob.setLed(EYE_2, RGB(0xFF, 0x00, 0x00));
    delay(2000);
    rob.setLed(EYE_2, RGB(0x22, 0x88, 0x22));
    delay(2000);
}