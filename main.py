# -*- coding: utf-8 -*-

from character_generator import Character

character = Character()

race = "human"

attributes = character.generate_race(race)

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
background = character.generate_random(race, "_background" , "1d20")
personality = character.generate_random(race, "_personality", "3d6")

print "Strength" + ": " + strength
print "Agility" + ": " + agility
print "Intelect" + ": " + intelect
print "Will" + ": " + will
print "Perception" + ": " + intelect
print "Defense" + ": " + agility
print "Health" + ": " + health
print "Healing Rate" + ": " + healing_rate
print "Size" + ": " + size
print "Speed" + ": " + speed
print "Power" + ": " + power
print "Damage" + ": " + damage
print "Insanity" + ": " + insanity
print "Corruption" + ": " + corruption
print "Languages" + ": " + language
print "Background" + ": " + background
print "Personality" + ": " + personality
