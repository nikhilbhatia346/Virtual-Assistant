from datetime import datetime
import wikipedia
import speech_recognition as sr  # to talk to alexa
import pyttsx3  # pyttsx3 means python text to speech, use this so alexa can talk to us
import pywhatkit  # to open applications like youtube
import pyjokes  # used to tell jokes

listener = sr.Recognizer()  # this listener will be able to recognize your voice
engine = pyttsx3.init()  # this engine will talk to us, init means to initialize the engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # the previous line and the current line is used to change the male voice of alexa to female
# engine.say('Hi, I am Alexa')
# engine.say('What can I do for you')
# engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():  # take command from us
    try:  # sometimes the microphone might not work or there is any other trouble
        with sr.Microphone() as source:  # using the microphone as the source, this will be the source of the audio
            print('listening...')
            voice = listener.listen(source)  # calling the speech recognition to listen to this source
            command = listener.recognize_google(voice)  # using the google api to covert the voice to text
            command = command.lower()  # make the command to the lowercase
            if 'alexa' in command:  # if the command has the name alexa in it then only print the command
                command = command.replace('alexa', '')  # put the empty string in the command instead of alexa
                print(command)

    except:  # don't do anything when the exception happens
        # print('hi')
        pass
    return command

def run_alexa():  # run the alexa
    command = take_command()  # use the function to take the command from the user
    print(command)
    if 'play' in command:  # if we want to play a song
        song = command.replace('play','')
        talk('playing' + song)
        # print('playing' + song)
        pywhatkit.playonyt(song)   # playonyt means play on youtube and pass in the song

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  # %I is the 12 hour format and %p is for the am or pm
        print(time)
        talk(time)

    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)  # get 1 line of information from the wikipedia from the wikipedia
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('No, I am in relationship with WIFI')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    else:
        talk('Please say the command again')

while True:  # continue running alexa
    run_alexa()




