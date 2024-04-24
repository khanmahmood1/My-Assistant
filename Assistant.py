
import sys
import threading
import tkinter as tk
import os


import speech_recognition
import pyttsx3 as tts

from neuralintents import BasicAssistant




class Assistant:

    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)

        self.assistant = BasicAssistant("intents.json", intent_methods = {"file" : self.create_file})
        self.assistant.train_model()

        self.root = tk.Tk()
        self.label = tk.Label(text="🤖", font=("Arial", 120, "bold"))
        self.label.pack()

        threading.Thread(target=self.run_assistant).start()



        self.root.mainloop()


    def create_file(self, **kwargs):
        with open("somefile.txt", "w") as f:
            f.write("WORLD:I AM DELUSIONAL\n User:I WANT TO LIVE IN DELUSION")

    def run_assistant(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    if "hey jake" in text:
                        self.label.config(fg="red")
                        audio = self.recognizer.listen(mic)
                        text = self.recognize_google(audio)
                        text = text.lower()
                        if text == "stop":
                            self.speaker.say("Bye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.destroy()
                            sys.exit()
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                        self.label.config(fg="black")

            except Exception as e:
                print(e)
                self.label.config(fg="black")
                continue

         
Assistant()

#IF YOU GOT ANY ERROR CONTACT ME 
