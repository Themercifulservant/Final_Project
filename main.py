import speech_recognition as sr
from tkinter import*
from tkinter.filedialog import *
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes


# root = Tk()
# root.geometry('300x300')
# root.title('Virtual Assistant')
# text = Label(root, text = 'I Am Your Personal Virtual Assistant. Ask Me Anything')
# text.pack()
# photo = PhotoImage(file = 'Image.png')
# root.mainloop()

screen = Tk()
screen.title("Virtual Assistant")
screen.geometry("1000x2500")
# screen.iconbitmap('app_icon.ico')

name_label = Label(text="Ask Me AnyThing", width=1500,  fg="green", font=("Calibri", 13))
name_label.pack()

microphone_photo = PhotoImage(file="Image.png", width=750)
microphone_button = Button(image=microphone_photo)
microphone_button.pack(pady=10)
screen.mainloop()

# settings_photo = PhotoImage(file="settings.png")
# settings_button = Button(image=settings_photo, command=change_name_window)
# settings_button.pack(pady=10)



listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='EN')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('Sorry via, I am in another relation')
    elif 'how are you' in command:
        talk('i am fine and you?')

    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)


while True:

    run_alexa()