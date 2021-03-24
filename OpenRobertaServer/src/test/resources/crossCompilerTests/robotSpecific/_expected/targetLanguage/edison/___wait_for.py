import Ed
Ed.EdisonVersion = Ed.V2
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_SLOW
obstacleDetectionOn = False
Ed.LineTrackerLed(Ed.ON)
Ed.ReadClapSensor()
Ed.ReadLineState()
Ed.TimeWait(250, Ed.TIME_MILLISECONDS)


while True:
    if (Ed.ReadKeypad() == Ed.KEYPAD_TRIANGLE) == True:
        break
    pass
while True:
    if (_irSeek(1)) < 30:
        break
    pass
while True:
    if (Ed.ReadLeftLightLevel() / 10) < 50:
        break
    pass
while True:
    if (Ed.ReadRightLightLevel() / 10) < 50:
        break
    pass
while True:
    if (Ed.ReadLineTracker() / 10) < 50:
        break
    pass
while True:
    if (Ed.ReadClapSensor() == Ed.CLAP_DETECTED) == True:
        break
    pass
while True:
    if (_obstacleDetection(Ed.OBSTACLE_LEFT)) == True:
        break
    pass
while True:
    if (_obstacleDetection(Ed.OBSTACLE_RIGHT)) == True:
        break
    pass
while True:
    if (_obstacleDetection(Ed.OBSTACLE_AHEAD)) == True:
        break
    pass


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
