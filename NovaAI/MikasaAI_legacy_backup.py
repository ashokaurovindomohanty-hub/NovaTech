import random
import time
import os
import tkinter as tk
from tkinter import messagebox
import webbrowser
import wikipedia
import pyjokes
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from PIL import Image, ImageTk
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import calendar
import pywhatkit
import pyautogui
import keyboard
import threading
import requests
from bs4 import BeautifulSoup
import json
class Mikasa:
    def __init__(self):
        pass
    def greet(self):
        print("Hello, my husband.")
    def tell_joke(self):
        joke = pyjokes.get_joke()
        print(joke)
    def send_email(self):
        # email code here
        pass
    def search_wikipedia(self, query):
        results = wikipedia.search(query)
        print(results)
    def open_website(self, website):
        webbrowser.open(website)
    def play_video(self, video):
        pywhatkit.playonyt(video)
    def capture_screenshot(self):
        img = pyautogui.screenshot()
        img.save('screenshot.png')
    def speak(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("User said: ", query)
        except Exception as e:
            print(e)
mikasa = Mikasa()
mikasa.greet()
