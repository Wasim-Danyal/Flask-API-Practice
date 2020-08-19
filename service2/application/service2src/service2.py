import random

def animalname():
    animal_names = [
        "Lion",
        "Tiger",
        "Cow",
        "Pig",
        "Wolf",        
    ]

    return random.choice(animal_names)

def animalnoise(animal):
    animal_noises_dict= {
        "Lion" : "Roar"
        "Tiger" : "Growl"
        "Cow" : "Moo" 
        "Pig" : "Oink"
        "Wolf" : "Howl"
    }

    return animalnoise.get(animal)