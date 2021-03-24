import Ed
Ed.EdisonVersion = Ed.V2
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_SLOW
obstacleDetectionOn = False
Ed.LineTrackerLed(Ed.ON)
Ed.ReadClapSensor()
Ed.ReadLineState()
Ed.TimeWait(250, Ed.TIME_MILLISECONDS)

___Element = Ed.ReadKeypad() == Ed.KEYPAD_TRIANGLE
___Element2 = _obstacleDetection(Ed.OBSTACLE_LEFT)
___Element3 = _irSeek(1)
___Element4 = Ed.ReadLeftLightLevel() / 10
___Element5 = Ed.ReadLineState() == Ed.LINE_ON_BLACK
___Element6 = Ed.ReadClapSensor() == Ed.CLAP_DETECTED

Ed.ReadObstacleDetection()
Ed.ReadKeypad()
Ed.ReadClapSensor()
Ed.ReadRemote()
Ed.ReadIRData()


def _irSeek(mode):
    global obstacleDetectionOn
    if (obstacleDetectionOn == True):
        Ed.ObstacleDetectionBeam(Ed.OFF)
        obstacleDetectionOn = False
    if (mode == 0): return Ed.ReadIRData()
    elif (mode == 1): return Ed.ReadRemote()

def _obstacleDetection(mode):
    global obstacleDetectionOn
    if (obstacleDetectionOn == False):
        Ed.ObstacleDetectionBeam(Ed.ON)
        obstacleDetectionOn = True
    return Ed.ReadObstacleDetection() == mode
