#!/usr/bin/env python
#
# Copyright 2010 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

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
import MySQLdb

doss = os.getcwd()
i=0
n=0

INFO = '''
        +=======================================+
        |.....JARVISE VIRTUAL INTELLIGENCE......|
        +---------------------------------------+
        |#Author: Valentin Genard               |
        |#Date: 01/06/2016                      |
        |#Changing the Description of this tool |
        | Won't made you the coder              |
        |#I don't take responsability for       |
        | problems of any kind                  |
        +---------------------------------------+
        |.....JARVISE VIRTUAL INTELLIGENCE......|
        +=======================================+
        |              OPTIONS:                 |
        |#hello/hi     #goodbye    #sleep mode  |
        |#your name    #jarvis     #what time   |
        |#asite.com    #next music #music       |
        |#pause music  #wifi       #thank you   |
        |#start/stop someapp                    |
        |#pip install/uninstall anapp          |
        |#googlemaps tanyplace                  |
        +=======================================+
        '''
#print(INFO)
connection = MySQLdb.connect (host = "localhost", user = "root", passwd = "", db = "va")
cursor = connection.cursor ()
#cursor.execute ("select pingrediants from pinfo where pname='bread'")
#data = cursor.fetchall ()
#for row in data :
 #   print 'bread ingrediants   - ',row[0]

# JARVIS'S EARS========================================================================================================== SENSITIVE BRAIN
                                                   # obtain audio
while (i<1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.adjust_for_ambient_noise(source)
        n=(n+1)     
        print("Say something!")
        audio = r.listen(source)
                                                   # interprete audio (Google Speech Recognition)
    try:
        s = (r.recognize_google(audio))
        message = (s.lower())
        print (message)


# POLITE JARVIS ============================================================================================================= BRAIN 1

        if ('bread ingrediants') in message:                          
            cursor.execute ("select pingrediants from pinfo where pname='bread'")
            data = cursor.fetchall ()
            for row in data :
                print 'bread ingrediants   - ',row[0]
                rand = ['bread ingrediants are',row[0]]
            speekmodule.speek(rand,n,mixer)
            break

        if ('where') in message:
            if ('find') in message:
                if('bread') in message:
                    cursor.execute ("select shelf from product where product_name='bread'")
                    data = cursor.fetchall ()
                    for row in data :
                        print 'breads are in shelf ',row[0]
                        rand = ['bread are in shelf'+row[0]]
                        speekmodule.speek(rand,n,mixer)
                if('biscuit') in message:
                    cursor.execute ("select shelf from product where product_name='Biscuit'")
                    data = cursor.fetchall ()
                    for row in data :
                        print 'biscuit are in shelf ',row[0]
                        rand = ['biscuit with nuts is'+row[0]]
                        speekmodule.speek(rand,n,mixer)
            #break

        if ('bread') in message:
            if ('with') in message:
                if('peanut') in message:
                    cursor.execute ("select product_name from product join prod_ingri on product.product_id=prod_ingri.product_id join ingrident on ingrident.ingri_Id=prod_ingri.ingri_Id where ingrident.ingri_name ='egg'")
                    data = cursor.fetchall ()
                    for row in data :
                        print 'bread with peanuts',row[0]
                        rand = ['bread with peanuts is'+row[0]]
                        speekmodule.speek(rand,n,mixer)
            if ('without') in message:
                if('peanut') in message:
                    cursor.execute ("select product_name from product join prod_ingri on product.product_id=prod_ingri.product_id join ingrident on ingrident.ingri_Id=prod_ingri.ingri_Id where not ingrident.ingri_name ='egg'")
                    data = cursor.fetchall ()
                    for row in data :
                        print 'bread with peanuts',row[0]
                        rand = ['bread with peanuts is'+row[0]]
                        speekmodule.speek(rand,n,mixer)
            #break
        
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


    # exceptions
    except sr.UnknownValueError:
        print("$could not understand audio")
    except sr.RequestError as e:
        print("Could not request results$; {0}".format(e))
