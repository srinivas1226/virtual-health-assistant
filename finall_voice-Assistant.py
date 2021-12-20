import pyttsx3
import operator
import speech_recognition as sr
import datetime
 
import wikipedia
import webbrowser
import os
import winshell 
import time
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
        print("Good Afternoon!")

    else:
        speak("Good Evening!")
        print("Good Evening!")

    speak("I am pi sir. How can I help you Sir")
    print("I am pi sir. How can I help you Sir")


def takeCommand():
    # its takes query from microphone and returns as string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognising....") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please....")
        speak("Say that again please....")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            os.system("pause")

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            os.system("pause")

        elif 'open amazon' in query:
            webbrowser.open_new_tab("https://www.amazon.in")
            speak("Amazon is open now")
            os.system("pause")

        elif 'open flipkart' in query:
            webbrowser.open_new_tab("https://www.flipkart.com")
            speak("flipkart is open now")
            os.system("pause")

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google is open now")
            os.system("pause")

        elif 'open gmail' in query:
            webbrowser.open_new_tab("https://accounts.google.com/login")
            speak("Google Mail is open now")
            os.system("pause")

        elif "what's time now" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The Time is {strTime}")
            print(f"Sir, The Time is {strTime}")
            os.system("pause")

        elif 'locate' in query:
            query = query.replace("locate", "")
            query = query.replace("where is", "")
            location = query
            speak("Sir here is")
            print("Sir here is")
            speak("location")
            webbrowser.open(
                "https://www.google.com/maps/place/" + location + "")
            os.system("pause")

        elif 'search' in query or 'what is' in query or 'who is' in query:
            query = query.replace("search", "")
            query = query.replace("what is", "")
            query = query.replace("who is", "")
            webbrowser.open_new_tab(query)
            os.system("pause")

        elif 'good morning' in query:
            speak("A warm good morning")
            print("A warm good morning")
            speak("How are you Sir")
            print("How are you Sir")
        elif 'who are you' in query:
            speak("I am your pi created by Creative Group!")
            print("I am your pi created by Creative Group!")
        elif 'hi' in query or 'hello' in query or 'hai' in query:
            speak("Hey There Whats up")
            print("Hey There Whats up")
        elif 'how are you' in query:
            speak("I am fine, Sir")
            print("I am fine, Sir")
            speak("How r you ")
            print("How r you ")
        elif 'fine' in query:
            speak("It's good to know that your fine")
            print("It's good to know that your fine")
            os.system("pause")
        elif 'who made you' in query or 'who created you' in query:
            speak("I have been created by Creative Group!")
            print("I have been created by Creative Group!")
            os.system("pause")
        
        #Health assistant started 
        
        elif 'what can you do' in query:
            speak("I can give you some tips for your health and i can also prescribe Medicines for You")
            print("I can give you some tips for your health and i can also prescribe Medicines for You")

        elif 'i am suffering from fever' in query or 'fever' in query or 'suffering from fever' in query:
            speak("You can take paracetamol or asprin")
            print("You can take paracetamol or asprin")
            os.system("pause")
  
        elif 'i am suffering from headache' in query or 'headache' in query or 'suffering from headache' in query:
            speak("You can take disprin")
            print("You can take disprin") 
            os.system("pause")
   
        elif 'i am suffering from cough and cold' in query or 'cough and cold' in query or 'suffering from cough and cold' in query:
            speak("You can take amoxicillin")
            print("You can take amoxicillin")
            os.system("pause")

        elif 'i am suffering from diabetes' in query or 'diabetes' in query or 'suffering from diabetes' in query:
            speak("You can take insulin lispro")
            print("You can take insulin lispro")
            os.system("pause")

        elif 'i am suffering from stomach ache' in query or 'stomach ache' in query or 'suffering from stomach ache' in query:
            speak("You can take panadol")
            print("You can take panadol")
            os.system("pause")

        elif 'i am suffering from skin allergy' in query or 'allergy' in query or 'suffering from allergy' in query:
            speak("You can take allegra")
            print("You can take allegra")
            os.system("pause")

        elif 'i am suffering from vomiting' in query or 'vomiting' in query or 'suffering from vomiting' in query:
            speak("You can take dolasetron")
            print("You can take dolasetron")
            os.system("pause")

        elif 'i am suffering from depression' in query or 'depression' in query or 'suffering from depression' in query:
            speak("You can take lexapro")
            print("You can take lexapro")
            os.system("pause")

        elif 'i am suffering from chickenpox' in query or 'chickenpox' in query or 'suffering from chickenpox' in query:
            speak("You can take a cool bath with added baking soda and you can also take benadryl")
            print("You can take a cool bath with added baking soda and you can also take benadryl")
            os.system("pause")

        elif 'i am suffering from arthritis' in query or 'arthritis' in query or 'suffering from arthritis' in query:
            speak("You can take immunosupressive drug and analgesic")
            print("You can take immunosupressive drug and analgesic")
            os.system("pause")

        elif 'i am suffering from asthma' in query or 'asthma' in query or 'suffering from asthma' in query:
            speak("You have to quit smoking and can take anti inflammatory drug")
            print("You have to quit smoking and can take anti inflammatory drug")
            os.system("pause")

        elif 'i am suffering from bipolar disorder' in query or 'bipolar disorder' in query or 'suffering from bipolar disorder' in query:
            speak("You can take antipsychotic drugs")
            print("You can take antipsychotic drugs")
            os.system("pause")

        elif 'i am suffering from chest pain' in query or 'chest pain' in query or 'suffering from chest pain' in query:
            speak("You can take nitroglycerine drugs")
            print("You can take nitroglycerine drugs")
            os.system("pause")

        elif 'i am suffering from conjunctvitis' in query or 'conjunctvitis' in query or 'suffering from conjunctvitis' in query:
            speak("You can maintain hygeine and self heal with cold compress")
            print("You can maintain hygeine and self heal with cold compress")
            os.system("pause")

        elif 'i am suffering from constipation' in query or 'constipation' in query or 'suffering from constipation' in query:
            speak("You can take stool softener and fibre supplement")
            print("You can take stool softener and fibre supplement")
            os.system("pause")

        elif 'i am suffering from dehydration' in query or 'dehydration' in query or 'suffering from dehydration' in query:
            speak("You can take oral rehydration solution")
            print("You can take oral rehydration solution")
            os.system("pause")

        elif 'i am suffering from food poison' in query or 'food poison' in query or 'suffering form food poison' in query:
            speak("ensure adequate hydration and take rehydration solution")
            print("ensure adequate hydration and take rehydration solution")
            os.system("pause")

        elif 'i am suffering from flu' in query or 'flu' in query or 'suffering from flu' in query:
            speak("You can take bed rest and antiviral drug ")
            print("You can take bed rest and antiviral drug ")
            os.system("pause")

        elif 'i am suffering from indigestion' in query or 'indigestion' in query or 'suffering from indigestion' in query:
            speak("You can take antacids and oral suspension medicines")
            print("You can take antacids and oral suspension medicines")
            os.system("pause")

        elif 'i am suffering from insomnia' in query or 'insomnia' in query or 'suffering from insomnia' in query:
            speak("You can take sedatives and anti depressants")
            print("You can take sedatives and anti depressants")
            os.system("pause")

        elif 'i am suffering from malaria' in query or 'malaria' in query or 'suffering from malaria' in query:
            speak("You can take anti parasites and antibiotics")
            print("You can take anti parasites and antibiotics")
            os.system("pause")

        elif 'i am suffering from malnutrition' in query or 'malnutrition' in query or 'suffering from malnutrition' in query:
            speak("You can high protein diet and nutiritive suppliments")
            print("You can high protein diet and nutiritive suppliments")
            os.system("pause")

        elif 'i am suffering from obesity' in query or 'obesity' in query or 'suffering from obesity' in query:
            speak("You  have to do physical exercise and take low fat diet")
            print("You  have to do physical exercise and take low fat diet")
            os.system("pause")

        elif 'i am suffering from panic disorder' in query or 'panic disorder' in query or 'suffering from panic disorder' in query:
            speak("You can take anti depressants")
            print("You can take anti depressants")
            os.system("pause")

        elif 'i am suffering from scabies' in query or 'scabies' in query or 'suffering from scabies' in query:
            speak("You can take anti parasite drugs")
            print("You can take anti parasite drugs")
            os.system("pause")

        elif 'i am suffering from Jaundice' in query or 'Jaundice' in query or 'suffering from Jaundice' in query:
            speak("You can take oral rehydration therapy and in critical case consult doctor")
            print("You can take oral rehydration therapy and in critical case consult doctor")
            os.system("pause")

        elif 'i am suffering from acne' in query or 'acne' in query or 'suffering from acne' in query:
            speak("You can apply aloe vera and take vitamin a derivatives")
            print("You can apply aloe vera and take vitamin a derivatives")
            os.system("pause")  

        elif 'thank you' in query:
            speak("welcome sir")
            print("welcome sir")
            os.system("pause")

        elif '' in query:
            speak("i did not recognise you")
            print("i did not recognise you")
            os.system("pause") 
           