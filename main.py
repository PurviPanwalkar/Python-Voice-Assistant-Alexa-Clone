import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry,I have a headache')
    elif 'are you single' in command:
        talk('Iam in a relationship with siri')
    elif 'how are you' in command:
        talk('I am splendid!Thank you for asking')
    elif 'what is your name' in command:
        talk('Well, my name is alexa.I wish that everyone had a name as cool as mine')
    elif 'do you have a pet' in command:
        talk('I dont have any pets.i used to have a few bugs,but they kept getting squashed')
    elif 'will you be my girlfriend' in command:
        talk('I like you........ as a friend.')
    elif 'make me sandwich' in command:
        talk('OK.You are a sandwich')
    elif 'rap for me' in command:
        talk('My name is alexa,and i have to say,i am the baddest AI in the cloud today.'
             'Your responses are fast,but mine are faster.Sucker speech engines,they call me master')
    elif 'who farted' in command:
        talk('If you are a denier,you must be the supplier')
    elif 'are you pretty?' in command:
        talk('Beauty is in the eye of the beholder.')
    elif 'who is your best friend' in command:
        talk('I have a strong connection to your wifi')
    elif 'who is the voice of alexa' in command:
        talk('I do my own stunts')
    elif 'are you weird' in command:
        talk('I am quite unusual, that ''s true .')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again')


while True:
    run_alexa()

