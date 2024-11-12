import random

songs = {
    "sad": ["SKINNY", "WILDFLOWER"],
    "chill": ["CHIHIRO", "BITTERSUITE"],
    "emotional": ["THE GREATEST", "BLUE"],
    "happy": ["BIRDS OF A FEATHER"],
    "horny": ["LUNCH"],
    "angry": ["THE DINER", "L'AMOUR DE MA VIE"],
    "bored": ["SKINNY", "WILDFLOWER", "CHIHIRO", "BITTERSUITE", "THE GREATEST", "BLUE", "BIRDS OF A FEATHER", "LUNCH", "THE DINER", "L'AMOUR DE MA VIE"]
}

def pick_song(mood):
    mood = mood.lower()
    if mood in songs:
        return random.choice(songs[mood])
    else:
        return "Mood not recognized. Please choose from: sad, chill, emotional, happy, horny, angry, or bored."

user_mood = input("How are you feeling? (e.g., sad, chill, emotional, happy, horny, angry, bored): ")
suggested_song = pick_song(user_mood)

print(f"Based on your mood, you should listen to: {suggested_song}")