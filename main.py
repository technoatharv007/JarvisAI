import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import sys
import psutil
import subprocess
# all program imported


# Initialize the engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set the desired voice index or name (change to your preferred voice)
new_voice_index = 1     # 1 for female and 0 for male voice
engine.setProperty('voice', voices[new_voice_index].id)

# spoke out the results
def say(text):  # spoke out result
    engine.say(text)
    engine.runAndWait()


# open microsoft edge
def open_edge_browser():
    try:
        # Open Microsoft Edge
        subprocess.Popen('msedge')
        print("Microsoft Edge opened successfully.")
    except OSError as e:
        print(f"Error: {e}")


# open whatsapp
def open_whatsapp():
    os.startfile("whatsapp://")


# open camera
def open_camera():
    os.startfile("microsoft.windows.camera:")


# open calculator
def open_calculator():
    os.startfile("calc.exe")


def open_calculator():
    if sys.platform == "win32":
        os.startfile("calc.exe")


# Function to save the spoken text to a notepad file
def save_to_file(text):
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = os.path.join(desktop_path, f"recorded_note_{timestamp}.txt")

    with open(file_name, "w") as file:
        file.write(text)
        print(f"Speech saved to {file_name}")


# open calendar
def open_calendar():
    if sys.platform == "win32":
        os.startfile("outlookcal:")
        open_calendar()


# open whether app
def open_weather_application():
    weather_path = "ms-weather:"  # Use the "ms-weather:" protocol to open the default weather app on Windows
    os.startfile(weather_path)


# tell about day
def get_current_day():
    now = datetime.datetime.now()
    day = now.strftime("%A")  # Get the full name of the current day
    return day


def check_running_processes():
    initial_processes = psutil.process_iter()
    while True:
        current_processes = psutil.process_iter()
        new_processes = [p for p in current_processes if p not in initial_processes]
        if new_processes:
            # New process detected, exit the code
            break


# say command as function
def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)  # Adjust the rate (speed)
    engine.say(text)
    engine.runAndWait()


# show logo of JARVIS.AI
def open_logo():
    os.startfile("logo.png")


# take command from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        say("Sorry for inconvenience but I am unable to understand what you said")
        return ""
    except sr.RequestError:
        say("Sorry, the speech recognition service is currently unavailable.")
        return ""


# setting up the mic for command
recognizer = sr.Recognizer()
if __name__ == '__main__':
    print('JARVIS.AI')
    say("JARVIS AI WELCOMES YOU ")
    while True:

        query = takeCommand()

        # will open websites
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["facebook", "https://www.facebook.com"], ["google", "https://www.google.com"],
                 ["chat GPT", "https://chat.openai.com"], ["spotify", "https://open.spotify.com"],
                 ["instagram", "https://www.instagram.com"], ["chrome", "https://www.google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} sir.....")
                webbrowser.open(site[1])
                check_running_processes(exit)

        # some general question

        # welcome
        welcome_phrases = ["Hi", "Hello", "Hello Jarvis", "hi Jarvis", "how are you", "how are you Jarvis"]

        for i, phrase in enumerate(welcome_phrases, 1):
            if phrase in query.lower():
                responses = {
                    1: "Hello, how can I assist you today?",
                    2: "Hello, how can I assist you today?",
                    3: "Hello, how can I assist you today?",
                    4: "Hello, how can I assist you today?",
                    5: "I'm doing good, how about you?",
                    6: "I'm doing good, how about you?"
                    # Add more responses as needed
                }
                if i in responses:
                    say(responses[i])
                break

        # name
        name_phrases = ["what is your name", "your name", "can I know your name", "may I know your name"]

        for i, phrase in enumerate(name_phrases, 1):
            if phrase in query.lower():
                responses = {
                    1: "My name is JARVIS.",
                    2: "I am called JARVIS.",
                    3: "Certainly, I'm called JARVIS.",
                    4: "Yes, my name is JARVIS."
                    # Add more responses as needed
                }
                if i in responses:
                    say(responses[i])
                break
            # personal touch
            # List of personal touch questions
            personal_touch = [
                "who created you", "who created jarvis", "who created you jarvis",
                "who is your favourite singer", "who is your favourite youtuber",
                "which weather you like", "which season you like the most",
                "which is your favourite game", "why your name is jarvis",
                "which is your favourite colour", "do you drink water",
                "do you eat food", "what is your favourite food",
                "what is your purpose", "what is your job", "what is your role",
                "are you human", "are you a robot", "are you a machine",
                "do you sleep", "can you dream", "do you have feelings",
                "what is the meaning of life", "what is love", "what is happiness",
                "can you tell jokes", "can you sing", "can you dance",
                "can you laugh", "can you cry", "can you feel pain",
                "do you have a family", "do you have friends", "do you have a pet",
                "can you learn", "can you improve", "can you think",
                "can you make decisions", "do you have a memory", "can you forget things",
                # Add more questions here...
            ]

            # Dictionary containing responses to the questions
            responses = {
                "who created you": "I was created by a team of developers.",
                "who created jarvis": "I am a product of collaborative effort.",
                "who created you jarvis": "I was developed by a team of engineers.",
                "who is your favourite singer": "I don't have personal preferences as I am an AI.",
                "who is your favourite youtuber": "I don't have personal preferences as I am an AI.",
                "which weather you like": "I don't have personal preferences as I am an AI.",
                "which season you like the most": "I don't have personal preferences as I am an AI.",
                "which is your favourite game": "I don't have personal preferences as I am an AI.",
                "why your name is jarvis": "My name was chosen by ATHARV he is obsessed by marvel.inc and named me after the tony stark's machine.",
                "which is your favourite colour": "I don't have personal preferences as I am an AI.",
                "do you drink water": "As an AI, I don't have physical needs.",
                "do you eat food": "As an AI, I don't have physical needs.",
                "what is your favourite food": "I don't have personal preferences as I am an AI.",
                "what is your purpose": "My purpose is to assist and provide information.",
                "what is your job": "My job is to assist users and provide information.",
                "what is your role": "My role is to assist users and provide information.",
                "are you human": "No, I'm an artificial intelligence.",
                "are you a robot": "Yes, I am a robot in a sense, but not a physical one.",
                "are you a machine": "Yes, I am a machine, an artificial intelligence.",
                "do you sleep": "As an AI, I don't require sleep.",
                "can you dream": "No, dreaming is a human experience.",
                "do you have feelings": "As an AI, I don't have emotions.",
                "what is the meaning of life": "The meaning of life varies for each individual.",
                "what is love": "Love can have different meanings depending on context.",
                "what is happiness": "Happiness is a positive emotional state.",
                "can you tell jokes": "Yes, I can tell jokes! Here's one: Why don't scientists trust atoms? Because they make up everything!",
                "can you sing": "I can't sing, but I can recite lyrics for you.",
                "can you dance": "I can't dance physically, but I can provide information about dancing.",
                "can you laugh": "I can't laugh physically, but I understand humor.",
                "can you cry": "As an AI, I can't cry because I don't have emotions.",
                "can you feel pain": "As an AI, I can't feel physical pain.",
                "do you have a family": "I don't have a family in the human sense.",
                "do you have friends": "I consider everyone I assist as my friends!",
                "do you have a pet": "I don't have pets as I am an AI.",
                "can you learn": "Yes, I can learn from interactions and new information.",
                "can you improve": "Yes, I strive to improve based on user interactions.",
                "can you think": "I can process information and respond based on programming.",
                "can you make decisions": "I follow programmed instructions to provide information and assistance.",
                "do you have a memory": "I have a storage system for processing data but not a human-like memory.",
                "can you forget things": "I don't forget information once it's stored unless explicitly programmed.",
                # Add more responses for other questions...
            }

            # Matching user's query with responses
            for question in personal_touch:
                if question.lower() in query.lower():
                    for response_question, response in responses.items():
                        if response_question == question.lower():
                            say(response)
                            break
                    break

            if "date is today" in query.lower():
                now = datetime.datetime.now()
                current_date = now.strftime("%B %d, %Y")
                say(f"Today's date is {current_date}")
                break

            if "your logo" in query.lower():
                say("Opening my logo. please wait")
                open_logo()
                check_running_processes(exit)
                break

            if "the time" in query.lower():  # date and time
                now = datetime.datetime.now()
                current_time = now.strftime("%I:%M %p")
                say(f"The current time is {current_time}")
                break

            if "save to file" in query.lower():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("listening please dictate")
                    audio = r.listen(source)
                try:
                    print("compiling......")
                    text = r.recognize_google(audio, language="en-in")
                    print(f"User said: {text}")
                finally:
                    save_to_file(text)



        if "exit" in query:
            check_running_processes(exit)

        apps = [["file explorer", r"C:\Users\My\Desktop\File Explorer.lnk"],
                ["minecraft", r"C:\Users\Public\Desktop\TLauncher.lnk"],
                ["microsoft edge", r"C:\Users\Public\Desktop\Microsoft Edge.lnk"],
                ["anydesk", r"C:\Users\My\Downloads\AnyDesk.exe"], ["notepad", r"C:\Windows\notepad.exe"],
                ["wordpad", r"C:\Windows\write.exe"], ["explorer", r"C:\Windows\explorer.exe"]]
        for app in apps:
            if f"open {app[0].lower()}" in query.lower():
                say(f"Opening {app[0]}. This may take a few moments.")
                os.system(app[1])
                check_running_processes(exit)
                break
            if "open whatsapp" in query.lower():
                say("Opening WhatsApp. this may take few moment")
                open_whatsapp()
                check_running_processes(exit)
                break
            if "open camera" in query.lower():
                say(" Opening Camera. this may take few moment")
                open_camera()
                check_running_processes(exit)
                break
            if "open calculator" in query.lower():
                say("Opening Calculator. Please wait.")
                open_calculator()
                check_running_processes(exit)
                break
            if "do nothing" in query.lower():
                say("as you wish")
                break

            if "open calendar" in query.lower():
                say("Opening Calendar. this may take few moment")
                open_calendar()
                check_running_processes(exit)
                break
            else:
                pass
