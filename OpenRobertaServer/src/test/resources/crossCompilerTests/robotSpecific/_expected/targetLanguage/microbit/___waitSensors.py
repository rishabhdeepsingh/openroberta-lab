import microbit
import random
import math

class BreakOutOfALoop(Exception): pass
class ContinueLoop(Exception): pass

timer1 = microbit.running_time()

def run():
    global timer1
    while True:
        if microbit.button_a.is_pressed() == True:
            break
    while True:
        if microbit.pin1.is_touched() == True:
            break
    while True:
        if "up" == microbit.accelerometer.current_gesture() == True:
            break
    while True:
        if "down" == microbit.accelerometer.current_gesture() == True:
            break
    while True:
        if "face down" == microbit.accelerometer.current_gesture() == True:
            break
    while True:
        if "face up" == microbit.accelerometer.current_gesture() == True:
            break
    while True:
        if "shake" == microbit.accelerometer.current_gesture() == True:
            break
    while True:
        if "freefall" == microbit.accelerometer.current_gesture() == True:
            break
    while True:
        if microbit.compass.heading() < 30:
            break
    while True:
        if ( microbit.running_time() - timer1 ) > 500:
            break
    while True:
        if microbit.compass.heading() < 30:
            break
    while True:
        if ( microbit.running_time() - timer1 ) > 500:
            break
    while True:
        if microbit.temperature() < 20:
            break
    while True:
        if microbit.pin0.read_analog() < 30:
            break
    while True:
        if microbit.pin0.read_digital() < 30:
            break
    while True:
        if microbit.pin0.read_pulsehigh() < 30:
            break
    while True:
        if microbit.pin0.read_pulselow() < 30:
            break
    while True:
        if microbit.accelerometer.get_x() > 512:
            break

def main():
    try:
        run()
    except Exception as e:
        raise

if __name__ == "__main__":
    main()