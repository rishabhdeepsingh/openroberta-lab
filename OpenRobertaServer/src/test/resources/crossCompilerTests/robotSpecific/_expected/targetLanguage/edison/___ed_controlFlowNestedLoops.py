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

# Control Flow Nested Loop --Start
while True:
    while not (___X >= 20):
        for ___i in range(11):
            for ___k0 in range(2):
                if (___i % 2) == 0:
                    continue
                ___X += 1
    break
for ___j in range(4):
    ___X += 1
    for ___k in range(5):
        ___X += 1
while True:
    while True:
        if 23 == ___X:
            while True:
                if (___X % 2) == 0:
                    continue
                ___X += 1
                break
            if (___X % 2) == 0:
                break
            ___X += 1000
        break
    break
# Control Flow Nested Loop -- End

