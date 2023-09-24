# My First ever project
#                       Text speaker

import pyttsx3

if __name__ == '__main__':
    # ex=pyttsx3.init()
    # ex.say('how r u')
    # ex.runAndWait()

    print("\t\tWELCOME!!\nThis is Rohit's Text speaker ", end='\t\t')
    sample = ' '
    print("(To exit the Speaker enter 'Q')")
    while sample != 'Q':
        sample = input('Enter the Text to Listen to that: ')
        aud = pyttsx3.init()
        if sample == 'Q':
            aud.say('Thank You for Using Me')
            aud.runAndWait()
            break
        aud.say(sample)
        aud.runAndWait()
