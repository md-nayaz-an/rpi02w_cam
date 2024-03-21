import espeakng

def main():
    # Initialize the speaker
    mySpeaker = espeakng.Speaker()

    # Set custom properties
    mySpeaker.amplitude = 50  # Adjust amplitude (default is 100)
    mySpeaker.wordgap = 4         # Set word gap (default is 10)
    mySpeaker.wpm = 140     # Set speech rate (default is 175)
    mySpeaker.voice = 'mb-us1' # Select the US male voice (default is 'en')
    mySpeaker.pitch = 60

    # Say the provided text
    mySpeaker.say("I'm under the water, please help me ooooooooo!")

if __name__ == "__main__":
    main()
