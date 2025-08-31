def main():
    import speech_recognition as sr

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio,language="zh-CN")
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError as e:
        print("API error:", e)
    
    try:
        text = r.recognize_google(audio,language="en-US")
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError as e:
        print("API error:", e)        
        
        
        
    

if __name__ == "__main__":
    main()



