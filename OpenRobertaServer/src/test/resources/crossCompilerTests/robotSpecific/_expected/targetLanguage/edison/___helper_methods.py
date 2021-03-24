import Ed
Ed.EdisonVersion = Ed.V2
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_SLOW
obstacleDetectionOn = False
Ed.LineTrackerLed(Ed.ON)
Ed.ReadClapSensor()
Ed.ReadLineState()
Ed.TimeWait(250, Ed.TIME_MILLISECONDS)

___obstacle = _obstacleDetection(Ed.OBSTACLE_LEFT)
___rccode = _irSeek(1)
___tempnum = 0
___testlist = Ed.List(0, [])
___tempbool = True

# Action
_motorOn(0, 23, Ed.DISTANCE_UNLIMITED)
_motorOn(0, 30, 1)
# Math operations
___tempnum = _pow(10, 10)
___tempnum = _abs(40)
___tempnum = ((40+5)/10)*10
___tempnum = ((60/10)+1)*10
___tempnum = (80/10)
# Math logic
___tempbool = (7 % 2) == 0
___tempbool = (7 % 2) == 1
___tempbool = _isPrime(7)
___tempbool = 7 > 0
___tempbool = 7 < 0
___tempbool = (7 % 6) == 0
# Lists
___tempnum = sum(___testlist)
___tempnum = min(___testlist)
___tempnum = max(___testlist)
___tempnum = sum(___testlist) / len(___testlist)


def _abs(num):
    if (num < 0): return -num
    else: return num

def _getDirection(dir, reverse):
    if reverse:
       if (dir == Ed.FORWARD): return Ed.BACKWARD
       else: return Ed.FORWARD
    else: return dir

def _irSeek(mode):
    global obstacleDetectionOn
    if (obstacleDetectionOn == True):
        Ed.ObstacleDetectionBeam(Ed.OFF)
        obstacleDetectionOn = False
    if (mode == 0): return Ed.ReadIRData()
    elif (mode == 1): return Ed.ReadRemote()

def max(list):
    listMax = list[0]
    listLength = len(list)
    for i in range(listLength):
        if list[i] > listMax:
            listMax = list[i]
    return listMax

def min(list):
    listMin = list[0]
    listLength = len(list)
    for i in range(listLength):
        if list[i] < listMin:
            listMin = list[i]
    return listMin

def _motorOn(motor, power, distance):
    _dir = Ed.FORWARD
    _reverse = False
    if (power < 0):
        _power = _shorten(-power)
        _reverse = True
    else: _power = _shorten(power)
    if (motor == Ed.MOTOR_LEFT):
        if (_power == 0): Ed.DriveLeftMotor(Ed.STOP, 0, 0)
        else: Ed.DriveLeftMotor(_getDirection(_dir, _reverse), _power, distance)
    if (motor == Ed.MOTOR_RIGHT):
        if (_power == 0): Ed.DriveRightMotor(Ed.STOP, 0, 0)
        else: Ed.DriveRightMotor(_getDirection(_dir, _reverse), _power, distance)

def _obstacleDetection(mode):
    global obstacleDetectionOn
    if (obstacleDetectionOn == False):
        Ed.ObstacleDetectionBeam(Ed.ON)
        obstacleDetectionOn = True
    return Ed.ReadObstacleDetection() == mode

def _pow(base, exp):
    result = 1
    b = base
    for _ in range(exp):
        result *= b
    return result

def _isPrime(num):
    if num <= 1: return False
    newNum = num - 2
    for x in range(newNum):
        y = (x + 2)
        if (num % y) == 0: return False
    return True

def _shorten(num): return ((num+5)/10)

def sum(list):
    listSum = 0
    listLength = len(list)
    for i in range(listLength): listSum = (listSum + list[i])
    return listSum
