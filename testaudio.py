import pyttsx4

def main():
    # Initialize the pyttsx4 engine
    engine = pyttsx4.init()

    # Set voice
    voices = engine.getProperty('voices')

    print("Available Voices:")
    i = 0
    for voice in voices:
#        print("-" * 30)

        print(i, "ID:", voice.id)
#        print("Name:", voice.name)
#        print("Languages:", voice.languages)
#        print("Gender:", voice.gender)
#        print("Age:", voice.age)
        i+=1

    engine.setProperty('voice', voices[44].id)  # Change the index to select a different voice

    # Set speech rate (words per minute)
    engine.setProperty('rate', 120)  # Adjust the value as needed

    # Set volume (0.0 to 1.0)
    engine.setProperty('volume', 0.5)  # Adjust the value as needed

    # Set pitch (0.0 to 1.0)
    engine.setProperty('pitch', 0.3)  # Adjust the value as needed

    # Say something
    text_to_speak = "Hello, how are you?"
    try:
        engine.say(text_to_speak)
        engine.runAndWait()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
