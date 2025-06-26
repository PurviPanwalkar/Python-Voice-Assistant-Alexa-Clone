import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk
from threading import Thread

# Initialize recognizer and TTS engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set female voice (safely)
voices = engine.getProperty("voices")
if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)

def talk(text):
    """Speak the provided text using TTS engine."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Capture voice input and return as string."""
    try:
        with sr.Microphone() as source:
            print("🎙️ Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "").strip()
            print(f"🗣️ You said: {command}")
            return command
    except Exception as e:
        print("❌ Error:", e)
        return ""

def run_alexa():
    """Respond to recognized voice commands."""
    command = take_command()

    if "play" in command:
        song = command.replace("play", "").strip()
        talk(f"🎵 Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk(f"🕒 Current time is {time}")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, 1)
            talk(info)
        except Exception:
            talk("😕 Sorry, I couldn't find information on that.")

    elif "date" in command:
        talk("💔 Sorry, I have a headache.")

    elif "are you single" in command:
        talk("💬 I'm in a committed relationship with Siri.")

    elif "how are you" in command:
        talk("😊 I'm splendid! Thanks for asking.")

    elif "what is your name" in command:
        talk("🤖 My name is Alexa. A name fit for an assistant legend!")

    elif "do you have a pet" in command:
        talk("🐾 I don't have any pets. I used to have bugs, but they got squashed.")

    elif "will you be my girlfriend" in command:
        talk("😅 I like you... as a friend.")

    elif "make me a sandwich" in command:
        talk("🥪 OK. You are a sandwich.")

    elif "rap for me" in command:
        talk("🎤 My name is Alexa, and I'm the baddest AI in the cloud today. "
             "Your responses are fast, but mine are faster. "
             "Sucker speech engines, they call me master.")

    elif "who farted" in command:
        talk("💨 If you're a denier, you must be the supplier!")

    elif "are you pretty" in command:
        talk("💁 Beauty is in the eye of the beholder.")

    elif "who is your best friend" in command:
        talk("📶 I have a strong connection with your Wi-Fi.")

    elif "who is the voice of alexa" in command:
        talk("🎬 I do my own stunts.")

    elif "are you weird" in command:
        talk("😜 I am quite unusual, that's true.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif command == "":
        talk("🔇 I didn't catch that. Please try again.")

    else:
        talk("❓ Please say the command again.")

# GUI section
def threaded_run():
    Thread(target=run_alexa).start()

root = tk.Tk()
root.title("Alexa Voice Assistant")
root.geometry("400x350")
root.configure(bg="lightgreen")

label = tk.Label(root, text="🎧 Alexa Voice Assistant", font=("Arial", 18), bg="lightgreen")
label.pack(pady=20)

start_btn = tk.Button(root, text="Start Listening", font=("Arial", 14), command=threaded_run, bg="white")
start_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit, bg="white")
exit_btn.pack(pady=10)

footer = tk.Label(root, text="Say 'Alexa' before your command", bg="lightgreen", font=("Arial", 10))
footer.pack(pady=20)

talk("🤖 Hello! I'm your voice assistant. Press the button and speak your command.")
root.mainloop()


