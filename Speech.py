
import pyaudio
import speech_recognition as sr
from pygame import mixer
import os
import random
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
import speekmodule

doss = os.getcwd()
i=0
n=0

INFO = '''
        +=======================================+
        |.....JARVISE VIRTUAL INTELLIGENCE......|
        +---------------------------------------+
       
        +---------------------------------------+
        |.....JARVISE VIRTUAL INTELLIGENCE......|
        +=======================================+
        |              OPTIONS:                 |
        |#hello/hi     #goodbye    #sleep mode  |
        |#your name    #jarvis     #what time   |
        +=======================================+
        '''
print(INFO)
                                                 # obtain audio
                                                   
while (i<1):
    r = sr.Recognizer()
    with sr.AudioFile("D:\\c drive\\Downloads\\hello.wav") as source:
        audio = r.record(source)
        #audio = r.listen(audio)
        #print(type(audio))
                                                   # interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())
        print (message)
        i=1


# POLITE JARVIS ============================================================================================================= BRAIN 1
    
        if ('goodbye') in message:                          
            rand = ['Goodbye Sir', 'Jarvis powering off in 3, 2, 1, 0']
            speekmodule.speek(rand,n,mixer)
            break
            
        if ('hello') in message or ('hi') in message:
            rand = ['Wellcome to Jarvis virtual intelligence project. At your service sir.']
            speekmodule.speek(rand,n,mixer)

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = ['You are wellcome', 'no problem']
            speekmodule.speek(rand,n,mixer)

        if message == ('jarvis'):
            rand = ['Yes Sir?', 'What can I doo for you sir?']
            speekmodule.speek(rand,n,mixer)

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand = ['Fine thank you']
            speekmodule.speek(rand,n,mixer)

        if  ('*') in message:
            rand = ['Be polite please']
            speekmodule.speek(rand,n,mixer)

        if ('your name') in message:
            rand = ['My name is Jarvis, at your service sir']
            speekmodule.speek(rand,n,mixer)

        
        if ('light on') in message:
            rand = ['lights onn']
            speekmodule.speek(rand,n,mixer)

        if ('light off') in message:
            rand = ['lights off']
            speekmodule.speek(rand,n,mixer)


        if ('fan off') in message:
            rand = ['Table fan offf']
            speekmodule.speek(rand,n,mixer)


        if ('fan on') in message:
            rand = ['Table fan on']
            speekmodule.speek(rand,n,mixer)



    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
