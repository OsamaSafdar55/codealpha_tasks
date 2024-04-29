              
                                                                       
                                                                        # Voice Assistant

import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def WishMe():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak ("Good Morning Sir! ")

  elif hour >12 and hour <18:
    speak ("Good Afternoon Sir ! ")

  else:
    speak("Good Evening Sir !")


  speak ( "Hello Sir I am Jarvis.How May I help you? ")  
    

def TakeCommand():
  r=sr.Recognizer()
  with sr.Microphone() as source:
    print ("Listening...")
    r.pause_threshold = 0.5
    audio = r.listen(source)
    
    
  try:
    print ("Recognizing....")
    query = r.recognize_google(audio ,  )
    print ("User said : ", query)
 
  except Exception as e:
    print (e)
    print ("Say that again please.....")
    return "None"
  return query

  



if __name__ == "__main__":
    
  
  WishMe()
  if 1:
    query = TakeCommand().lower()

    if 'wikipedia' in query:
      speak('Searching Wikipedia...')
      query= query.replace("wikipedia", "")
      results = wikipedia.summary(query, sentences=2)
      speak("According To Wikipedia ")
      print (results)
      speak(results)

    elif 'open youtube' in query:
      webbrowser.open("youtube.com")
      
    elif 'open google' in query:
      webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
      webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
      music_dir = 'D:\\Songs'
      songs = os.listdir(music_dir)
      print(songs)
      random_song = random.choice(songs)
      os.startfile(os.path.join(music_dir, random_song))
    
    elif 'time' in query:
      strTime = datetime.datetime.now().strftime("%H : %M : %S ")
      print(strTime)
      speak(f"Sir! The Time is : {strTime}")
    
    elif 'open visual studio' in query:
      code_path = "C:\\Users\\Osama\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
      os.startfile(code_path)

    elif 'open obs studio' in query:
      code_path = "C:\Program Files\obs-studio\bin\64bit\obs64.exe"
      os.startfile(code_path)

    elif 'open google chrome' in query:
      code_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
      os.startfile(code_path)

    elif 'open epic lanucher' in query:
      code_path = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
      os.startfile(code_path)

