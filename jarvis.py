import pyttsx3
import datetime
import speech_recognition as sp
import wikipedia
import webbrowser
import time
  


engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
      engine.say(audio)
      engine.runAndWait()
      
      
def wishme():
       currentTime = datetime.datetime.now()
       x= currentTime.hour
       
       if x<12:
             speak("good morning sir")
       elif x<18:
             speak("good afternoon sir")
       else :
             speak("good evening masterr")
     
         
            
       speak("i am your ai  , how can i help you ?")
      
      

def takeCommand():
      
      r= sp.Recognizer()
      
      with  sp.Microphone()  as  source:
            print("listening.....")
            r.pause_threshold = 1
            audio= r.listen(source)
            
            
      try:
            print("recognizing.....")   
            query = r.recognize_google(audio, language="en-in")   
            print(f"user said :{query}")
            
      except Exception as e:
            print("say the command again")   
            return "None"   
      return query


  
if __name__ == "__main__":
       wishme()
        
       while True:
             query= takeCommand().lower()
             
             if  "wikipedia" in query:
                   speak("searching in wikipedia")
                   
                   query = query.replace("wikipedia","")
                   result= wikipedia.summary(query,sentences=2)
                   speak("according to wikipedia")
                   print(result)
                   speak(result)
                   
             elif "open youtube" in query:
                   webbrowser.open("youtube.com")
      
             elif "open google"  in query:    
                   webbrowser.open("google.com")
        
             elif "open telegram" in query:
                   webbrowser.open("telegram.com")
                   
             elif "open whatsapp" in query:
                   webbrowser.open("whatsapp.com") 
                   
             elif "open facebook" in query:
                   webbrowser.open("facebook.com")
                   
             elif "open instagram" in query:
                   webbrowser.open("insatgram.com")
                   
             elif "open stack overflow" in query:
                   webbrowser.open("stackoverflow.com")     
          
             else :
                   speak("unable to understand please tell again") 