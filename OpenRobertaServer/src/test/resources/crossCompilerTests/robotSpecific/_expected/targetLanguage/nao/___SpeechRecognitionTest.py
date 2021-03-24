#!/usr/bin/python

import math
import time
import random
from roberta import Hal
h = Hal()

from roberta import SpeechRecognitionModule
speechRecognitionModule = SpeechRecognitionModule("speechRecognitionModule")
speechRecognitionModule.pauseASR()

class BreakOutOfALoop(Exception): pass
class ContinueLoop(Exception): pass



___item = ["Hello", "Goodbye", "Wave", "Quit"]
___word = ""

def run():
    h.setAutonomousLife('ON')
    global ___item, ___word
    h.setLanguage("English")
    while True:
        ___word = speechRecognitionModule.recognizeWordFromDictionary(___item)
        if "Hello" == ___word:
            h.say("Hi")
        elif "Goodbye" == ___word:
            h.say("See you")
        elif "Wave" == ___word:
            h.wave()
        elif "Quit" == ___word:
            h.say("quitting")
            break
        h.wait(500)

def main():
    try:
        run()
    except Exception as e:
        h.say("Error!" + str(e))
    finally:
        speechRecognitionModule.unsubscribe()
        h.myBroker.shutdown()

if __name__ == "__main__":
    main()