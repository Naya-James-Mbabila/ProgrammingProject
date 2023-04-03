'''Naya James Mbabila 
Student ID  10964513
Biomedical Engineering Department
Project 2 problem 1'''
import pyttsx3 as pt
import PySimpleGUI as sg

engine = pt.init()
Voice_Kind = engine.getProperty('voices')

layout=[
[sg.Input(key = 'Input'), sg.Button('Speak', key='Speak_BUTTON')],
[ sg.Text(' Select Voice Type', key='Voice'), sg.Radio('Male', 'RADIO1', default=True, key = 'MALE_BUTTON',), sg.Radio('Female','RADIO1', key='FEMALE_BUTTON')],
]
window = sg.Window(' Text to speech App', layout )
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    elif event == 'Speak_BUTTON':
        text = values['Input']
        
        if values['MALE_BUTTON']:
            engine.setProperty('voice',  'Voice ID HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
            engine.setProperty('rate', 130)
            engine.setProperty('volume', 1) 


        if values['FEMALE_BUTTON']:
            engine.setProperty('voice', Voice_Kind[1].id)        
            engine.setProperty('rate', 130)
            engine.setProperty('volume', 1.5) 
        engine.say(text)
        engine.runAndWait()

window.read()
        
