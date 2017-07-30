# -*- coding: utf-8 -*-

from character_generator import Character
import sys

character = Character()

ancestry = sys.argv[1]

attributes = character.generate_ancestry(ancestry)

strength = attributes["strength"]
agility = attributes["agility"]
intelect = attributes["intelect"]
will = attributes["will"]
perception = intelect
defense = agility
health = strength
healing_rate = str(int(round(int(health)/4, 0)))
size = attributes["size"]
speed = attributes["speed"]
power = attributes["power"]
damage = attributes["damage"]
insanity = attributes["insanity"]
corruption = attributes["corruption"]
language = attributes["languages"]
background = character.generate_random(ancestry, "_background" , "1d20").encode("utf-8")
personality = character.generate_random(ancestry, "_personality", "3d6").encode("utf-8")
religion = character.generate_random(ancestry, "_religion", "3d6").encode("utf-8")
age = character.generate_random(ancestry, "_age", "3d6").encode("utf-8")
build = character.generate_random(ancestry, "_build", "3d6").encode("utf-8")
appearence = character.generate_random(ancestry, "_appearence", "3d6").encode("utf-8")
true_age = character.generate_random(ancestry, "_true_age", "3d6").encode("utf-8")
apparent_gender = character.generate_random(ancestry, "_apparent_gender", "1d6").encode("utf-8")
apparent_ancestry = character.generate_random(ancestry, "_apparent_ancestry", "3d6").encode("utf-8")
quirk = character.generate_random(ancestry, "_quirk", "1d20").encode("utf-8")
form = character.generate_random(ancestry, "_form", "3d6").encode("utf-8")
purpose = character.generate_random(ancestry, "_purpose", "1d20").encode("utf-8")
hatred = character.generate_random(ancestry, "_hatred", "1d20").encode("utf-8")

print "Strength: " + strength
print "Agility: " + agility
print "Intelect: " + intelect
print "Will: " + will
print "Perception: " + intelect
print "Defense: " + agility
print "Health: " + health
print "Healing Rate: " + healing_rate
print "Size: " + size
print "Speed: " + speed
print "Power: " + power
print "Damage: " + damage
print "Insanity: " + insanity
print "Corruption: " + corruption
print "Languages: " + language
print "Background: " + background
print "Personality: " + personality

if ancestry == "human":
    print "Religion: " + religion
    print "Age: " + age
    print "Build: " + build
    print "Appearence: " + appearence
elif ancestry == "changeling":
    print "True Age: " + true_age
    print "Apparent Gender: " + apparent_gender
    print "Apparent Ancestry: " + apparent_ancestry
    print "Quirk" + ": " + quirk
elif ancestry == "clockwork":
    print "Form: " + form
    print "Purpose: " + purpose
elif ancestry == "dwarf":
    print "Age: " + age
    print "Appearence: " + appearence
    print "Background: " + background
    print "Build: " + build
    print "Hatred: " + hatred
    print "Personality: " + personality
elif ancestry == "goblin":
    print "Goblin"
elif ancestry == "orc":
    print "Orc"
