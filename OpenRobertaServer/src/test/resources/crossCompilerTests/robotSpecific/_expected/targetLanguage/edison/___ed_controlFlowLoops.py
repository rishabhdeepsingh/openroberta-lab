import Ed
Ed.EdisonVersion = Ed.V2
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_SLOW
obstacleDetectionOn = False
Ed.LineTrackerLed(Ed.ON)
Ed.ReadClapSensor()
Ed.ReadLineState()
Ed.TimeWait(250, Ed.TIME_MILLISECONDS)

___x = 0
___y = 1

# Control Flow Loop -- Start
for ___k0 in range(5):
    ___x = ___x + 1
while not (___x == 10):
    ___x = ___x + 1
while ___x < 15:
    ___x = ___x + 1
for ___i in range(6):
    ___x = ___x + 1
for ___j in range(5):
    ___x = ___x + 1
for ___k in range(6):
    ___x = ___x + 1
for ___o in range(7):
    ___x = ___x + 1
for ___p in range(9):
    ___x = ___x + 1
for ___m in range(5):
    ___y = ___y + 1
    ___x = ___x + 1
while True:
    if ___x < 30:
        ___x = ___x + 1
        if True:
            continue
        ___x = ___x + 1000
    elif ___x >= 30:
        break
# Control Flow Loop -- End

