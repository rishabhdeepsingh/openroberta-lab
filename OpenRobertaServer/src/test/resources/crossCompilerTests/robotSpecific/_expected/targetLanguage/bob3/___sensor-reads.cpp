#include "bob3.h" 
Bob3 rob;


bool ___b;
double ___c;

void setup()
{
    ___b = true;
    ___c = 0;
    
}

void loop()
{
    rob.setLed(EYE_2, RGB(0x00, 0x00, 0xff));
    rob.setLed(EYE_1, RGB(0xFF, 0x00, 0x00));
    delay(1000);
    ___b = ( rob.getArm(2) == 1 );
    ___b = ( rob.getArm(2) == 2 );
    ___b = ( rob.getArm(2) == 3 );
    ___b = ( rob.getArm(2) > 0 );
    ___b = ( rob.getArm(1) == 1 );
    ___b = ( rob.getArm(1) == 2 );
    ___b = ( rob.getArm(1) == 3 );
    ___b = ( rob.getArm(1) > 0 );
    ___c = rob.getIRLight();
    ___c = rob.getIRSensor();
    ___c = rob.getTemperature();
    ___c = rob.getID();
}