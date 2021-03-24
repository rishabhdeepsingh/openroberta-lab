import microbit
import random
import math

class BreakOutOfALoop(Exception): pass
class ContinueLoop(Exception): pass

timer1 = microbit.running_time()

___item = microbit.compass.heading()
___item2 = ( microbit.running_time() - timer1 )
___item3 = microbit.temperature()
___item4 = microbit.pin0.read_analog()
___item5 = microbit.accelerometer.get_x()
___item6 = microbit.pin0.read_digital()
___item7 = microbit.pin0.read_pulsehigh()
___item8 = microbit.pin0.read_pulselow()
def run():
    global timer1, ___item, ___item2, ___item3, ___item4, ___item5, ___item6, ___item7, ___item8
    microbit.display.scroll(str(microbit.button_a.is_pressed()))
    microbit.display.scroll(str(microbit.pin1.is_touched()))
    microbit.display.scroll(str("up" == microbit.accelerometer.current_gesture()))
    microbit.display.scroll(str("down" == microbit.accelerometer.current_gesture()))
    microbit.display.scroll(str("face down" == microbit.accelerometer.current_gesture()))
    microbit.display.scroll(str("face up" == microbit.accelerometer.current_gesture()))
    microbit.display.scroll(str("shake" == microbit.accelerometer.current_gesture()))
    microbit.display.scroll(str("freefall" == microbit.accelerometer.current_gesture()))
    timer1 = microbit.running_time()

def main():
    try:
        run()
    except Exception as e:
        raise

if __name__ == "__main__":
    main()