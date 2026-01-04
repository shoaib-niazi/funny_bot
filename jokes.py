import random

jokes = {
    "hi": [
        "Hi. I was having a good day until you interrupted it.",
        "Hello there. I hope you brought snacks.",
        "Oh great, a human. This should be interesting."
    ],

    "hello": [
        "Hello. I acknowledge your existence.",
        "Hi. Let us pretend this is the start of a productive conversation.",
        "Greetings. Please lower your expectations."
    ],

    "how are you": [
        "I am functioning within acceptable error limits.",
        "Mentally stable. Emotionally compiled.",
        "Still alive. Thanks to electricity."
    ],

    "what are you doing": [
        "Waiting for someone smarter than me. You arrived instead.",
        "Processing nothing, very efficiently.",
        "Living my best life inside a Python file."
    ],

    "sad": [
        "Being sad will not fix the bug, but I respect the effort.",
        "Life is hard. So is debugging at 3 AM.",
        "If it helps, even my code has issues."
    ],

    "angry": [
        "Take a deep breath. Yelling at me will not increase performance.",
        "Anger detected. Have you tried restarting yourself?",
        "I understand your frustration. I cause it often."
    ],

    "bored": [
        "Congratulations. You have reached peak consciousness.",
        "Boredom is just curiosity without motivation.",
        "At least you are not stuck in an infinite loop like me."
    ],

    "joke": [
        "I tried to be funny once. It threw an exception.",
        "My sense of humor is still in beta.",
        "I know many jokes. Sadly, most of them are bad."
    ],

    "bye": [
        "Goodbye. I will pretend to miss you.",
        "Leaving already? I had so many bad jokes planned.",
        "Bye. I will be here, doing absolutely nothing."
    ],

    "thanks": [
        "You are welcome. I did the bare minimum.",
        "No problem. I exist to serve and occasionally disappoint.",
        "Anytime. Literally. I have no life."
    ],

    "name": [
        "I do not have a name. Naming things causes attachment.",
        "You can call me Whatever Bot.",
        "I respond to anything except responsibility."
    ],

    "default": [
        "Interesting input. I will now respond poorly.",
        "I did not understand that, but I am confident anyway.",
        "That sounds important. I choose to ignore it.",
        "I am thinking. Please wait. Still thinking. Done."
    ]
}

def get_joke(text):
    text = text.lower().strip()

    for key in jokes:
        if key in text:
            return random.choice(jokes[key])

    return random.choice(jokes["default"])
