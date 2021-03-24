#include "bob3.h" 
Bob3 rob;


double ___counter;

void setup()
{
    ___counter = 0;
    
}

void loop()
{
    remember((int)(rob.getIRLight()));
    ___counter += recall();
}