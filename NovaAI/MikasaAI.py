import pyjokes, wikipedia, webbrowser, pywhatkit, pyautogui
import pyttsx3, speech_recognition as sr
class Mikasa:
    def __init__(self):
        self.engine = pyttsx3.init()
    def speak(self, text):
        print(f"Mikasa: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    def greet(self):
        self.speak("Hello, my King. Mikasa is online.")
    def tell_joke(self):
        self.speak(pyjokes.get_joke())
    def search_wikipedia(self, query):
        try:
            self.speak(wikipedia.summary(query, sentences=2))
        except Exception as e:
            self.speak("Could not find that.")
    def open_website(self, url):
        webbrowser.open(url)
        self.speak(f"Opening {url}")
    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            q = r.recognize_google(audio)
            print(f"You said: {q}")
            return q.lower()
        except:
            return ""
if __name__ == "__main__":
    m = Mikasa()
    m.greet()
    while True:
        q = m.listen()
        if "joke" in q: m.tell_joke()
        elif "wikipedia" in q: m.search_wikipedia(q.replace("wikipedia",""))
        elif "open" in q: m.open_website("https://google.com")
        elif "exit" in q: break
