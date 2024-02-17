import random

fires = [
    "The fire was lower but still burning",
    "A man trying to fire the place",
    "People burning crackers on the wall",
    "There is a fire in the jungle",
    "There is a fire in the woods",
    "There is a fire in the workstation",
    "There is a fire in the building",
    "There is a fire in the power plant"
    "There is a fire in the house"
]
guns = [
    "A man holding gun",
    "A man pointing the gun",
    "A black man aiming gun",
    "Black gun in hand",
    "Group of people having gun",
    "Men aiming gun on each other"
]
knifes = [
    "A man holding knife",
    "Knife on table",
    "Man keeping knife in bag",
    "A man pointing knife",
    "A man holding knife",
    "Man keeping knife on neck of other person",
    "Knife under belt"
]


def predict_caption(string):
    if string==2:
        caption = random.choice(fires)
        fires.remove(caption)
    elif string==0:
        caption = random.choice(guns)
        guns.remove(caption)
    elif string==1:
        caption = random.choice(knifes)
        knifes.remove(caption)
    return caption
