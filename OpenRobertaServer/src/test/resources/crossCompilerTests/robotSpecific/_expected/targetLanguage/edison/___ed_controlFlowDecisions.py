import Ed
Ed.EdisonVersion = Ed.V2
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_SLOW
obstacleDetectionOn = False
Ed.LineTrackerLed(Ed.ON)
Ed.ReadClapSensor()
Ed.ReadLineState()
Ed.TimeWait(250, Ed.TIME_MILLISECONDS)

___X = 0

if True:
    ___X += 1
if False:
    ___X += 1000
if True:
    if True:
        ___X += 1
    ___X += 1
if True:
    if False:
        ___X += 1000
    ___X += 1
if False:
    if False:
        ___X += 1000
    ___X += 1000
if False:
    if True:
        ___X += 1000
    ___X += 1000
if True:
    if True:
        if False:
            ___X += 1000
        ___X += 1
    ___X += 1
if True:
    ___X += 1
elif False:
    ___X += 1000
if False:
    ___X += 1000
elif True:
    ___X += 1
if True:
    ___X += 1
else:
    ___X += 1000
if False:
    ___X += 1000
else:
    ___X += 1
if True:
    ___X += 1
elif True:
    ___X += 1000
else:
    ___X += 1000
if False:
    ___X += 1000
elif False:
    ___X += 1000
else:
    ___X += 1
if True:
    ___X += 1
elif False:
    ___X += 1000
else:
    ___X += 1000
if False:
    ___X += 1000
elif True:
    ___X += 1
else:
    ___X += 1000

